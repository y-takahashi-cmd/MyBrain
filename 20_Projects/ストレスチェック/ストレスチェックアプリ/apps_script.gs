// ===== 社員コンディションチェック｜Google Apps Script =====
// スプレッドシートIDをここに入れてください
const SHEET_ID = 'YOUR_SPREADSHEET_ID';
const SHEET_NAME = '回答データ';
const ADMIN_PASSWORD = 'kanon2026';

// セッションアンケート用シート名
const SESSION_SHEET_NAME = 'セッションアンケート';

// ===== POST：回答データを受け取って保存 =====
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(SHEET_ID);

    // セッションアンケート（pre / mid / post）
    if (data.surveyType === 'pre' || data.surveyType === 'mid' || data.surveyType === 'post') {
      return saveSessionSurvey(ss, data);
    }

    // ストレスチェック（既存）
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(['社員ID','企業ID','年月','Q1_体調','Q2_集中力','Q3_ストレス','Q4_睡眠','Q5_人間関係','Q6_仕事量','タイムスタンプ']);
    }
    sheet.appendRow([
      data.employeeId,
      data.companyId,
      data.yearMonth,
      data.Q1, data.Q2, data.Q3, data.Q4, data.Q5, data.Q6,
      data.timestamp || new Date().toISOString()
    ]);
    return ContentService.createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch(err) {
    return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function saveSessionSurvey(ss, data) {
  let sheet = ss.getSheetByName(SESSION_SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SESSION_SHEET_NAME);
    sheet.appendRow([
      'アンケート種別','クライアントID','企業ID','セッション日',
      'Q1','Q2','Q3',
      'T1（記述1）','T2（記述2）','T3（記述3）','T4（記述4）',
      'アクション達成率','タイムスタンプ'
    ]);
  }
  sheet.appendRow([
    data.surveyType,
    data.clientId,
    data.companyId,
    data.sessionDate,
    data.Q1 || '',
    data.Q2 || '',
    data.Q3 || '',
    data.T1 || '',
    data.T2 || '',
    data.T3 || '',
    data.T4 || '',
    data.actionPercent !== undefined ? data.actionPercent : '',
    data.timestamp || new Date().toISOString()
  ]);
  return ContentService.createTextOutput(JSON.stringify({ status: 'ok' }))
    .setMimeType(ContentService.MimeType.JSON);
}

// ===== GET：データを返す =====
function doGet(e) {
  const params = e.parameter;
  const action  = params.action || '';
  const pw      = params.pw || '';
  const company = params.company || '';

  const ss    = SpreadsheetApp.openById(SHEET_ID);
  const sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) return jsonResponse([]);

  const rows = sheet.getDataRange().getValues();
  const header = rows[0];
  const data = rows.slice(1).map(row => ({
    employeeId: row[0],
    companyId:  row[1],
    yearMonth:  row[2],
    Q1: Number(row[3]),
    Q2: Number(row[4]),
    Q3: Number(row[5]),
    Q4: Number(row[6]),
    Q5: Number(row[7]),
    Q6: Number(row[8]),
    timestamp:  row[9],
  }));

  // 管理者：全データ
  if (action === 'all' && pw === ADMIN_PASSWORD) {
    return jsonResponse(data);
  }

  // セッションアンケート全件（管理者のみ）
  if (action === 'sessions-all' && pw === ADMIN_PASSWORD) {
    const sSheet = ss.getSheetByName(SESSION_SHEET_NAME);
    if (!sSheet) return jsonResponse([]);
    const sRows = sSheet.getDataRange().getValues();
    const sData = sRows.slice(1).map(row => ({
      surveyType:    row[0],
      clientId:      row[1],
      companyId:     row[2],
      sessionDate:   row[3],
      Q1: row[4] !== '' ? Number(row[4]) : null,
      Q2: row[5] !== '' ? Number(row[5]) : null,
      Q3: row[6] !== '' ? Number(row[6]) : null,
      T1: row[7], T2: row[8], T3: row[9], T4: row[10],
      actionPercent: row[11] !== '' ? Number(row[11]) : null,
      timestamp: row[12],
    }));
    return jsonResponse(sData);
  }

  // 企業：自社データのみ・個人ID不変のまま返す（admin側で氏名と紐づけ）
  if (action === 'company' && company) {
    const filtered = data
      .filter(d => d.companyId === company)
      .map(d => ({
        // 企業向けには employeeId を匿名化
        employeeId: anonymize(d.employeeId, company),
        companyId: d.companyId,
        yearMonth: d.yearMonth,
        Q1: d.Q1, Q2: d.Q2, Q3: d.Q3,
        Q4: d.Q4, Q5: d.Q5, Q6: d.Q6,
      }));
    return jsonResponse(filtered);
  }

  return jsonResponse({ error: 'unauthorized' });
}

// 企業向けに個人IDを匿名化（A001→社員1 等）
function anonymize(id, company) {
  // 同じIDは常に同じ番号になるようにする（集計の一貫性のため）
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let mapSheet = ss.getSheetByName('ID匿名化_' + company);
  if (!mapSheet) {
    mapSheet = ss.insertSheet('ID匿名化_' + company);
    mapSheet.appendRow(['元ID','匿名ID']);
  }
  const mapData = mapSheet.getDataRange().getValues();
  for (let i = 1; i < mapData.length; i++) {
    if (mapData[i][0] === id) return mapData[i][1];
  }
  const newAnon = '社員' + mapData.length;
  mapSheet.appendRow([id, newAnon]);
  return newAnon;
}

function jsonResponse(data) {
  return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

// ===== 月次リマインドメール送信（毎月1日に実行するトリガーを設定） =====
function sendMonthlyReminder() {
  const ss        = SpreadsheetApp.openById(SHEET_ID);
  const memberSheet = ss.getSheetByName('メンバーリスト');
  if (!memberSheet) return;

  const members = memberSheet.getDataRange().getValues();
  const baseUrl = 'YOUR_APP_URL'; // デプロイ後のindex.htmlのURL

  members.slice(1).forEach(row => {
    const name      = row[0];
    const email     = row[1];
    const id        = row[2];
    const companyId = row[3];
    if (!email) return;

    const url = `${baseUrl}?id=${id}&company=${companyId}`;
    GmailApp.sendEmail(
      email,
      '【コンディションチェック】今月の回答をお願いします',
      `${name} さん\n\n毎月のコンディションチェックの時間です。\n約1分で終わります。\n\n▶ 回答はこちら\n${url}\n\n企業のオンライン保健室　髙橋由香`
    );
  });
}
