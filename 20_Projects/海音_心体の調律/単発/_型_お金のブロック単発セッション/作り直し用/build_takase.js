const pptxgen = require("pptxgenjs");
const { applyTheme } = require("C:/Users/y-takahashi/.claude/skills/synced/3a3b4b9f-13f5-4bed-b7b8-70eb4a39821b_952c28d6-8d48-49c2-acd6-0c34cb154e35/pptx/scripts/apply_theme.js");

const THEME = {
  name: "Kanon",
  headFontFace: "Yu Mincho",
  bodyFontFace: "Yu Gothic",
  colors: {
    dk1: "4A4440", lt1: "FFFFFF", dk2: "5C4A2E", lt2: "FDFAF4",
    accent1: "B08A4E", accent2: "8C6A34", accent3: "E9D9B6",
    accent4: "EFE8F6", accent5: "E6F3EF", accent6: "F8EBEE",
    hlink: "8C6A34", folHlink: "7A716A",
  },
};
const T = THEME.colors;
const OUT = process.argv[2] || "deck.pptx";
const IMG = __dirname + "/img/";

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625
pres.title = "胸の奥の痛みをほどく 単発セッション";
pres.author = "海音（かのん）〜心体の調律〜 髙橋由香";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;

// ---- layouts ----
pres.defineSlideMaster({
  title: "TITLE",
  background: { path: IMG + "gold_bg.jpg" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 1.55, w: 8.4, h: 1.3, fontFace: THEME.headFontFace, fontSize: 38, bold: true, color: C.text2, align: "center", valign: "middle" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 2.95, w: 8.4, h: 1.2, fontSize: 16, bold: true, color: C.text2, align: "center", valign: "top" }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "DIVIDER",
  background: { path: IMG + "q_bg.jpg" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.0, w: 8.4, h: 1.0, fontFace: THEME.headFontFace, fontSize: 36, bold: true, color: C.accent2, align: "center", valign: "middle" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.05, w: 8.4, h: 0.9, fontSize: 16, color: C.text1, align: "center", valign: "top" }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT",
  background: { color: T.lt1 },
  margin: [0.5, 0.5, 0.5, 0.5],
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.5, w: 9.0, h: 0.65, fontFace: THEME.headFontFace, fontSize: 24, bold: true, color: C.accent2, align: "left", valign: "middle", margin: 0 }, text: "" } },
    { text: { text: "海音（かのん）〜心体の調律〜", options: { x: 0.5, y: 5.2, w: 5, h: 0.3, fontSize: 9, color: C.accent1, margin: 0 } } },
  ],
  slideNumber: { x: 9.0, y: 5.2, w: 0.5, h: 0.3, fontSize: 9, color: T.accent1, align: "right" },
});
pres.defineSlideMaster({
  title: "QUESTION",
  background: { path: IMG + "q_bg.jpg" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 1.0, y: 1.7, w: 8.0, h: 1.7, fontFace: THEME.headFontFace, fontSize: 32, bold: true, color: C.text2, align: "center", valign: "middle" }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 1.0, y: 3.5, w: 8.0, h: 0.8, fontSize: 15, color: C.accent2, align: "center", valign: "top" }, text: "" } },
    { text: { text: "海音（かのん）〜心体の調律〜", options: { x: 0.5, y: 5.2, w: 5, h: 0.3, fontSize: 9, color: C.accent1, margin: 0 } } },
  ],
  slideNumber: { x: 9.0, y: 5.2, w: 0.5, h: 0.3, fontSize: 9, color: T.accent1, align: "right" },
});
pres.defineSlideMaster({ title: "IMAGE", background: { color: T.lt1 } });

// ---- helpers ----
function card(s, name, x, y, w, h, fill) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: name, x, y, w, h, rectRadius: 0.12, fill: { color: fill }, line: { color: T.accent3, width: 0.75 } });
}
function txt(s, name, text, o) { s.addText(text, Object.assign({ objectName: name, isTextBox: true, margin: 0.08, color: C.text1, fontSize: 15, valign: "top" }, o)); }
function label(s, text) { txt(s, "label", text, { x: 0.5, y: 0.2, w: 6, h: 0.3, fontSize: 11, bold: true, color: C.accent1, margin: 0 }); }
function circleNum(s, name, n, x, y, fill) {
  s.addShape(pres.shapes.OVAL, { objectName: name + "_c", x, y, w: 0.42, h: 0.42, fill: { color: fill || T.accent1 }, line: { type: "none" } });
  s.addText(String(n), { objectName: name + "_n", isTextBox: true, x, y, w: 0.42, h: 0.42, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0 });
}

// 講座：物語の1場面（上に物語の一文、左に資料、右に「お金で言うと」）
const STORY_TOTAL = 7;
function story(no, headline, file, ratio, money, notes) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S1 });
  label(s, `第2部　頭の構造を知る ｜ ${no} / ${STORY_TOTAL}`);
  s.addText(headline, { placeholder: "title" });
  const w = 5.6, h = w * ratio;
  s.addImage({ path: IMG + file, x: 0.5, y: 1.35, w, h, altText: "講座スライド" });
  card(s, "money_card", 6.35, 1.35, 3.15, h, T.accent6);
  txt(s, "money_head", "胸の痛みで言うと…", { x: 6.55, y: 1.5, w: 2.8, h: 0.4, fontSize: 15, bold: true, color: C.accent2 });
  txt(s, "money_body", money, { x: 6.55, y: 1.95, w: 2.8, h: h - 0.7, fontSize: 14, paraSpaceAfter: 6 });
  s.addNotes(notes);
}

// 質問：1枚に1つ
let qNo = 0;
const qFills = [T.accent4, T.accent6, T.accent5];
function question(section, labelText, q, hint, notes) {
  qNo++;
  const s = pres.addSlide({ masterName: "QUESTION", sectionTitle: section });
  s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
  txt(s, "qlabel", labelText, { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
  s.addText(q, { placeholder: "title" });
  if (hint) s.addText(hint, { placeholder: "body" });
  s.addNotes(notes);
}


// 由香さん用（見せないスライド。ここで画面共有を止める）
function facil(section, title, items, file) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: "misenai_band", x: 0.5, y: 0.2, w: 9.0, h: 0.55, rectRadius: 0.1, fill: { color: T.accent2 }, line: { type: "none" } });
  txt(s, "misenai", "【共有停止】", { x: 0.5, y: 0.2, w: 9.0, h: 0.55, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle", margin: 0 });
  txt(s, "facil_title", title, { x: 0.5, y: 0.85, w: 9.0, h: 0.45, fontFace: THEME.headFontFace, fontSize: 22, bold: true, color: C.accent2, margin: 0 });
  card(s, "facil_card", 0.5, 1.3, 5.9, 3.7, "FFF8E8");
  txt(s, "facil_list", items.map((t, i) => ({ text: t, options: { bullet: { type: "number" }, breakLine: i < items.length - 1 } })),
    { x: 0.65, y: 1.4, w: 5.6, h: 3.5, fontSize: 12, paraSpaceAfter: 3 });
  if (file) s.addImage({ path: IMG + file, x: 6.7, y: 1.3, w: 2.6, h: 3.68, altText: "ガイドブック" });
  s.addNotes("見せないスライド。画面共有を止めてから読む。読んだら次のスライドで共有を再開。");
}

// =========== はじめに ===========
pres.addSection({ title: "はじめに" });
let s = pres.addSlide({ masterName: "TITLE", sectionTitle: "はじめに" });
s.addImage({ path: IMG + "logo.png", x: 4.45, y: 0.45, w: 1.1, h: 1.065, altText: "海音ロゴ" });
s.addText("胸の奥の痛みをほどく\n単発セッション", { placeholder: "title" });
s.addText("髙瀨 三由紀 さん　120分\n海音（かのん）〜心体の調律〜　髙橋 由香", { placeholder: "body" });
s.addNotes("開始（11/2 月 9:00〜・120分）。お話を聴く→頭の仕組み→ワーク→エネルギーの順に進めることを伝える。書くのは由香が画面の中で行うので、髙瀨さんは話すこと・感じることに集中してOKと伝える。ご自身では痛すぎてヒーリングできなかったとのこと（病院ではなんともないと言われている＝エネルギーの痛み）なので、「今日はひとりで向き合わなくて大丈夫」と最初に伝える。");

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "はじめに" });
s.addText("今日の流れ（120分）", { placeholder: "title" });
const flow = [
  ["0〜25分", "第1部", "魂の傷を聴く", T.accent6],
  ["25〜45分", "第2部", "頭の構造を知る", T.accent4],
  ["45〜95分", "ワーク", "思い込みを\n書き換える", T.accent5],
  ["95〜110分", "エネルギー", "残った痛みを\n取り除く", "F4EEDF"],
  ["110〜120分", "まとめ", "変化を\n確かめる", T.accent4],
];
flow.forEach((f, i) => {
  const x = 0.5 + i * 1.84;
  card(s, "flow_card" + i, x, 1.6, 1.66, 2.5, f[3]);
  txt(s, "flow_time" + i, f[0], { x: x + 0.1, y: 1.75, w: 1.46, h: 0.4, fontSize: 13, color: C.accent2, bold: true, align: "center" });
  txt(s, "flow_part" + i, f[1], { x: x + 0.1, y: 2.25, w: 1.46, h: 0.5, fontSize: 18, bold: true, fontFace: THEME.headFontFace, color: C.text2, align: "center" });
  txt(s, "flow_desc" + i, f[2], { x: x + 0.1, y: 2.9, w: 1.46, h: 1.0, fontSize: 14, align: "center" });
});
s.addNotes("全体の流れ。質問は1つずつゆっくり聴いていく。");

s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "はじめに" });
s.addText("今日、大切にしたいこと", { placeholder: "title" });
txt(s, "care_lead", "無理に変わろうとしなくて大丈夫", { x: 0.5, y: 1.2, w: 9.0, h: 0.45, fontSize: 16, color: C.text1, margin: 0 });
[["選べます", "話す・話さない・休む", T.accent4], ["正解はありません", "感じ方は人それぞれ", T.accent6], ["今日の目標", "一つ気づいて、\n一つ持ち帰る", T.accent5]].forEach((c, i) => {
  const x = 0.5 + i * 3.08;
  card(s, "care_card" + i, x, 1.9, 2.84, 2.3, c[2]);
  txt(s, "care_head" + i, c[0], { x: x + 0.2, y: 2.1, w: 2.45, h: 0.45, fontSize: 19, bold: true, color: C.accent2 });
  txt(s, "care_body" + i, c[1], { x: x + 0.2, y: 2.7, w: 2.45, h: 1.2, fontSize: 16, color: C.text1 });
});
s.addNotes("はじめに安心を渡す。今日の目標は「一つ気づいて、一つ持ち帰る」。最後の「最初の一歩」が持ち帰るものになる。");

// =========== 第1部：聴く（1問ずつ） ===========
const S2 = "第1部 魂の傷を聴く";
pres.addSection({ title: S2 });
s = pres.addSlide({ masterName: "DIVIDER", sectionTitle: S2 });
s.addText("第1部　魂の傷を聴く", { placeholder: "title" });
s.addText("直感でおしえてください（0〜25分）\n答えたくない質問は、飛ばして大丈夫です", { placeholder: "body" });
s.addNotes("ここから25分。1問ずつ、ゆっくり聴く。");
const L1 = "どのような事でお悩みですか？";
question(S2, L1, "胸の奥の痛みについて、\nおしえてください", "直感で大丈夫です", "本人の言葉で。どこが・どんなふうに痛むか（ぎゅっと・ずきっと・重い等）。");
question(S2, L1, "それは、いつからですか？", "どのくらいの期間、続いていますか？", "");
question(S2, L1, "どんな時に、\n痛みが強くなりますか？", "誰といる時・何をしている時・何を思い出した時", "痛みが強くなる場面は、ワークの場面候補としてメモ。");
question(S2, L1, "その痛みに、\n色や形があるとしたら？", "何色ですか？　どんな形ですか？　重さはありますか？", "体の感じを言葉にしてもらう。最後のエネルギーの前後で比べられる。");
question(S2, L1, "1〜10で言うと、\n今の痛みはどのくらいですか？", "", "数字をメモしておく（最後の変化の確認に使う）。");
question(S2, L1, "ご自分でヒーリングしようとした時、\n何が起きましたか？", "今日は、ひとりで向き合わなくて大丈夫です", "痛すぎて自分ではできなかった、という今回のお申込みの理由。どこで止まったか・何が出てきたかを聴く。");
question(S2, L1, "その痛みは、あなたの人生に\nどのような影響がありますか？", "", "");
s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S2 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
txt(s, "qlabel", "ゴールデンエイジ", { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
s.addText("子どもの頃に\n見たこと・聞いたことが、\n今の「当たり前」になりやすい", { placeholder: "title" });
s.addText("この大切な時期を「ゴールデンエイジ」と呼びます", { placeholder: "body" });
s.addNotes("ここでは短く一言だけ。くわしくは第2部の「ゴールデンエイジ」のスライドで話す。");
question(S2, "幼少期のこと", "子ども時代のことも、\n聴かせていただいても\nいいですか？", "話したくないことは、話さなくて大丈夫です", "本人のOKをもらってから、幼少期の質問へ。");
const L2 = "問題の心理状況：幼少期の影響";
question(S2, L2, "どのような\nお子さんでしたか？", "", "");
question(S2, L2, "ご両親は、厳しかったですか？\n優しかったですか？", "", "胸がぎゅっとした場面・がまんした場面の話が出たら、ワークの場面候補としてメモ。");
question(S2, L2, "ご両親に、かけてほしかった\n言葉はありますか？", "", "ここは特にゆっくり。出てきた言葉はワークのSTEP4で使える。");
question(S2, "胸の痛みの、いちばん古い記憶", "胸の奥が、はじめて\nぎゅっと痛んだのは\nいつ頃ですか？", "誰かを責めるのではなく、当時のあなたの気持ちを大切にします", "その時、何を感じていたか。怖かった？悲しかった？怒り？寂しさ？と、気持ちに名前をつける手伝いをする。ここで出た場面がワークの第一候補。");

s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S2 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
txt(s, "qlabel", "第2部へ", { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
s.addText("お話を聴かせてくださって、\nありがとうございます", { placeholder: "title" });
s.addText("ここで少し、頭の仕組みのお話をさせてください", { placeholder: "body" });
s.addNotes("聴いたお話を受け取ってから、講座へ。講座の途中で、いま聴いた話（胸の痛みのいちばん古い記憶・子どもの頃の話）につなげて話す。");

// =========== 第2部：講座（物語） ===========
const S1 = "第2部 頭の構造を知る";
pres.addSection({ title: S1 });
s = pres.addSlide({ masterName: "DIVIDER", sectionTitle: S1 });
s.addText("第2部　頭の構造を知る", { placeholder: "title" });
s.addText("なぜ「わかっているのに」痛みが残るのか（25〜45分）", { placeholder: "body" });
s.addNotes("ここから20分。1枚ずつの説明ではなく、ひとつのお話としてつなげて話す。");

s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S1 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
txt(s, "qlabel", "第2部のはじめに", { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
s.addText("頭ではわかっているのに、\n胸の奥の痛みだけは、\nなかなか消えてくれない", { placeholder: "title" });
s.addText("その理由を、頭の仕組みからお話しします", { placeholder: "body" });
s.addNotes("物語の入り口。第1部で聴いた髙瀨さんの話を受けて「それはあなたのヒーリングの力が足りないからではなく、頭（脳）の仕組みだから」と伝えて、次へ。");

story(1, "人は「頭」ではなく「感情」で動いている", "yk2.jpg", 0.5625,
  "「もう大丈夫」と頭でわかっていても痛むのは、心が弱いからではありません。\n頭で考えるより先に、感情が体に出ているからです。",
  "感情がないと行動は起きない。理性はエネルギーを使う。理論は後付け。→だから、胸の痛みをほどくには、理屈ではなく感情に触れる必要がある。次は、その感情を動かしている脳の3つのクセ。");
s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S1 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
s.addText("ピンクの象", { placeholder: "title", fontSize: 54 });
s.addNotes("言葉だけを見せて、少し間を置く。「ピンクの象を想像しないでください」と言ってから次のスライドへ。");

story(2, "脳のクセ①　「〜しない」がわからない", "yk9.jpg", 0.5625,
  "「痛まないように」「思い出さないように」と思うほど、脳は痛む場面を思い描いてしまいます。",
  "ピンクの象を想像しないでください→想像してしまう。脳は否定語を受け付けない。新しいことを嫌い、変わらない言い訳を上手に作る。");
story(3, "脳のクセ②　過去の「強い思い」に引っ張られる", "yk14.jpg", 0.5625,
  "つらかった体験は「二度と触れるな」と保存されて、似た場面になると胸をぎゅっと縮めて、あなたを守ろうとします。",
  "強い出来事はトラウマ化して、タグ付きファイルとして保存される。脳は過去のマイナス体験を一般化して未来を予測する。→第1部で聴いた「胸の痛みのいちばん古い記憶」・子どもの頃の話は、ここにつながる。痛みは敵ではなく、守ろうとしてきたもの。では、その強い思いはいつ刻まれるのか？");

// 5：ゴールデンエイジ
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S1 });
label(s, `第2部　頭の構造を知る ｜ 4 / ${STORY_TOTAL}`);
s.addText("その「強い思い」が刻まれるのが、ゴールデンエイジ", { placeholder: "title" });
const ga = [
  ["子どもの頃", "家の中で見たこと・聞いた言葉・言われ方"],
  ["脳が保存", "「これが当たり前」として記憶する"],
  ["大人になった今", "その当たり前が、自分の基準として動き続ける"],
];
ga.forEach((g, i) => {
  const y = 1.35 + i * 1.08;
  card(s, "ga_card" + i, 0.5, y, 5.6, 0.9, i === 2 ? T.accent6 : T.lt2);
  circleNum(s, "ga" + i, i + 1, 0.68, y + 0.24);
  txt(s, "ga_head" + i, g[0], { x: 1.25, y: y + 0.07, w: 4.7, h: 0.38, fontSize: 16, bold: true, color: C.text2 });
  txt(s, "ga_body" + i, g[1], { x: 1.25, y: y + 0.45, w: 4.7, h: 0.4, fontSize: 14 });
});
card(s, "money_card", 6.35, 1.35, 3.15, 3.06, T.accent6);
txt(s, "money_head", "胸の痛みで言うと…", { x: 6.55, y: 1.5, w: 2.8, h: 0.4, fontSize: 15, bold: true, color: C.accent2 });
txt(s, "money_body", "子どもの頃、胸がぎゅっとした場面で覚えた「こうしなきゃ」が、今も胸の奥で続いています。", { x: 6.55, y: 1.95, w: 2.8, h: 2.3, fontSize: 14 });
s.addNotes("第1部で少し話したゴールデンエイジの、くわしい話。言われ方・見てきたことが、そのまま今の基準になっている。由香さんの言葉で補足する。");

story(5, "でも、その「当たり前」は人によって全然ちがう", "yk19.jpg", 0.5625,
  "痛みを抱えたまま「これが当たり前」と思ってきたことも、あなたの育った場所で作られたもの。\n作られたものだから、書き換えられます。",
  "メロンちょっと食べた→この人の「ちょっと」はどのくらい？　普通＝当たり前は人それぞれ。みんなの当たり前は同じではない。");
story(6, "ポジティブとは「入れ替えられる」こと", "yk22.jpg", 0.5625,
  "痛みを無理に「もう平気」と思い込むことではありません。\n古い受け取り方を、新しい受け取り方に入れ替えられる状態のことです。",
  "ネガティブ＝情報の入れ替えができない、自分の正しさに固執する。ポジティブ＝入れ替えができる、他の正しさを認められる。");
// 7：感情とエネルギー値（ホーキンズ『パワーか、フォースか』の意識のマップをもとに作図）
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S1 });
label(s, `第2部　頭の構造を知る ｜ 7 / ${STORY_TOTAL}`);
s.addText("感情には「エネルギーの高さ」がある", { placeholder: "title" });
const levels = [
  ["700〜1000", "悟り", "言語に絶する"], ["600", "平和", "至福"], ["540", "喜び", "静穏"],
  ["500", "愛", "尊敬"], ["400", "理性", "理解"], ["350", "受容", "許し"],
  ["310", "意欲", "楽観"], ["250", "中立", "信頼"], ["200", "勇気", "肯定"],
  ["175", "プライド", "嘲笑"], ["150", "怒り", "憎しみ"], ["125", "欲望", "切望"],
  ["100", "恐怖", "不安"], ["75", "深い悲しみ", "後悔"], ["50", "無気力", "絶望"],
  ["30", "罪悪感", "非難"], ["20", "恥", "屈辱"],
];
const lvFill = (v) => v >= 600 ? "F0CC6A" : v >= 400 ? "F3D98B" : v >= 200 ? "F8EBC8" : "EEF0F5";
const LX = 0.5, LW = 5.6, LY = 1.42, RH = 0.21;
const colX = [LX, LX + 1.15, LX + 2.85], colW = [1.15, 1.7, 1.5];
[["エネルギー値", 0], ["意識のレベル", 1], ["感情", 2]].forEach(([t, c]) =>
  txt(s, "lv_head" + c, t, { x: colX[c], y: 1.2, w: colW[c], h: 0.22, fontSize: 9, bold: true, color: C.accent2, align: "center", valign: "middle", margin: 0 }));
levels.forEach((lv, i) => {
  const y = LY + i * RH, v = parseInt(lv[0]);
  s.addShape(pres.shapes.RECTANGLE, { objectName: "lv_row" + i, x: LX, y, w: LW, h: RH, fill: { color: lvFill(v) }, line: { color: T.lt1, width: 0.75 } });
  lv.forEach((t, c) => txt(s, `lv_${i}_${c}`, t, { x: colX[c], y, w: colW[c], h: RH, fontSize: 10, bold: c === 1, color: C.text2, align: "center", valign: "middle", margin: 0 }));
});
// 200（勇気）と175（プライド）の間：パワーとフォースの境目
const by = LY + 9 * RH;
s.addShape(pres.shapes.LINE, { objectName: "lv_border", x: LX, y: by, w: LW, h: 0, line: { color: T.accent2, width: 2, dashType: "dash" } });
txt(s, "lv_power", "▲ パワー（生かす力）", { x: LX + LW - 1.9, y: by - 0.22, w: 1.85, h: 0.2, fontSize: 8, bold: true, color: C.accent2, align: "right", valign: "middle", margin: 0 });
txt(s, "lv_force", "▼ フォース（押す力）", { x: LX + LW - 1.9, y: by + 0.01, w: 1.85, h: 0.2, fontSize: 8, bold: true, color: C.accent2, align: "right", valign: "middle", margin: 0 });
card(s, "money_card", 6.35, 1.2, 3.15, 3.78, T.accent6);
txt(s, "money_head", "胸の痛みで言うと…", { x: 6.55, y: 1.32, w: 2.8, h: 0.4, fontSize: 15, bold: true, color: C.accent2 });
txt(s, "money_body", "胸の奥にしまってきた感情にも、エネルギーの高さがあります。\n出てきた感情を否定せずに感じ切ると、統合されて、上へ上がっていきます。\n怒りや悲しみが出ても大丈夫。\nほどけはじめているサインです。", { x: 6.55, y: 1.75, w: 2.8, h: 2.75, fontSize: 13, paraSpaceAfter: 6 });
txt(s, "lv_src", "D.R.ホーキンズ『パワーか、フォースか』の意識のマップをもとに作成", { x: 6.5, y: 4.5, w: 2.9, h: 0.4, fontSize: 8, color: C.accent1 });
s.addNotes("ホーキンズ博士の意識のマップ。200（勇気）より下は人から奪う・押す力（フォース）、上は生かす力（パワー）。恥20・罪悪感30・無気力50・深い悲しみ75・恐怖100は、エネルギーがとても低い。胸の奥にしまってきた感情がこのあたりにあると、自分ではヒーリングしようにも痛すぎて触れられない。出てきた感情を否定せず、順番に感じ切って統合していくと、上へ上がっていく。怒り150は悲しみ75より上＝怒りが出てきたら上がってきたサイン。「だから、今から感情を統合するワークをしましょう」とワークへ。無理にポジティブに変えない（ポジ変禁止）。");


// =========== ワーク ===========
const S3 = "ワーク 思い込みを書き換える";
pres.addSection({ title: S3 });
s = pres.addSlide({ masterName: "DIVIDER", sectionTitle: S3 });
s.addText("ワーク　思い込みを書き換える", { placeholder: "title" });
s.addText("思い込みが生まれた場面に戻って、書き換えていきます（45〜95分）", { placeholder: "body" });
s.addNotes("アートシフトワーク その18（エフィカシーを上げる5次元タイムライン）。画面では「5次元」「VAK」「ポジション」の言葉は使わない。ここから50分（120分版なので、和解と許し・理想の未来も入れている）。思い込みは20個ではなく、1階層目5つ＋2階層目まで（10個くらい）にしぼる。書き込みは由香が画面の表に打ち込む。");

s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S3 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
txt(s, "qlabel", "ワークの前に", { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
txt(s, "pre_main", "今回、一番大きいと感じる思い込みに\n向き合っていきます", { x: 0.8, y: 1.2, w: 8.4, h: 1.4, fontFace: THEME.headFontFace, fontSize: 28, bold: true, color: C.text2, align: "center", valign: "middle" });
txt(s, "pre_sub", "ただ、それが整理されると、次の思い込みや感情に気づくこともあります。\nだからこそ、一度で終わりではなく、\n自分自身で繰り返し向き合っていくことが大切です。", { x: 0.8, y: 2.85, w: 8.4, h: 1.5, fontSize: 16, color: C.text1, align: "center", valign: "top", lineSpacingMultiple: 1.3 });
s.addNotes("ワークに入る前に伝える。今日で全部終わらせようとしなくていい、というメッセージ。");

facil(S3, "STEP 1〜2 の進め方", [
  "穴埋め「胸の奥の痛みは、＿」「この痛みがなくなったら、私は＿」→本人の言葉を打ち込む",
  "「その言葉は、守っている？選択を狭めている？」",
  "すごい質問「何があなたをそう思わせるのですか？」（見える・色・聞こえる・体の感じ）",
  "1階層目を5つ以上 → 表に打ち込み、100点満点で点数",
  "1階層目で一番強いものを軸に、2階層目も同じ質問で（全部で10個くらい）",
  "点数がわからない時はOリング・筋肉反射",
], "gb12.jpg");

// STEP1 穴埋め
s = pres.addSlide({ masterName: "QUESTION", sectionTitle: S3 });
s.addShape(pres.shapes.RECTANGLE, { objectName: "frame", x: 0.25, y: 0.15, w: 9.5, h: 4.95, fill: { type: "none" }, line: { color: T.accent1, width: 1 } });
txt(s, "qlabel", "STEP 1　胸の痛みの奥にある思い込みを言葉にする", { x: 0.5, y: 0.35, w: 9.0, h: 0.4, fontSize: 13, bold: true, color: C.accent2, align: "center", margin: 0 });
txt(s, "fill1", "「胸の奥の痛みは、＿＿＿＿＿＿」", { x: 0.8, y: 1.3, w: 8.4, h: 0.9, fontFace: THEME.headFontFace, fontSize: 30, bold: true, color: C.text2, align: "center", valign: "middle" });
txt(s, "fill2", "「この痛みがなくなったら、私は＿＿＿＿」", { x: 0.8, y: 2.3, w: 8.4, h: 0.9, fontFace: THEME.headFontFace, fontSize: 30, bold: true, color: C.text2, align: "center", valign: "middle" });
txt(s, "fill_hint", "正解を探さず、浮かんだ言葉をそのまま", { x: 0.8, y: 3.5, w: 8.4, h: 0.5, fontSize: 15, color: C.accent2, align: "center" });
s.addNotes("由香が＿＿の所に本人の言葉を打ち込む。ここで出た言葉が、思い込みの入口（ガイドブックの「私は〇〇を達成したい！ただ…」の代わり）。2つ目で「痛みがあるから守られていること・やらずに済んでいること」が出ることがある。責めずにそのまま受け取る。");

question(S3, "STEP 1", "その言葉は、今のあなたを\n守っていますか？\nそれとも、選択を狭めていますか？", "", "どちらでもOK。守ってくれていたなら、まずそれを認めてから次へ。");

question(S3, "STEP 1　すごい質問", "何があなたを\nそう思わせるのですか？", "何が見えますか？　どんな色ですか？\n何が聞こえますか？　体はどんな感じがしますか？", "1階層目を5つ以上。出てきたものは次の表に打ち込む。");

// STEP2 表
s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S3 });
s.addText("STEP 2　思い込みに点数をつける（100点満点）", { placeholder: "title" });
const hdr = { bold: true, color: T.lt1, fill: { color: T.accent1 }, align: "center", valign: "middle", fontSize: 13 };
const rows = [[{ text: "No.", options: hdr }, { text: "思い込み（気持ちや想い）", options: hdr }, { text: "点数", options: hdr }]];
for (let i = 1; i <= 10; i++) rows.push([{ text: String(i), options: { align: "center" } }, { text: "" }, { text: "／100", options: { align: "right", color: T.accent1 } }]);
s.addTable(rows, { x: 0.5, y: 1.3, w: 5.8, colW: [0.6, 4.1, 1.1], rowH: 0.33, fontSize: 13, color: T.dk1, border: { type: "solid", pt: 0.75, color: T.accent3 }, fill: { color: T.lt1 } });
card(s, "s2_note", 6.6, 1.3, 2.9, 3.63, T.lt2);
txt(s, "s2_note_t", [
  { text: "思いつくまま、いくつでも", options: { bold: true, color: C.accent2, breakLine: true } },
  { text: "点数は、直感で大丈夫です", options: { breakLine: true } },
  { text: "正解・不正解はありません", options: {} },
], { x: 6.75, y: 1.42, w: 2.6, h: 3.4, fontSize: 14, paraSpaceAfter: 10 });
s.addNotes("由香が画面共有したまま表に打ち込む。髙瀨さんは話すだけでOK。10個くらい出たら次へ。1階層目で一番強いものを軸に、2階層目も同じ質問で出す。点数がわからない時はOリング・筋肉反射で。例：私ががまんすれば丸くおさまる80点／人に頼ってはいけない70点。");

facil(S3, "STEP 3〜4 の進め方", [
  "上位3つに印 → 一番邪魔している思い込みを1つ（Oリング可）",
  "確認「ゆるんだら、よい影響が出そう？」",
  "思い込みが生まれた場面へ（見える・色・聞こえる・体の感じ）",
  "外から見る「本当はどうして欲しかった？」「本当はどうしたかった？」",
  "和解と許し「相手の考え方は、いつできた？」「相手は本当はどうしたかった？」（無理に許さなくてよい）",
  "痛みがほどけた未来のあなた（見える・色・聞こえる・体の感じ）→「どんなあなたですか？」",
  "未来のあなたから「あの時のあなたへ、＿」→「伝えてみて、どんな気持ち？」",
  "「これから自分にかけたい言葉」を本人の言葉で（由香が打ち込む）",
], "gb13.jpg");
question(S3, "STEP 3", "一番、邪魔している思い込みは\nどれですか？", "点数の高い上位3つの中から、1つ選びます", "表の上位3つに印をつける→その中で一番邪魔しているものを1つ。判断できない時はOリング・筋肉反射で。");
question(S3, "STEP 3　確認の質問", "その思いが“ゆるんだら”、\nあなたの毎日によい影響が\n出そうですか？", "", "YESなら、その思い込みでSTEP4へ。");

question(S3, "STEP 4", "その思い込みが生まれた場面に\n戻ってみましょう", "何が見えますか？　どんな色ですか？\n何が聞こえますか？　体はどんな感じがしますか？\n苦しくなったら、いったん止めて、息を吐き切りましょう", "手順：①今の自分の場所に立ち、今の気持ちを話す ②思い込みが生まれた過去の場面へ移動し、見える・色・聞こえる・体の感じで話す ③その場所から出て、自分を外から見る→次の2つの質問 ④もう一度その場所に戻り、全部吐き出す。VAKという言葉は使わない。第1部の「胸の痛みのいちばん古い記憶」の場面が出やすい。感情が強く出たら止めて呼吸に戻す。胸の痛みが強くなったら、いったん止めて息を吐き切る。ポジ変をしない。");
question(S3, "STEP 4　外から見ながら", "本当は、\nどうして欲しかったの？", "「満たされていない想い」を、言葉にしていきます", "ポジションの外から、子どもの頃の自分を見ながら。");
question(S3, "STEP 4　外から見ながら", "本当は、\nどうしたかったの？", "相手の中にも入ってみる？", "");
question(S3, "STEP 4　和解と許し", "その相手の考え方は、\nいつ、どうやって\nできたのでしょう？", "相手にも、相手の子ども時代があります", "相手の信念・価値観はいつできたか。無理に許さなくていい。相手を理解すると、自分の胸がゆるむことがある。仁部さん版（90分）では外したもの。");
question(S3, "STEP 4　和解と許し", "相手は本当は、\nどうしたかったのでしょう？", "", "相手の中に入ったまま、または外から見ながら。出てきた言葉をそのまま受け取る。");
question(S3, "STEP 4　未来のあなた", "胸の痛みがほどけた\n未来のあなたを\n思い浮かべてください", "何が見えますか？　どんな色ですか？\n何が聞こえますか？　体はどんな感じがしますか？", "仁部さん版で外した「理想の未来」。5次元という言葉は使わない。特に胸のあたりの感じを聞く（軽い・あたたかい・広い等）。");
question(S3, "STEP 4　未来のあなた", "その未来のあなたは、\nどんなあなたですか？", "どんな毎日を過ごしていますか？", "見える・色・聞こえる・体の感じで、未来の自分をはっきりさせる。その未来のあなたから、次のスライドで「あの時のあなた」に言葉をかける。");
question(S3, "STEP 4　未来のあなたから", "あの時のあなたへ、\n＿＿＿＿＿＿＿＿","伝えてみて、どんな気持ちですか？", "＿＿に本人の言葉を打ち込む。言いたかったことを全部吐き出す（100％出たか？）。怒鳴る・泣く・大声を出す・体を大きく動かす・殴るなどしてOK。相手が聞いてくれている・謝っているイメージで。出し切るまで待つ。");


s = pres.addSlide({ masterName: "CONTENT", sectionTitle: S3 });
s.addText("これから選びたい、自分への言葉", { placeholder: "title" });
card(s, "old_card", 0.5, 1.4, 4.35, 2.7, T.lt2);
txt(s, "old_head", "今まで自分にかけてきた言葉", { x: 0.7, y: 1.55, w: 4.0, h: 0.4, fontSize: 16, bold: true, color: C.accent2 });
txt(s, "old_body", "", { x: 0.7, y: 2.05, w: 4.0, h: 1.9, fontSize: 18, fontFace: THEME.headFontFace });
card(s, "new_card", 5.15, 1.4, 4.35, 2.7, T.accent6);
txt(s, "new_head", "これから自分にかけたい言葉", { x: 5.35, y: 1.55, w: 4.0, h: 0.4, fontSize: 16, bold: true, color: C.accent2 });
txt(s, "new_body", "", { x: 5.35, y: 2.05, w: 4.0, h: 1.9, fontSize: 18, fontFace: THEME.headFontFace });
txt(s, "new_note", "無理にポジティブな言葉にせず、自分が納得できる言葉で", { x: 0.5, y: 4.3, w: 9.0, h: 0.45, fontSize: 14, color: C.text1 });
s.addNotes("由香が本人の言葉をそのまま打ち込む。言葉は本人が決める（由香が作らない）。");

// =========== エネルギー ===========
const S4 = "エネルギー";
pres.addSection({ title: S4 });
s = pres.addSlide({ masterName: "DIVIDER", sectionTitle: S4 });
s.addText("エネルギーで取り除く", { placeholder: "title" });
s.addText("残っている痛みを、やさしく手放していきます（95〜110分）\nはじめる前に、今の気持ちと胸の感じを確かめます。終わったら、感じたことを言葉にしてみましょう", { placeholder: "body" });
s.addNotes("ワークで残ったものをエネルギーで取り除く。ご自身では痛すぎてできなかった所なので、120分版ではここを15分とる。前後で胸の痛み（1〜10・色・形・重さ）を確かめる。");

// =========== まとめ ===========
const S5 = "まとめ";
pres.addSection({ title: S5 });
question(S5, "ふり返り", "最初に「1〜10」で聞いた\n胸の痛みは、\nいまどのくらいですか？", "はじめ：＿＿　→　いま：＿＿", "第1部の「1〜10で言うと、今の痛みはどのくらいですか？」で聞いた数字と比べる。色や形・重さの変化も聞く。由香が＿＿に打ち込む。");

question(S5, "ふり返り", "今日、いちばん\n変わったと感じることは\n何ですか？", "それが、今日持ち帰るものです", "本人の言葉で言ってもらう。");

question(S5, "これから", "次に同じ感情が出てきたら、\n自分にどんな言葉を\nかけてあげたいですか？", "気づいたら、責めずに見つめる。そして、今の自分で選び直す", "「一度で終わりではなく、繰り返し向き合う」につなげる。");

s = pres.addSlide({ masterName: "TITLE", sectionTitle: S5 });
txt(s, "magic_main", "根深いものは、\n何度も何度も\n自分に魔法をかけて、とっていく", { x: 0.6, y: 1.1, w: 8.8, h: 2.3, fontFace: THEME.headFontFace, fontSize: 34, bold: true, color: C.text2, align: "center", valign: "middle" });
txt(s, "magic_sub", "あなたが自分にかける言葉が、魔法になります", { x: 0.8, y: 3.55, w: 8.4, h: 0.6, fontSize: 18, bold: true, color: C.text2, align: "center", valign: "middle" });
s.addNotes("由香さんの言葉。一度で外れなくても失敗ではなく、ほどいている途中だと伝える。");

s = pres.addSlide({ masterName: "IMAGE", sectionTitle: S5 });
s.addImage({ path: IMG + "mc13_gold.jpg", x: 0, y: (5.625 - 10 * 893 / 1600) / 2, w: 10, h: 10 * 893 / 1600, altText: "絶対的安心感" });
s.addNotes("すべての土台は絶対的安心感。「何をやっても、やらなくても大丈夫」「嫌なことをやめても、愛される」。");

s = pres.addSlide({ masterName: "TITLE", sectionTitle: S5 });
s.addImage({ path: IMG + "logo.png", x: 4.45, y: 0.45, w: 1.1, h: 1.065, altText: "海音ロゴ" });
s.addText("ありがとうございました", { placeholder: "title" });
s.addText("1週間後に、LINEでその後のご様子をお伺いします\n海音（かのん）〜心体の調律〜　髙橋 由香", { placeholder: "body" });
s.addNotes("終了。1週間後にLINEで「その後いかがですか？」と連絡する。");

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote " + OUT);
})();
