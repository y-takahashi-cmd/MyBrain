from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

for section in doc.sections:
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fr = fp.add_run('海音〜心体の調律〜　髙橋由香')
    fr.font.size = Pt(9)

def set_cell_bg(cell, color_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tcPr.append(shd)

def style_cell(cell, bold=False, size=10, bg=None):
    if bg:
        set_cell_bg(cell, bg)
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.size = Pt(size)
            run.font.bold = bold

# タイトル（左寄せ）
p = doc.add_paragraph()
r = p.add_run('企業のオンライン保健室　月次報告書')
r.font.size = Pt(14)
r.font.bold = True

doc.add_paragraph()

# ヘッダー表（3行4列）
t = doc.add_table(rows=3, cols=4)
t.style = 'Table Grid'

# 行0: 会社名 | 株式会社サステナ　様（3列マージ）
c = t.rows[0].cells
c[0].text = '会社名'
c[1].text = '株式会社サステナ　様'
c[1].merge(c[3])
style_cell(c[0], bold=True, bg='D9E1F2')
style_cell(c[1])

# 行1: 報告年月日 | 日付 | 対象月 | 月
c1 = t.rows[1].cells
c1[0].text = '報告年月日'
c1[1].text = '2026年4月27日'
c1[2].text = '対象月'
c1[3].text = '2026年4月'
style_cell(c1[0], bold=True, bg='D9E1F2')
style_cell(c1[1])
style_cell(c1[2], bold=True, bg='D9E1F2')
style_cell(c1[3])

# 行2: 報告者 | 名前 | 月テーマ | テーマ
c2 = t.rows[2].cells
c2[0].text = '報告者'
c2[1].text = '髙橋　由香'
c2[2].text = '月テーマ'
c2[3].text = '全員との接点が整い、いよいよ本格的なスタート'
style_cell(c2[0], bold=True, bg='D9E1F2')
style_cell(c2[1])
style_cell(c2[2], bold=True, bg='D9E1F2')
style_cell(c2[3])

doc.add_paragraph()

# 【総評】
h1 = doc.add_paragraph()
r1 = h1.add_run('【総評】')
r1.font.bold = True
r1.font.size = Pt(10)

souhy = doc.add_paragraph(
    '4月は、樋田さん（第2・3回）・佐藤さん（第1・2回）・大森さん（第1・2回）と計6回のセッションを実施しました。'
    '三井康平さんについては問診票を受領し、書面にて結果をお伝えしました。\n'
    '4月でメンバー全員との接点が整いました。一人ひとりの「今」と「ありたい姿」を丁寧に受け取った一ヶ月です。\n'
    '各メンバーに共通して感じたのは、「本当はゆっくりしたい・疲れている」という声でした。'
    '言葉にはしていませんが、体がそのサインを出しています。'
    '特に佐藤さんへ「社員から信頼されている」という事実をお伝えした際、ご本人が少し驚かれていたことが印象的でした。'
)
souhy.runs[0].font.size = Pt(10)

doc.add_paragraph()

# 【個別セッションの状況】
h2 = doc.add_paragraph()
r2 = h2.add_run('【個別セッションの状況】')
r2.font.bold = True
r2.font.size = Pt(10)

data = [
    ['氏名', '受診日', '現状', '課題'],
    ['浅野 航さん', '次回\n5月予定',
     '3月に2回完了。心理状態96%と良好。睡眠リズム・下半身筋力が課題。',
     '・21時5分の下半身運動\n・健康宅配食（ナッシュ）を試す\n・10秒開口ストレッチ\n次回：5月頃'],
    ['樋田 雅史さん', '4/3\n4/24',
     '副腎・男性ホルモン50%・代謝35%・心理状態35%（要注意水準）。前回休職前と似た状況への不安あり。',
     '・退勤の儀式（着替え・一度外に出る）\n・ウインナーをやめる\n・寝る前に良いことを1つ思い浮かべる\n「前回と同じ状況になりそうなら会社に伝える」と決意\n次回：5/22（木）18:30〜'],
    ['佐藤 洋介さん', '4/10\n4/17',
     '心理状態88%・体調80%。血圧136/91（高血圧傾向）。毒素・代謝・副腎が要注意ライン超え。',
     '・「楽々やってまーす」と声に出す\n・寝る前の思考をポジティブに締める\n・旅・キャンプの予定を前もって立てる\n次回：6月頃'],
    ['大森 美葉さん', '4/13\n4/23',
     '体調80%・心理状態58%。栄養30%・毒素28%・副腎25%が要注意ライン超え。低用量ピル服用中。',
     '・マグネシウム・鉄＋ビタミンC・D補給\n・毎日5分「好きだったことを考える」\n・趣味（絵・色鉛筆・本）を生活に取り込む\n次回：6月頃'],
    ['三井 康平さん', '書面報告\nのみ',
     '心理状態61%は安定。男性ホルモン・副腎・甲状腺・代謝が要注意ライン超え。',
     '書面にて問診票結果をお伝え済み。\n5月以降、状況に応じて対応予定。'],
]

tbl = doc.add_table(rows=len(data), cols=4)
tbl.style = 'Table Grid'
col_widths = [Cm(3), Cm(2), Cm(5.5), Cm(7.5)]
for i, row in enumerate(tbl.rows):
    for j, cell in enumerate(row.cells):
        cell.text = data[i][j]
        cell.width = col_widths[j]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(9)
        if i == 0:
            set_cell_bg(cell, 'D9E1F2')
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True
                    run.font.size = Pt(10)

doc.add_paragraph()

# 【全体傾向と提言】
h3 = doc.add_paragraph()
r3 = h3.add_run('【全体傾向と提言】')
r3.font.bold = True
r3.font.size = Pt(10)

teigen = doc.add_paragraph(
    'リモートワーク環境では仕事道具が常に目の前にあり、脳が仕事モードから抜け出せない状態が続きやすい傾向があります。'
    '樋田さん・大森さんに共通して「ゆっくりしたい」「休みたい」という声があり、体が静かに疲弊しているサインと受け止めています。\n\n'
    '① 樋田さんは心身の数値が要注意水準です。「前回と同じ状況になりそうなら会社に伝える」という本人の決意を支えながら、月1回フォローを継続します。\n'
    '② 浅野さん・大森さんは次回6月に向けて、習慣の定着状況を確認します。\n'
    '③ 三井さんとは5月以降、状況に応じて面談の機会を設けてまいります。'
)
teigen.runs[0].font.size = Pt(10)

doc.add_paragraph()

# 以上
p_end = doc.add_paragraph('以上')
p_end.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_end.runs[0].font.size = Pt(10)

output_path = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\株式会社サステナ\02_報告会記録\サステナ様_2026年4月_月次報告書.docx'
doc.save(output_path)
print(f'保存完了：{output_path}')
