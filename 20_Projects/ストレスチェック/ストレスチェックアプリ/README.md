# 社員コンディションチェックアプリ

## ファイル構成

| ファイル | 用途 |
|---|---|
| `index.html` | 社員回答画面（URL配布用） |
| `admin.html` | 管理者画面（髙橋のみ・全データ閲覧） |
| `company.html` | 企業向け閲覧画面（集計のみ・個人特定不可） |
| `apps_script.gs` | Google Apps Script（データ保存・取得） |

---

## セットアップ手順

### Step 1：Googleスプレッドシート作成

1. Googleスプレッドシートを新規作成
2. スプレッドシートのURL中の ID をコピー
   - 例：`https://docs.google.com/spreadsheets/d/【ここ】/edit`

### Step 2：Google Apps Script設定

1. スプレッドシートの「拡張機能」→「Apps Script」を開く
2. `apps_script.gs` の内容を貼り付け
3. `SHEET_ID` に Step1 でコピーしたIDを入力
4. 「デプロイ」→「新しいデプロイ」→「ウェブアプリ」
   - アクセス：「全員」
   - 実行ユーザー：自分
5. デプロイされたURLをコピー（例：`https://script.google.com/macros/s/xxxxx/exec`）

### Step 3：HTMLファイルにURLを設定

`index.html`・`admin.html`・`company.html` の `YOUR_GAS_URL` を Step2のURLに書き換え

### Step 4：Netlify or Azure にデプロイ

既存の `kokorocare-presents` リポジトリにフォルダを追加してpushするか、新規リポジトリとしてデプロイ

---

## 社員への配布URL

```
https://your-domain/index.html?id=A001&company=CP
```

- `id`：社員ID（例：A001、A002…）
- `company`：企業ID（例：CP=クラウドパワー、SG=杉山事務所）

---

## 管理者パスワード

- 管理者（admin.html）：`kanon2026`

---

## 企業ごとのパスワード（company.html）

| 企業ID | パスワード | 企業名 |
|---|---|---|
| CP | cp2026 | クラウドパワー株式会社 |
| SG | sg2026 | 杉山耕一税理士事務所 |

※ 追加する場合は `company.html` の `COMPANY_PASSWORDS` オブジェクトに追記

---

## メンバーリストシート（リマインドメール用）

スプレッドシートに「メンバーリスト」シートを作成し以下の形式で入力：

| A：氏名 | B：メールアドレス | C：社員ID | D：企業ID |
|---|---|---|---|
| 田中太郎 | tanaka@example.com | A001 | CP |

Apps Scriptのトリガーで `sendMonthlyReminder` を毎月1日に実行するよう設定する。

---

## 改善判定ロジック

| 項目 | 改善の方向 |
|---|---|
| 体調・集中力・睡眠 | スコアが上がれば改善 ✅ |
| ストレス・人間関係・仕事量 | スコアが下がれば改善 ✅ |

改善率 = （今月 − 先月）÷ 先月 × 100（良好系）
改善率 = （先月 − 今月）÷ 先月 × 100（ストレス系）
