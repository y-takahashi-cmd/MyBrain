const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const IMG = "C:/Users/y-takahashi/MyBrain/20_Projects/BNI_REALIZE/メインプレゼン_素材";
const OUT = process.argv[2];

const G = "1F6B45", G_L = "EAF4EC", O = "E8742A", O_L = "FDEFE4", TX = "333333", GR = "6B6B6B", W = "FFFFFF";
const F = "Meiryo";

function pngSize(p) {
  const b = fs.readFileSync(p);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}
function img(name) { return path.join(IMG, name + ".png"); }
function exists(name) { return fs.existsSync(img(name)); }

// fit image inside box (contain), centered
function addImg(slide, name, x, y, w, h) {
  if (!exists(name)) { return; }
  const s = pngSize(img(name));
  if (!["nurse_chara", "logo_mark"].includes(name)) {
    // cover: fill the box, crop overflow
    const c = Math.max(w / s.w, h / s.h);
    slide.addImage({ path: img(name), x, y, w: s.w * c, h: s.h * c, sizing: { type: "cover", w, h }, objectName: "img_" + name });
    return;
  }
  const r = Math.min(w / s.w, h / s.h);
  const iw = s.w * r, ih = s.h * r;
  slide.addImage({ path: img(name), x: x + (w - iw) / 2, y: y + (h - ih) / 2, w: iw, h: ih, objectName: "img_" + name });
}
function shadow() { return { type: "outer", color: "000000", opacity: 0.12, blur: 6, offset: 2, angle: 90 }; }
function card(slide, x, y, w, h, fill) {
  slide.addShape("roundRect", { x, y, w, h, fill: { color: fill || W }, line: { color: fill || W }, rectRadius: 0.12, shadow: shadow() });
}
function t(slide, text, o) {
  slide.addText(text, Object.assign({ fontFace: F, color: TX, isTextBox: true, margin: 0, valign: "top" }, o));
}
function title(slide, text) {
  t(slide, text, { x: 0.5, y: 0.3, w: 9, h: 0.6, fontSize: 24, bold: true, color: G, valign: "middle" });
}

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "企業のオンライン保健室 メインプレゼン";
pres.author = "髙橋由香";

// ---------- 1 表紙 ----------
{
  const s = pres.addSlide(); s.background = { color: G };
  t(s, "BNI REALIZE　メインプレゼン", { x: 0.6, y: 0.6, w: 5.6, h: 0.35, fontSize: 14, color: "CFE6D6" });
  t(s, "企業のオンライン保健室", { x: 0.6, y: 1.25, w: 5.8, h: 0.8, fontSize: 34, bold: true, color: W });
  t(s, "ストレスチェック、\nやった後、どうしていますか？", { x: 0.6, y: 2.2, w: 5.8, h: 1.1, fontSize: 22, color: W, bold: true, lineSpacingMultiple: 1.1 });
  s.addShape("roundRect", { x: 0.6, y: 3.6, w: 3.6, h: 0.55, fill: { color: O }, line: { color: O }, rectRadius: 0.1 });
  t(s, "出勤できなくなる前に", { x: 0.6, y: 3.6, w: 3.6, h: 0.55, fontSize: 18, bold: true, color: W, align: "center", valign: "middle" });
  t(s, "髙橋 由香", { x: 0.6, y: 4.55, w: 4, h: 0.45, fontSize: 18, color: W, bold: true });
  card(s, 6.6, 0.55, 2.9, 4.5, W);
  addImg(s, "nurse_chara", 6.75, 0.7, 2.6, 4.2);
  s.addNotes("皆さん、こんにちは。企業のオンライン保健室の髙橋由香です。");
}

// ---------- 2 自己紹介 ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "看護師として、命と向き合ってきました");
  card(s, 0.5, 1.2, 2.7, 1.55, G_L);
  t(s, "20年以上", { x: 0.65, y: 1.32, w: 2.4, h: 0.7, fontSize: 32, bold: true, color: G });
  t(s, "看護師として、患者さんや\nご家族と関わってきました", { x: 0.65, y: 2.02, w: 2.45, h: 0.65, fontSize: 12, color: TX });
  card(s, 3.45, 1.2, 2.7, 1.55, O_L);
  t(s, "余命1年", { x: 3.6, y: 1.32, w: 2.4, h: 0.7, fontSize: 32, bold: true, color: O });
  t(s, "私自身も、がんで\n宣告を受けた経験があります", { x: 3.6, y: 2.02, w: 2.45, h: 0.65, fontSize: 12, color: TX });
  t(s, "だからこそ、心と体は\n働くことにも、生きることにも\n欠かせない土台だと知っています", { x: 0.5, y: 3.1, w: 5.7, h: 1.4, fontSize: 18, bold: true, color: TX, lineSpacingMultiple: 1.2 });
  card(s, 6.5, 1.2, 3.0, 3.6, W);
  addImg(s, "logo_mark", 6.65, 1.4, 2.7, 3.2);
  s.addNotes("私は20年以上、看護師として、たくさんの患者さんやご家族と関わってきました。そして私自身も、がんで「余命1年」と宣告された経験があります。だからこそ、心と体は、働くことにも、生きることにも欠かせない土台だと、身にしみて知っています。");
}

// ---------- 3 ストレスチェックと義務化 ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "私の仕事は、会社のストレスチェックです");
  t(s, "社員さんの心の状態を年に1回確かめる、\n法律で決められた検査です", { x: 0.5, y: 1.1, w: 5.6, h: 0.75, fontSize: 15, color: TX });
  card(s, 0.5, 2.1, 2.5, 2.3, G_L);
  t(s, "今", { x: 0.65, y: 2.25, w: 2.2, h: 0.4, fontSize: 14, bold: true, color: GR });
  t(s, "社員50名以上の\n会社が義務", { x: 0.65, y: 2.75, w: 2.2, h: 1.2, fontSize: 18, bold: true, color: G });
  t(s, "▶", { x: 3.05, y: 2.95, w: 0.4, h: 0.6, fontSize: 22, color: O, align: "center" });
  card(s, 3.5, 2.1, 2.6, 2.3, O_L);
  t(s, "2028年4月から", { x: 3.65, y: 2.25, w: 2.35, h: 0.4, fontSize: 14, bold: true, color: O });
  t(s, "50名未満の\n小さな会社も\n義務に", { x: 3.65, y: 2.75, w: 2.35, h: 1.4, fontSize: 18, bold: true, color: O });
  t(s, "出典：厚生労働省（令和10年4月1日施行）", { x: 0.5, y: 4.6, w: 5.6, h: 0.3, fontSize: 10, color: GR });
  card(s, 6.4, 1.1, 3.1, 3.8, W);
  addImg(s, "smartphone", 6.5, 1.2, 2.9, 3.6);
  s.addNotes("私の仕事は、会社のストレスチェックです。ストレスチェックは、社員さんの心の状態を年に1回確かめる、法律で決められた検査です。2028年4月からは、50名未満の小さな会社も義務になります。");
}

// ---------- 4 問いかけ ----------
{
  const s = pres.addSlide(); s.background = { color: G_L };
  t(s, "皆さんに、質問です", { x: 0.6, y: 0.7, w: 5, h: 0.4, fontSize: 16, bold: true, color: G });
  t(s, "ストレスチェック、\nやった後、\nどうしていますか？", { x: 0.6, y: 1.25, w: 5, h: 2.3, fontSize: 32, bold: true, color: G, lineSpacingMultiple: 1.15 });
  t(s, "実は、やって終わりになっている会社がほとんどです。\nやるだけでは、何も変わりません。", { x: 0.6, y: 3.85, w: 5, h: 0.8, fontSize: 14, color: TX });
  card(s, 5.9, 0.7, 3.6, 4.2, W);
  addImg(s, "q_shacho", 6.0, 0.8, 3.4, 4.0);
  s.addNotes("ここで、皆さんに質問です。「ストレスチェック、やった後、どうしていますか？」実は、やって終わりになっている会社がほとんどです。でも、ストレスチェックは、やるだけでは何も変わりません。");
}

// ---------- 5 変わるのは2つ ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "結果が出たら、変わらなければいけないことが2つ");
  const cols = [
    { x: 0.5, img: "kaisha", head: "① 会社", body: "どの部署で、何が負担になっているのか。\n会社として手を打つ", c: G, bg: G_L },
    { x: 5.1, img: "honnin", head: "② 社員さんご本人", body: "睡眠や体の疲れ、気持ちの持ち方。\n自分でバランスを整える", c: G, bg: G_L },
  ];
  cols.forEach(o => {
    card(s, o.x, 1.05, 4.4, 2.95, o.bg);
    addImg(s, o.img, o.x + 0.15, 1.15, 4.1, 1.6);
    t(s, o.head, { x: o.x + 0.25, y: 2.85, w: 3.9, h: 0.4, fontSize: 17, bold: true, color: o.c });
    t(s, o.body, { x: o.x + 0.25, y: 3.25, w: 3.9, h: 0.7, fontSize: 13, color: TX });
  });
  s.addShape("roundRect", { x: 1.5, y: 4.3, w: 7, h: 0.75, fill: { color: O }, line: { color: O }, rectRadius: 0.12 });
  t(s, "両方そろわないと、ストレスが積み重なって　休職・退職へ", { x: 1.5, y: 4.3, w: 7, h: 0.75, fontSize: 17, bold: true, color: W, align: "center", valign: "middle" });
  s.addNotes("結果が出たら、変わらなければいけないことが2つあります。1つは、会社。どの部署で、何が負担になっているのか。会社として手を打つこと。もう1つは、社員さんご本人。睡眠や体の疲れ、気持ちの持ち方。自分でバランスを整えること。この両方がそろわないと、ストレスは高いまま積み重なって、休職や退職につながってしまいます。");
}

// ---------- 6 アプリ ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "専用アプリで、準備から分析までかんたん");
  const steps = [
    { n: "1", h: "準備", b: "必要な準備は、\n画面の手順にそって\n進めるだけ" },
    { n: "2", h: "受検", b: "社員さんは\nスマホで\nいつでも回答" },
    { n: "3", h: "分析", b: "回収後の集団分析は\nボタン一つで\nできあがり" },
  ];
  steps.forEach((o, i) => {
    const x = 0.5 + i * 2.05;
    card(s, x, 1.15, 1.8, 3.1, G_L);
    s.addShape("ellipse", { x: x + 0.6, y: 1.35, w: 0.6, h: 0.6, fill: { color: G }, line: { color: G } });
    t(s, o.n, { x: x + 0.6, y: 1.35, w: 0.6, h: 0.6, fontSize: 20, bold: true, color: W, align: "center", valign: "middle" });
    t(s, o.h, { x: x + 0.1, y: 2.1, w: 1.6, h: 0.45, fontSize: 18, bold: true, color: G, align: "center" });
    t(s, o.b, { x: x + 0.1, y: 2.65, w: 1.6, h: 1.4, fontSize: 12, color: TX, align: "center" });
    if (i < 2) t(s, "▶", { x: x + 1.8, y: 2.45, w: 0.25, h: 0.4, fontSize: 14, color: O, align: "center" });
  });
  t(s, "紙を配る・集める・集計する手間がなくなります", { x: 0.5, y: 4.45, w: 6, h: 0.4, fontSize: 14, bold: true, color: O });
  card(s, 6.85, 1.15, 2.65, 3.7, W);
  addImg(s, "smartphone", 6.95, 1.25, 2.45, 3.5);
  s.addNotes("しかも、専用のアプリがあるので、とても便利です。準備は、画面の手順にそって進めるだけ。社員さんはスマホで受けられて、回収した後の集団分析も、ボタン一つで出てきます。");
}

// ---------- 7 やった後を支える ----------
{
  const s = pres.addSlide(); s.background = { color: G_L };
  title(s, "「やった後」を、会社と社員さんの両方から支えます");
  card(s, 0.5, 1.1, 4.3, 1.5, W);
  t(s, "会社へ", { x: 0.7, y: 1.22, w: 3.9, h: 0.4, fontSize: 16, bold: true, color: G });
  t(s, "部署ごとの分析から、「どこに、どんな手を打てばいいか」をお伝えします", { x: 0.7, y: 1.65, w: 3.9, h: 0.85, fontSize: 13, color: TX });
  card(s, 0.5, 2.8, 4.3, 1.5, W);
  t(s, "社員さんへ（プレミアムプラン）", { x: 0.7, y: 2.92, w: 3.9, h: 0.4, fontSize: 16, bold: true, color: O });
  t(s, "ストレスが高く出た方のお話を看護師の経験で聞き、その人に合った整え方を一緒に。必要なら受診へ", { x: 0.7, y: 3.35, w: 3.9, h: 0.85, fontSize: 13, color: TX });
  t(s, "実施者の資格あり。社員さん一人ひとりの結果は会社に見えないので、安心して本音で答えられます", { x: 0.5, y: 4.45, w: 4.4, h: 0.6, fontSize: 11, color: GR });
  card(s, 5.1, 1.1, 4.4, 3.95, W);
  addImg(s, "online", 5.2, 1.2, 4.2, 3.75);
  s.addNotes("企業のオンライン保健室は、この「やった後」を、会社と社員さんの両方から支えます。会社には、部署ごとの分析から「どこに、どんな手を打てばいいか」をお伝えします。さらにご希望の会社には、ストレスが高く出た社員さんに、看護師の経験を生かしてオンラインでお話を聞き、その人に合った整え方を一緒に見つけます。必要なら受診にもつなげます。私は実施者の資格を持っていて、社員さん一人ひとりの結果は会社には見えません。だから社員さんも、安心して本音で答えられます。");
}

// ---------- 8 想い ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "始まりは、ある社長さんからの一本の相談でした");
  const st = [
    { q: "「会社に来られなくなった社員を見てほしい」", a: "お話を重ねるうちに、また出勤できるように" },
    { q: "「右腕が辞めると言っている」", a: "ご本人が本当の気持ちに気づき、会社に残って改革へ" },
  ];
  st.forEach((o, i) => {
    const x = 0.5 + i * 3.1;
    card(s, x, 1.1, 2.85, 2.5, G_L);
    t(s, o.q, { x: x + 0.2, y: 1.25, w: 2.45, h: 0.95, fontSize: 15, bold: true, color: G });
    t(s, "▼", { x: x + 0.2, y: 2.2, w: 2.45, h: 0.3, fontSize: 12, color: O, align: "center" });
    t(s, o.a, { x: x + 0.2, y: 2.55, w: 2.45, h: 0.9, fontSize: 13, color: TX });
  });
  s.addShape("roundRect", { x: 0.5, y: 3.9, w: 5.95, h: 1.05, fill: { color: O_L }, line: { color: O_L }, rectRadius: 0.12 });
  t(s, "気づいた後に、会社も本人も動けるように寄りそう。\nそれが、企業のオンライン保健室をつくった理由です", { x: 0.7, y: 3.98, w: 5.6, h: 0.9, fontSize: 14, bold: true, color: O, valign: "middle" });
  card(s, 6.75, 1.1, 2.75, 3.85, W);
  addImg(s, "nurse_chara", 6.85, 1.2, 2.55, 3.65);
  s.addNotes("始まりは、ある社長さんからの一本の相談でした。「会社に来られなくなった社員を見てほしい」。お話を重ねるうちに、その方はまた出勤できるようになりました。次の相談は、「右腕が辞めると言っている」。セッションの中で、ご本人が自分の本当の気持ちに気づき、会社に残って改革を進めてくれました。看護師時代、私は病気になってから出会う方をたくさん見てきました。もっと早く気づけていたら。そう思うことが何度もありました。ストレスチェックは、その「早く気づく」ための入口です。でも、気づいただけでは、誰も救われません。気づいた後に、会社も本人も動けるように寄りそう。それが、私が企業のオンライン保健室をつくった理由です。");
}

// ---------- 9 料金 ----------
{
  const s = pres.addSlide(); s.background = { color: G_L };
  title(s, "選べる3つのプラン（1人あたり・年額）");
  const plans = [
    { n: "ライト", p: "2,600", d: "低コストで始めたい会社に", it: ["ストレスチェック（年1回）", "集団分析レポート（簡易版）", "報告書（PDF）"], c: G },
    { n: "スタンダード", p: "5,400", d: "実施者に任せて安心", it: ["ストレスチェック（年1回）", "集団分析レポート（詳細版）", "報告書（PDF）"], c: "2E6BA6" },
    { n: "プレミアム", p: "14,400", d: "やった後まで、まるごと", it: ["ストレスチェック実施", "集団分析レポート（詳細版）", "高ストレスの方の面談", "医師の面接へのつなぎ", "保健室だより"], c: O },
  ];
  plans.forEach((o, i) => {
    const x = 0.5 + i * 3.05, y = 1.05, w = 2.85, h = 3.85;
    card(s, x, y, w, h, W);
    s.addShape("roundRect", { x, y, w, h: 0.55, fill: { color: o.c }, line: { color: o.c }, rectRadius: 0.12 });
    t(s, o.n + (i === 2 ? "　おすすめ" : ""), { x, y, w, h: 0.55, fontSize: 16, bold: true, color: W, align: "center", valign: "middle" });
    t(s, o.d, { x: x + 0.15, y: y + 0.65, w: w - 0.3, h: 0.3, fontSize: 11, color: GR, align: "center" });
    t(s, [{ text: o.p, options: { fontSize: 28, bold: true, color: o.c } }, { text: " 円×人数", options: { fontSize: 12, color: TX } }], { x: x + 0.1, y: y + 0.95, w: w - 0.2, h: 0.6, align: "center", valign: "middle" });
    t(s, o.it.map((v, k) => ({ text: v, options: { bullet: true, breakLine: k < o.it.length - 1 } })), { x: x + 0.2, y: y + 1.7, w: w - 0.35, h: 2.05, fontSize: 11, color: TX, paraSpaceAfter: 3 });
  });
  t(s, "初期費用：各プラン 50,000円　／　プレミアムの面談は10人あたり年6回まで含む", { x: 0.5, y: 5.0, w: 9, h: 0.3, fontSize: 10, color: GR });
  s.addNotes("料金は、ライト・スタンダード・プレミアムの3つのプランから選べます。（料金の説明は短く。おすすめはプレミアム。）");
}

// ---------- 10 金の卵 ----------
{
  const s = pres.addSlide(); s.background = { color: W };
  title(s, "金の卵：ストレスチェックをやりたい会社");
  t(s, "会社の大きさは問いません", { x: 0.5, y: 0.9, w: 5.8, h: 0.35, fontSize: 14, bold: true, color: O });
  const ex = ["2028年4月から義務になる、社員50名未満の会社", "紙でやっていて、配る・集める・集計が大変な会社", "結果をもらっても、「そのあと」が何もできていない会社"];
  ex.forEach((v, i) => {
    card(s, 0.5, 1.4 + i * 0.68, 5.8, 0.55, G_L);
    t(s, v, { x: 0.7, y: 1.4 + i * 0.68, w: 5.5, h: 0.55, fontSize: 13, color: TX, valign: "middle" });
  });
  s.addShape("roundRect", { x: 0.5, y: 3.6, w: 5.8, h: 1.35, fill: { color: O_L }, line: { color: O_L }, rectRadius: 0.12 });
  t(s, "つなぐ時のひと言", { x: 0.7, y: 3.68, w: 5.4, h: 0.3, fontSize: 11, bold: true, color: O });
  t(s, "「ストレスチェックから、そのあとの社員さんのフォローまでやってくれる髙橋さんがいるよ。一度話してみませんか？」", { x: 0.7, y: 4.0, w: 5.4, h: 0.85, fontSize: 13, bold: true, color: TX });
  card(s, 6.6, 0.9, 2.9, 4.05, W);
  addImg(s, "egg_goose", 6.7, 1.0, 2.7, 3.85);
  s.addNotes("今日の金の卵は、「ストレスチェックをやりたい、やらなきゃいけない会社」です。会社の大きさは問いません。例えば、2028年4月から義務になる社員50名未満の会社、今、紙でストレスチェックをやっていて、配る・集める・集計するのが大変な会社、結果をもらっても「そのあと」が何もできていない会社。こんな言葉を聞いたら、私を思い出してください。「ストレスチェック、うちもやらなきゃいけないらしいね」「ストレスチェックの紙を集めるのが大変で」「最近、社員の元気がないんだよね」「大事な社員から、辞めたいと言われて」。つなぐ時は、この一言で十分です。「ストレスチェックから、そのあとの社員さんのフォローまでやってくれる、髙橋さんがいるよ。一度話してみませんか？」");
}

// ---------- 11 金のガチョウ ----------
{
  const s = pres.addSlide(); s.background = { color: G_L };
  title(s, "金のガチョウ：複数の企業を支援している専門家");
  card(s, 0.5, 1.1, 4.4, 1.6, W);
  t(s, "産業医さん", { x: 0.7, y: 1.2, w: 4, h: 0.45, fontSize: 18, bold: true, color: G });
  t(s, "ストレスチェックの実施や、その後の社員さんのフォローで協力したい。医師の面接を希望された時も、一緒に支えられます", { x: 0.7, y: 1.68, w: 4.0, h: 0.95, fontSize: 12, color: TX });
  card(s, 0.5, 2.95, 4.4, 1.3, W);
  t(s, "社会保険労務士さん", { x: 0.7, y: 3.05, w: 4, h: 0.45, fontSize: 18, bold: true, color: G });
  t(s, "これから義務化に備える中小企業を、一緒に支えたい", { x: 0.7, y: 3.52, w: 4.0, h: 0.6, fontSize: 12, color: TX });
  t(s, "そんな専門家をご存じなら、ぜひご紹介ください", { x: 0.5, y: 4.5, w: 4.6, h: 0.45, fontSize: 13, bold: true, color: O });
  card(s, 5.2, 1.1, 4.3, 3.85, W);
  addImg(s, "team", 5.3, 1.2, 4.1, 3.65);
  s.addNotes("そして、私にとっての金のガチョウは、複数の企業を支援している、産業医さんと社会保険労務士さんです。産業医さんとは、ストレスチェックの実施や、その後の社員さんのフォローで協力したい。ストレスが高く出た方が医師の面接を希望された時も、一緒に支えられます。社労士さんとは、これから義務化に備える中小企業を、一緒に支えたい。そんな専門家の方をご存じでしたら、ぜひご紹介ください。");
}

// ---------- 12 締め ----------
{
  const s = pres.addSlide(); s.background = { color: G };
  card(s, 0.5, 0.5, 4.3, 3.0, W);
  addImg(s, "genki", 0.6, 0.6, 4.1, 2.8);
  t(s, "社員さんが元気になれば、会社が元気になる。\n会社が元気になれば、家族も元気になる。", { x: 5.1, y: 0.6, w: 4.4, h: 1.0, fontSize: 14, color: W, bold: true });
  t(s, "周りの社長さんに、聞いてみてください", { x: 5.1, y: 1.8, w: 4.4, h: 0.35, fontSize: 12, color: "CFE6D6" });
  t(s, "「ストレスチェック、\nやった後、どうしていますか？」", { x: 5.1, y: 2.15, w: 4.4, h: 0.95, fontSize: 18, color: W, bold: true });
  s.addShape("roundRect", { x: 5.1, y: 3.25, w: 4.4, h: 0.6, fill: { color: O }, line: { color: O }, rectRadius: 0.1 });
  t(s, "出勤できなくなる前に", { x: 5.1, y: 3.25, w: 4.4, h: 0.6, fontSize: 20, bold: true, color: W, align: "center", valign: "middle" });
  t(s, "企業のオンライン保健室　髙橋 由香", { x: 0.5, y: 4.15, w: 9, h: 0.4, fontSize: 16, bold: true, color: W });
  t(s, "https://kokorocare.business　／　info@kokorocare.business", { x: 0.5, y: 4.6, w: 9, h: 0.35, fontSize: 12, color: "CFE6D6" });
  s.addNotes("社員さんが元気になれば、会社が元気になる。会社が元気になれば、そこで働く人の家族も元気になる。皆さんの周りの社長さんに、ぜひ聞いてみてください。「ストレスチェック、やった後、どうしていますか？」その答えに詰まる社長さんがいたら、ぜひ髙橋由香につないでください。「出勤できなくなる前に」。企業のオンライン保健室、髙橋由香でした。ありがとうございました。");
}

pres.writeFile({ fileName: OUT }).then(f => console.log("wrote", f));
