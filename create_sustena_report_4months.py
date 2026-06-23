
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

# ===== タイトル =====
p = doc.add_paragraph()
r = p.add_run('企業のオンライン保健室　月次報告書')
r.font.size = Pt(14)
r.font.bold = True

doc.add_paragraph()

# ===== ヘッダー表（3行4列）=====
t = doc.add_table(rows=3, cols=4)
t.style = 'Table Grid'

c0 = t.rows[0].cells
c0[0].text = '会社名'
c0[1].text = '株式会社サステナ　様'
c0[1].merge(c0[3])
style_cell(c0[0], bold=True, bg='D9E1F2')
style_cell(c0[1])

c1 = t.rows[1].cells
c1[0].text = '報告年月日'
c1[1].text = '2026年6月29日'
c1[2].text = '対象期間'
c1[3].text = '2026年3月〜6月（4ヶ月間）'
style_cell(c1[0], bold=True, bg='D9E1F2')
style_cell(c1[1])
style_cell(c1[2], bold=True, bg='D9E1F2')
style_cell(c1[3])

c2 = t.rows[2].cells
c2[0].text = '報告者'
c2[1].text = '髙橋　由香'
c2[2].text = 'テーマ'
c2[3].text = '4ヶ月モニター総括〜変化の記録と今後への提言'
style_cell(c2[0], bold=True, bg='D9E1F2')
style_cell(c2[1])
style_cell(c2[2], bold=True, bg='D9E1F2')
style_cell(c2[3])

doc.add_paragraph()

# ===== 【総評】=====
h1 = doc.add_paragraph()
r1 = h1.add_run('【総評】')
r1.font.bold = True
r1.font.size = Pt(10)

souhy = doc.add_paragraph(
    '　2026年3月から6月にかけての4ヶ月間、企業のオンライン保健室のモニター期間として、'
    '株式会社サステナの皆さまと個別セッションを重ねてまいりました。\n'
    '　この4ヶ月間で、浅野さん3回・樋田さん4回・佐藤さん3回・大森さん3回（6/29予定含む）・'
    '三井さん書面対応という形で、全員との接点を持つことができました。\n'
    '　全体を通じて感じたのは、「リモートワーク環境が心身の切り替えを難しくしている」という共通の課題です。'
    '仕事道具が常に目の前にある状況が、気づかないうちに体と心に負荷をかけていました。'
    '4ヶ月を経て、各メンバーがそれぞれのペースで確実に変化してきています。'
)
souhy.runs[0].font.size = Pt(10)

doc.add_paragraph()

# ===== 【個別セッションの状況】=====
h2 = doc.add_paragraph()
r2 = h2.add_run('【個別セッションの状況】')
r2.font.bold = True
r2.font.size = Pt(10)

data = [
    ['氏名', '実施日', '現状・変化', '課題・アクション'],
    ['浅野 航さん',
     '3/17・3/27\n5/22（計3回）',
     '心理状態96%と高水準を維持。\n「この1〜2年で自信がついてきた」と自己評価。\n現在の生活満足度70〜75%。\n「やることは今と同じ、仕事の内容と報酬が広がれば」という安定した状態。\n「上から目線に聞こえることがある」という自己気づきが生まれた。',
     '・違和感を感じた瞬間に「今の言い方、上から目線だったかも？」と自問する\n・お金（65点）・人間関係（60点）を伸ばすことを意識する\n\n【会社への提言】\n・「動かす側」としての役割を明確に言語化する\n・佐藤社長との定期対話の場を設ける（月1回1on1推奨）\n・半年〜1年のキャリアパスを本人に伝える'],
    ['樋田 雅史さん',
     '3月・4/3\n4/24・5/22\n（計4回）',
     '初回から継続して、笑顔の出方・エネルギーの質が変化（5/22に最も顕著）。\n卓球の教え子が県大会進出→朝2回自然に早起きができた。\n「熱中しても自分で切れる」という感覚が育ちつつある。\n仕事の構造的問題（断れない・期日固定）は継続課題。\n6月から新案件開始で「光が射した」感覚あり。',
     '・アラームのラベルを「何時まで寝ていいよ」に変える\n・寝る前の切り替えルーティン継続\n・手のマッサージ（縦縦縦横横・1分）\n\n【会社への提言】\n・「①順調に進んでいますか？　②できていることは？　③あと何をやれば？」の順で定期的に声をかける\n・業務を属人化させない仕組みの検討\n・再休職を防ぐためのアーリーサインを共有済み（本人と「同じ状況になりそうなら伝える」と約束）'],
    ['佐藤 洋介さん',
     '4/10・4/17\n6/19（計3回）',
     '体調良好・ストレス低を4ヶ月維持。\n睡眠改善傾向（夜中の覚醒が減少）。\n組織課題「ほうれんそうが届かない」の構造を言語化。\n「お客様の立場で考える」を行動指針として発見し、「武器ができた」と本人が表現。\n6/30に次回セッション予定。',
     '・「お客様の立場で考える」を会議・日常の合言葉として定着させる\n・社労士と連携中のアルバイト対応を継続\n\n【会社への提言】\n・「ほうれんそう」の評価基準を人事制度に明文化する\n・スタッフへの業務全体像（自分の仕事が全体のどこに位置するか）の共有\n・「お客様の立場で」という視座を社内標語化する'],
    ['大森 美葉さん',
     '4/13・4/23\n6/29（計3回予定）',
     '体調は安定（80%）。大きな不調なし。\n初回は覇気なし・感情を閉ざしている印象だったが、「好きなことを計画してやる」が自分に合っていると気づいた。\n「誠タイプ（世界・チームのためが原動力）」「No.2役割が得意」という自己理解が深まりつつある。\n6/29の第3回で変化を確認予定。',
     '・好きなこと（絵・色鉛筆・本）を生活に計画的に取り込む\n・葉酸・B6・鉄の食事からの補充\n\n【会社への提言】\n・「大森さんのおかげで○○が助かった」と具体的な貢献を言葉で伝える\n・急かさない・じっくり待てる環境づくり\n・「会社のために」という言葉が一番の動機づけになる'],
    ['三井 康平さん',
     '書面対応\n（4/25問診票\n分析）',
     '心理状態61%と安定。仕事への目的意識・前向きさは良好。\n身体面では胃腸・男性ホルモン・副腎・甲状腺・代謝が要注意ライン超え。\n特に制酸剤の長期使用による栄養吸収阻害・男性ホルモン低下が気になる。\n問診票結果・プロファイリング結果を書面でお渡し済み。',
     '書面にて問診票結果・アドバイスをお渡し済み。\n\n【三井社長へのご提案】\n・胃腸：制酸剤の長期使用は栄養吸収に影響している可能性があります。一度消化器内科へのご相談をお勧めいたします\n・男性ホルモン：複数の低下サインが見られます。泌尿器科・メンズクリニックでの検査（テストステロン・TSH）をお勧めいたします\n・現在の数値は早期対応が可能な段階です。自覚症状が少ないうちに検査・対処されることをお勧めいたします'],
]

tbl = doc.add_table(rows=len(data), cols=4)
tbl.style = 'Table Grid'
col_widths = [Cm(2.5), Cm(2.5), Cm(5.5), Cm(7.5)]
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

# ===== 【全体傾向と提言】=====
h3 = doc.add_paragraph()
r3 = h3.add_run('【全体傾向と提言】')
r3.font.bold = True
r3.font.size = Pt(10)

teigen = doc.add_paragraph(
    '■ 4ヶ月間を通じた全体傾向\n'
    '　リモートワーク中心の環境において、「オンとオフの切り替えが難しい」という課題が全員に共通していました。'
    '特に樋田さん・大森さんは「ゆっくりしたい」「休みたい」という体のサインを持ちながらも、'
    'それを表に出せずにいました。「自分のコンディションを言葉にする習慣」が育ってきたことは、4ヶ月の大きな成果です。\n\n'
    '■ 今後に向けた提言\n'
    '① 樋田さんの状態を継続的に見守ってください\n'
    '　　前回の休職前と似た業務負荷が6月に再び高まっていた時期がありました。'
    '「同じ状況になりそうなら伝える」という本人との約束が機能していますが、'
    '会社側からも「順調に進んでいますか？」という定期的な声かけを続けてください。\n\n'
    '② 浅野さんのキャリアに会社の言葉を\n'
    '　　30代のいま、「この会社にいたら何ができるようになるか」という問いに会社が答えられるかどうかが定着の鍵です。\n\n'
    '③ 佐藤社長の「お客様の立場で」を組織の文化に\n'
    '　　今回のセッションで生まれた行動指針を、ぜひ組織全体の合言葉として根付かせてください。\n\n'
    '④ 大森さん・三井さんへの個別の声かけを\n'
    '　　二人とも内に秘めるタイプです。「助かっています」「最近どうですか？」の一言が大きな安心感につながります。\n\n'
    '　引き続き、皆さまの健康と組織の活力を支えてまいります。どうぞよろしくお願いいたします。'
)
teigen.runs[0].font.size = Pt(10)

doc.add_paragraph()

p_end = doc.add_paragraph('以上')
p_end.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_end.runs[0].font.size = Pt(10)

output_path = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\株式会社サステナ\02_報告会記録\サステナ様_2026年3-6月_総括報告書.docx'
doc.save(output_path)
print(f'保存完了：{output_path}')
