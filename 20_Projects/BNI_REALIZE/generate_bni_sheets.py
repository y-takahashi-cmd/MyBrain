"""BNI REALIZEチャプター用：メンバー略歴シート + GAINSワークシート PDF生成"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# フォント登録
FONT_DIR = r"C:\Windows\Fonts"
try:
    pdfmetrics.registerFont(TTFont("Meiryo", os.path.join(FONT_DIR, "meiryo.ttc"), subfontIndex=0))
    pdfmetrics.registerFont(TTFont("MeiryoBold", os.path.join(FONT_DIR, "meiryob.ttc"), subfontIndex=0))
    R, B = "Meiryo", "MeiryoBold"
except Exception:
    try:
        pdfmetrics.registerFont(TTFont("NotoSans", os.path.join(FONT_DIR, "NotoSansJP-VF.ttf")))
        R = B = "NotoSans"
    except Exception:
        R, B = "Helvetica", "Helvetica-Bold"

NAVY   = HexColor("#1F3864")
BLUE   = HexColor("#4472C4")
GREY   = HexColor("#555555")
BORDER = HexColor("#AAAAAA")
W, H   = A4

OUT = r"C:\Users\y-takahashi\MyBrain\20_Projects\BNI_REALIZE"
os.makedirs(OUT, exist_ok=True)


def section_header(c, x, y, w, h, text):
    c.setFillColor(NAVY)
    c.rect(x, y, w, h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont(B, 10)
    c.drawString(x + 3*mm, y + 2*mm, text)


def hline(c, x, y, x2):
    c.setStrokeColor(black)
    c.setLineWidth(0.4)
    c.line(x, y, x2, y)


def border_box(c, x, y, w, h):
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.5)
    c.rect(x, y, w, h, fill=0, stroke=1)


def wrap_draw(c, text, x, y, max_w, font, size, color=black, leading=4.8*mm):
    c.setFont(font, size)
    c.setFillColor(color)
    line = ""
    lines = []
    for ch in text:
        if c.stringWidth(line + ch, font, size) > max_w:
            lines.append(line)
            line = ch
        else:
            line += ch
    if line:
        lines.append(line)
    for l in lines:
        c.drawString(x, y, l)
        y -= leading
    return y, len(lines)


def label_val_inline(c, cx, cy, label, val, label_font, val_font, size, label_color, val_color):
    """ラベル：値　をインラインで描画。値ありの場合は値を、なしの場合は空欄ライン"""
    c.setFont(label_font, size)
    c.setFillColor(label_color)
    c.drawString(cx, cy, label)
    lw = c.stringWidth(label, label_font, size)
    if val:
        c.setFont(val_font, size)
        c.setFillColor(val_color)
        c.drawString(cx + lw, cy, val)
        return cx + lw + c.stringWidth(val, val_font, size)
    else:
        return cx + lw


# ================================================================
# Sheet 1: メンバー略歴シート
# ================================================================
def create_member_sheet(path):
    c = canvas.Canvas(path, pagesize=A4)
    mx = 14*mm
    cw = W - 2*mx
    y = H - 14*mm
    ind = mx + 6*mm

    # タイトル
    c.setFont(B, 15)
    c.setFillColor(black)
    c.drawCentredString(W / 2, y, "メンバー略歴シート")
    y -= 10*mm

    # ── スピーカー / 日時 ──
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(mx, y, "スピーカー：")
    sw = c.stringWidth("スピーカー：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(mx + sw, y, "髙橋　由香")
    vw = c.stringWidth("髙橋　由香", B, 9)
    hline(c, mx + sw + vw + 1*mm, y - 1, mx + cw * 0.5)

    c.setFont(R, 9)
    c.setFillColor(GREY)
    day_x = mx + cw * 0.57
    c.drawString(day_x, y, "日時：")
    dw = c.stringWidth("日時：", R, 9)
    hline(c, day_x + dw + 1*mm, y - 1, mx + cw)
    y -= 6*mm

    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(mx, y, "所属チャプター：")
    chw = c.stringWidth("所属チャプター：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(mx + chw, y, "REALIZE")
    y -= 8*mm

    # ── セクション：ビジネスについて ──
    SH = 7*mm
    section_header(c, mx, y - SH, cw, SH, "ビジネスについて")
    y -= SH + 5*mm
    biz_top = y

    def row(cy, label, val):
        c.setFont(R, 9)
        c.setFillColor(GREY)
        c.drawRightString(ind + 26*mm, cy, label)
        lx = ind + 27*mm
        if val:
            c.setFont(B, 9)
            c.setFillColor(black)
            c.drawString(lx, cy, val)
        else:
            hline(c, lx, cy - 1, mx + cw)
        return cy - 7*mm

    y = row(y, "事業名：", "企業のオンライン保健室")
    y = row(y, "専門分野：", "海音式メソッド（予防医学 × NLP心理学 × コーチング × プロファイリング）")
    y = row(y, "所在地：", "東京都府中市本町1-9-41　坪井ビル3F")

    # 過去の職業 + 経験年数（同行）
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawRightString(ind + 26*mm, y, "過去に経験した職業：")
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(ind + 27*mm, y, "看護師")
    nen_x = mx + cw * 0.62
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(nen_x, y, "経験年数")
    nenw = c.stringWidth("経験年数", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(nen_x + nenw + 2*mm, y, "1年")
    y -= 5*mm

    border_box(c, mx, y, cw, biz_top - y)
    y -= 5*mm

    # ── セクション：個人的な情報 ──
    section_header(c, mx, y - SH, cw, SH, "個人的な情報")
    y -= SH + 5*mm
    pers_top = y

    # 家族について（値あり）
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(ind, y, "家族について：")
    fw = c.stringWidth("家族について：", R, 9)
    fx = ind + fw + 3*mm

    # 配偶者：専業主夫
    c.drawString(fx, y, "配偶者")
    spw = c.stringWidth("配偶者", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(fx + spw + 1*mm, y, "専業主夫")
    spouse_vw = c.stringWidth("専業主夫", B, 9)

    # その他家族：息子2人
    ofx = fx + spw + spouse_vw + 8*mm
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(ofx, y, "その他家族")
    ofw = c.stringWidth("その他家族", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(ofx + ofw + 1*mm, y, "息子2人")
    other_vw = c.stringWidth("息子2人", B, 9)

    # ペット：なし
    pfx = ofx + ofw + other_vw + 8*mm
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(pfx, y, "ペット")
    petw = c.stringWidth("ペット", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(pfx + petw + 1*mm, y, "なし")
    y -= 7*mm

    # 趣味：カラオケ・漫画・パチスロ・スピリチュアル
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(ind, y, "趣味：")
    tw = c.stringWidth("趣味：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(ind + tw, y, "カラオケ・漫画・パチスロ・スピリチュアル")
    y -= 7*mm

    # その他の関心事
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(ind, y, "その他の関心事：")
    okw = c.stringWidth("その他の関心事：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(ind + okw, y, "人の在り方の形成の仕方について")
    y -= 7*mm

    # 出身地 / 居住地 / 居住年数
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(ind, y, "出身地：")
    szw = c.stringWidth("出身地：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(ind + szw, y, "北海道札幌市")
    szv = c.stringWidth("北海道札幌市", B, 9)

    jyx = ind + szw + szv + 6*mm
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(jyx, y, "居住地：")
    jyw = c.stringWidth("居住地：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(jyx + jyw, y, "北海道札幌市東区北31条東7丁目")
    jyv = c.stringWidth("北海道札幌市東区北31条東7丁目", B, 9)

    nyx = jyx + jyw + jyv + 6*mm
    c.setFont(R, 9)
    c.setFillColor(GREY)
    c.drawString(nyx, y, "居住年数：")
    nyw = c.stringWidth("居住年数：", R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    c.drawString(nyx + nyw, y, "27年")
    y -= 5*mm

    border_box(c, mx, y, cw, pers_top - y)
    y -= 5*mm

    # ── セクション：その他 ──
    section_header(c, mx, y - SH, cw, SH, "その他")
    y -= SH + 6*mm
    other_top = y

    # 私の強い願望は
    c.setFont(R, 9)
    c.setFillColor(GREY)
    wl = "私の強い願望は："
    c.drawString(ind, y, wl)
    wlw = c.stringWidth(wl, R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    wv = "日本中の働く人が、心も体もイキイキと働き続けられる社会をつくる"
    c.drawString(ind + wlw + 1*mm, y, wv)
    wvw = c.stringWidth(wv, B, 9)
    c.setFont(R, 9)
    c.drawString(ind + wlw + wvw + 2*mm, y, "ことです。")
    y -= 9*mm

    # 誰も知らない私（6回死にかけ）
    c.setFont(R, 9)
    c.setFillColor(GREY)
    dl = "誰も知らない私：　実は、私は…"
    c.drawString(ind, y, dl)
    y -= 5.5*mm
    c.setFont(B, 8.5)
    c.setFillColor(black)
    dv = "過去に6回ほど死にかけています。だからこそ「体が資本」を誰より深く知っています。"
    y, _ = wrap_draw(c, dv, ind + 4*mm, y, cw - 8*mm, B, 8.5, black, 5*mm)
    y -= 4*mm

    # 私の成功の鍵は
    c.setFont(R, 9)
    c.setFillColor(GREY)
    kl = "私の成功の鍵は："
    c.drawString(ind, y, kl)
    klw = c.stringWidth(kl, R, 9)
    c.setFont(B, 9)
    c.setFillColor(black)
    kv = "医療現場の経験と、心理学・コーチングを統合した「人を丸ごと診る力」"
    c.drawString(ind + klw + 1*mm, y, kv)
    y -= 5*mm

    border_box(c, mx, y, cw, other_top - y)

    c.save()
    print(f"OK: {path}")


# ================================================================
# Sheet 2: GAINSワークシート（1ページ目のみ）
# ================================================================
def create_gains_sheet(path):
    c = canvas.Canvas(path, pagesize=A4)
    mx = 14*mm
    cw = W - 2*mx
    y = H - 14*mm

    # タイトル
    c.setFont(B, 15)
    c.setFillColor(black)
    c.drawCentredString(W / 2, y, "GAINS  ワークシート")
    y -= 12*mm

    LEFT_W  = cw * 0.45
    GAP     = 5*mm
    RIGHT_W = cw - LEFT_W - GAP
    RX      = mx + LEFT_W + GAP

    sections = [
        {
            "label": "Goals（目標）：",
            "desc": (
                "自分や大切な人のために達成したい、仕事上または個人的な目標。"
                "自分の目標を定めるとともに、他の人の目標を知る必要があります。"
                "信頼関係の構築には、目標達成を支援するのが一番です。"
            ),
            "box_label": "Goals",
            "value": (
                "社員の心身の問題を「出勤できなくなる前に」予防する。"
                "企業オンライン保健室を全国の中小企業に届け、"
                "健康経営を当たり前の文化にすること。"
                "海音式メソッドを習得した仲間と共に、"
                "日本中に保健室を届けるしくみをつくること。"
            ),
            "box_h": 27*mm,
        },
        {
            "label": "Accomplishments（実績）：",
            "desc": (
                "人は自分が誇りにしていることを話題にしたいと思うものです。"
                "相手が過去に達成した実績は、相手のことを知る上で重要な手掛"
                "かりになります。また、あなたの知識、スキル、経験、価値は、"
                "あなたの実績の中に凝縮されています。常に自分の実績を相手に"
                "伝えることができるようにしておきましょう。"
            ),
            "box_label": "Accomplishments",
            "value": (
                "・看護師として現場経験を積んだ後、予防医学・NLP心理学・"
                "プロファイリングを統合した独自の「海音式メソッド」を確立。"
                "・来られなくなった社員の回復支援に成功。"
                "・右腕社員の退職を防ぎ、残業削減と売上維持を同時実現。"
                "・現在4社に企業オンライン保健室を継続提供中。"
                "・産業カウンセラー・保健師への養成講座も実施中。"
            ),
            "box_h": 32*mm,
        },
        {
            "label": "Interests（興味）：",
            "desc": (
                "スポーツ、読書、音楽鑑賞などの関心ごとは、他の人とつながる"
                "きっかけになります。人は共通の興味を持つ人と過ごしたいと思"
                "うものです。相手と興味が一致していれば、人間関係の強化につ"
                "ながります。"
            ),
            "box_label": "Interests",
            "value": (
                "カラオケ・漫画・パチスロ・スピリチュアル・"
                "人の在り方の形成の仕方・予防医学・健康経営"
            ),
            "box_h": 20*mm,
        },
        {
            "label": "Networks（人脈）：",
            "desc": (
                "フォーマル、カジュアルの両方を含めいろいろなものが考えられ"
                "ます。あなたが関係を持っている組織や機関、企業や個人など。"
            ),
            "box_label": "Networks",
            "value": (
                "常勝会（全国360名超の実業家ネットワーク）、"
                "中小企業経営者、医療・福祉・産業保健の専門家コミュニティ、"
                "BNI REALIZEチャプター"
            ),
            "box_h": 22*mm,
        },
        {
            "label": "Skills（スキル）：",
            "desc": (
                "自分の人脈にいる人の才能や能力について理解を深めれば、必要"
                "なときに、適切かつ手ごろな商品・サービスを見つけたり、紹介"
                "したりしやすくなります。また、より多くの人があなたのスキル"
                "について知れば、それだけビジネスのチャンスを獲得しやすくな"
                "ります。"
            ),
            "box_label": "Skills",
            "value": (
                "予防医学 / 看護・医療知識 / NLP心理学 / プロファイリング"
                " / コーチング / 言葉治療カウンセリング。"
                "これらを統合した「海音式メソッド」で、社員の見えないサインを"
                "早期にキャッチし、離職・休職・パフォーマンス低下を未然に防ぐ。"
            ),
            "box_h": 30*mm,
        },
    ]

    for sec in sections:
        sec_top = y
        box_h   = sec["box_h"]

        # 左：ラベル
        c.setFont(B, 10)
        c.setFillColor(black)
        c.drawString(mx, sec_top, sec["label"])

        # 左：説明文
        desc_y = sec_top - 5.5*mm
        wrap_draw(c, sec["desc"], mx, desc_y, LEFT_W, R, 8, GREY, 4.2*mm)

        # 右：枠
        box_y = sec_top - box_h
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.rect(RX, box_y, RIGHT_W, box_h, fill=0, stroke=1)

        # 右：ボックスラベル（青）
        c.setFont(B, 9)
        c.setFillColor(BLUE)
        c.drawString(RX + 2*mm, sec_top - 5*mm, sec["box_label"])

        # 右：記入値
        wrap_draw(c, sec["value"], RX + 2*mm, sec_top - 10*mm, RIGHT_W - 4*mm, R, 8.5, black, 4.5*mm)

        y = box_y - 5*mm

    # フッターテキスト
    if y > 20*mm:
        c.setFont(R, 7.5)
        c.setFillColor(GREY)
        footer = (
            "人脈に加えたい相手をどれくらいよく知っていますか？場合によっては宿題が必要です。"
            "すでに知っている人とより時間を過ごし、その人のG.A.I.N.S.を知りましょう。"
            "あなたも相手に同じ情報を伝えてください。あなたのことをより知ってもらうことで、"
            "あなたの商品・サービス、知識やスキル、経験が役立つ機会が生じた際、"
            "すぐにあなたの名前が頭に浮かぶようになります。"
        )
        wrap_draw(c, footer, mx, y - 3*mm, cw, R, 7.5, GREY, 4*mm)

    c.save()
    print(f"OK: {path}")


if __name__ == "__main__":
    create_member_sheet(os.path.join(OUT, "BNI_メンバー略歴シート_髙橋由香.pdf"))
    create_gains_sheet(os.path.join(OUT, "BNI_GAINSワークシート_髙橋由香.pdf"))
    print("Done!")
