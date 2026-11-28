r"""動物キャラ版の名札（名刺サイズ）。由香さん・次男カズキさん。2026-11-28作成。
個性心理學版と5アニマル版を別々のファイルで作る。
元データ：個性心理學カルテ（11/25・生まれた時刻あり）／5アニマル無料版スクショ（11/28）。
"""
from pptx import Presentation
from pptx.util import Cm
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from nafuda_core import _box, _text, NAVY, GRAY, LIGHT, WHITE

DIR = r"C:\Users\y-takahashi\MyBrain\20_Projects\クライアント_髙橋由香"
OUT_KOSEI = DIR + r"\動物キャラ名札_個性心理學版_由香・カズキ_v0.1.pptx"
OUT_5 = DIR + r"\動物キャラ名札_5アニマル版_由香・カズキ_v0.1.pptx"

# グループの色（個性心理學カルテの色に合わせる）
GROUP = {
    "地球": (RGBColor(0x5B, 0xB8, 0xE6), WHITE),
    "太陽": (RGBColor(0xD9, 0x3B, 0x3B), WHITE),
    "月": (RGBColor(0xF5, 0xC5, 0x18), NAVY),
}
ANIMAL_GROUP = {"子守熊": "地球", "虎": "地球", "猿": "地球", "狼": "地球",
                "ペガサス": "太陽", "ライオン": "太陽", "チータ": "太陽", "ゾウ": "太陽",
                "こじか": "月", "ひつじ": "月", "たぬき": "月", "黒ひょう": "月"}

PEOPLE_KOSEI = [
    dict(name="髙橋 由香", honshitsu="子守熊", sub="夢とロマンの子守熊",
         others=[("表面", "こじか"), ("意志", "ライオン"), ("希望", "ライオン")],
         kodo=0, vector=0,
         info="右脳型　リズム：海洋　レール：リアリティ　2026年＝投資・2027年＝成果",
         hitokoto="先にゴールと予定を教えてもらえると、安心して力が出ます。\n感じたことを言葉にするのが得意です。"),
    dict(name="カズキ", honshitsu="ペガサス", sub="落ち着きのあるペガサス",
         others=[("表面", "ひつじ"), ("意志", "ひつじ"), ("希望", "こじか")],
         kodo=1, vector=1,
         info="右脳型　リズム：大樹　レール：ロマン　2026年＝調整・2027年＝焦燥",
         hitokoto="ゴールだけ一言で伝えてもらえると、一番のびます。\nやり方は任せてもらえると、ひらめきが動き出します。"),
]

PEOPLE_5 = [
    dict(name="髙橋 由香", honshitsu="子守熊", sub="本質＝基本の性格",
         others=[("表面", "こじか"), ("意思決定", "ライオン"), ("希望", "こじか"), ("隠れ", "こじか")],
         hitokoto="決めるときは、ライオンのようにきっぱり。\n本当の力の元は、安心して信頼し合える関係です。"),
    dict(name="カズキ", honshitsu="ペガサス", sub="本質＝基本の性格",
         others=[("表面", "ひつじ"), ("意思決定", "ひつじ"), ("希望", "虎"), ("隠れ", "たぬき")],
         hitokoto="みんなの和を大事にして決めます。\n心の奥には「自分のやり方で生きたい」想いがあります。"),
]


def _switch(s, x, y, w, label, left, right, side, col):
    _text(s, x, y, w, 0.3, label, size=5.5, bold=True, color=GRAY)
    half = w / 2
    for i, t in enumerate((left, right)):
        on = i == side
        _box(s, x + i * half, y + 0.33, half - 0.05, 0.42, fill=col if on else LIGHT,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        _text(s, x + i * half, y + 0.33, half - 0.05, 0.42, t + ("型 ★" if on else "型"), size=6 if on else 5.5,
              bold=on, color=WHITE if on else GRAY, align=PP_ALIGN.CENTER)


def front(prs, p, header):
    g = ANIMAL_GROUP[p["honshitsu"]]
    band, ink = GROUP[g]
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, 9.1, 5.5, fill=WHITE)
    _box(s, 0, 0, 9.1, 1.45, fill=band)
    _text(s, 0.35, 0.1, 6, 0.3, header, size=5.5, color=ink)
    _text(s, 0.35, 0.38, 5.2, 0.7, p["name"], size=16, bold=True, color=ink)
    _text(s, 0.35, 1.05, 5.0, 0.3, f"{g}グループ", size=5.5, color=ink)
    _box(s, 5.6, 0.2, 3.15, 1.05, fill=WHITE, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    _text(s, 5.6, 0.22, 3.15, 0.3, "本質", size=5, color=GRAY, align=PP_ALIGN.CENTER)
    _text(s, 5.6, 0.5, 3.15, 0.5, p["honshitsu"], size=14, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
    _text(s, 5.6, 0.95, 3.15, 0.25, p["sub"], size=5, color=GRAY, align=PP_ALIGN.CENTER)

    _text(s, 0.35, 1.55, 6, 0.3, "わたしの中にいる動物たち", size=5.5, bold=True, color=GRAY)
    n = len(p["others"])
    cw = (8.4 - 0.13 * (n - 1)) / n
    for i, (pos, animal) in enumerate(p["others"]):
        c, cink = GROUP[ANIMAL_GROUP[animal]]
        x = 0.35 + i * (cw + 0.13)
        _box(s, x, 1.88, cw, 0.85, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        _text(s, x, 1.92, cw, 0.28, pos, size=5, color=cink, align=PP_ALIGN.CENTER)
        _text(s, x, 2.2, cw, 0.45, animal, size=9, bold=True, color=cink, align=PP_ALIGN.CENTER)

    if "kodo" in p:
        _switch(s, 0.35, 2.85, 4.1, "動き方（行動パターン）", "目標指向", "状況対応", p["kodo"], band)
        _switch(s, 4.65, 2.85, 4.1, "考える向き（心理ベクトル）", "過去回想", "未来展望", p["vector"], band)
        _text(s, 0.35, 3.7, 8.4, 0.3, p["info"], size=5.5, bold=True, color=NAVY)
    else:
        groups = [g] + [ANIMAL_GROUP[a] for _, a in p["others"]]
        line = "　".join(f"{k}グループ×{groups.count(k)}" for k in ("月", "地球", "太陽") if groups.count(k))
        _text(s, 0.35, 3.0, 8.4, 0.35, "5つの内わけ：" + line, size=6.5, bold=True, color=NAVY)

    _box(s, 0.35, 4.05, 8.4, 1.2, fill=RGBColor(0xF4, 0xF4, 0xF4), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    _text(s, 0.55, 4.1, 1.5, 1.1, "わたしへの\nひとこと", size=5.5, bold=True, color=NAVY)
    _text(s, 2.0, 4.1, 6.6, 1.1, p["hitokoto"], size=6.5, bold=True, color=NAVY)


def back(prs, rows, source):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, 9.1, 5.5, fill=WHITE)
    _box(s, 0, 0, 9.1, 0.6, fill=NAVY)
    _text(s, 0.35, 0.05, 8.4, 0.5, "動物キャラ名札の見方", size=9, bold=True, color=WHITE)
    for i, (k, v) in enumerate(rows):
        y = 0.75 + i * 0.42
        _box(s, 0.35, y, 1.6, 0.36, fill=LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        _text(s, 0.35, y, 1.6, 0.36, k, size=6, bold=True, color=NAVY, align=PP_ALIGN.CENTER)
        _text(s, 2.1, y, 6.6, 0.36, v, size=6, color=NAVY)
    y = 2.95
    for i, (gname, desc) in enumerate([("月", "人との和・安心を大事にする"), ("地球", "自分のペース・中身を大事にする"),
                                         ("太陽", "ひらめき・勢いを大事にする")]):
        c, cink = GROUP[gname]
        x = 0.35 + i * 2.85
        _box(s, x, y, 0.8, 0.36, fill=c, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        _text(s, x, y, 0.8, 0.36, gname, size=6, bold=True, color=cink, align=PP_ALIGN.CENTER)
        _text(s, x + 0.9, y, 1.9, 0.36, desc, size=4.8, color=NAVY)
    _text(s, 0.35, 3.45, 8.4, 0.35, "元にしたもの：" + source, size=5, color=GRAY)
    _box(s, 0.35, 4.0, 8.4, 1.15, fill=RGBColor(0xEA, 0xF2, 0xFA), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    _text(s, 0.55, 4.05, 8.0, 1.05, "これは評価ではありません。関わり方のヒントです。\n「この人にはどう伝えるといいかな？」と思った時に見てください。",
          size=6.5, bold=True, color=NAVY)


def make(out, people, header, rows, source):
    prs = Presentation()
    prs.slide_width = Cm(9.1)
    prs.slide_height = Cm(5.5)
    for p in people:
        front(prs, p, header)
    back(prs, rows, source)
    prs.save(out)
    return out


if __name__ == "__main__":
    print(make(OUT_KOSEI, PEOPLE_KOSEI, "わたしの動物キャラ名札（個性心理學）",
               [("本質", "基本の性格"), ("表面", "人に見せている顔"), ("意志", "何かを決めるときに出てくる顔"),
                ("希望", "心の奥で願っていること"), ("動き方・向き", "目標指向／状況対応・過去回想／未来展望")],
               "個性心理學 個性診断カルテ（生まれた時刻まで入力）"))
    print(make(OUT_5, PEOPLE_5, "わたしの動物キャラ名札（5アニマル）",
               [("本質", "基本の性格"), ("表面", "人に見せている顔"), ("意思決定", "何かを決めるときに出てくる顔"),
                ("希望", "心の奥で願っていること"), ("隠れ", "自分でも気づきにくい一面")],
               "動物占い 5アニマル（無料版）"))
