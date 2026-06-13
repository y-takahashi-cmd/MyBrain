import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

matplotlib.rcParams['font.family'] = 'Meiryo'

PRIMARY = '#74B2E0'
SECONDARY = '#1E3A5F'
LIGHT = '#B8D9F0'

output_path = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\クラウドパワー株式会社\02_報告会記録\クラウドパワー様_アンケート結果_2026年6月.pdf'

with PdfPages(output_path) as pdf:

    # --- 表紙 ---
    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_subplot(111)
    ax.axis('off')
    fig.patch.set_facecolor('white')
    ax.axhline(y=0.82, xmin=0.1, xmax=0.9, color=PRIMARY, linewidth=3)
    ax.axhline(y=0.18, xmin=0.1, xmax=0.9, color=PRIMARY, linewidth=3)
    ax.text(0.5, 0.75, 'クラウドパワー株式会社', ha='center', va='center',
            fontsize=18, color=SECONDARY, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.65, '企業のオンライン保健室', ha='center', va='center',
            fontsize=14, color=SECONDARY, transform=ax.transAxes)
    ax.text(0.5, 0.53, '社員アンケート集計結果', ha='center', va='center',
            fontsize=26, color=PRIMARY, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.42, '2026年6月', ha='center', va='center',
            fontsize=14, color=SECONDARY, transform=ax.transAxes)
    ax.text(0.5, 0.33, '回答数：5件（全員回答）', ha='center', va='center',
            fontsize=13, color='#555555', transform=ax.transAxes)
    ax.text(0.5, 0.24, '企業のオンライン保健室　髙橋由香', ha='center', va='center',
            fontsize=12, color=SECONDARY, transform=ax.transAxes)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

    # --- Q1: 円グラフ ---
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.patch.set_facecolor('white')
    fig.text(0.5, 0.92, 'Q1　現在の状態に最も近いものを選んでください',
             ha='center', fontsize=13, color=SECONDARY, fontweight='bold')
    fig.text(0.5, 0.88, '単一選択・回答 5件',
             ha='center', fontsize=10, color='#666666')
    ax_pie = fig.add_axes([0.2, 0.45, 0.6, 0.38])
    labels = ['元気に働いている\n3件（60%）', '少し疲れている\n2件（40%）']
    sizes = [60, 40]
    colors = [PRIMARY, LIGHT]
    ax_pie.pie(sizes, labels=labels, colors=colors, startangle=90,
               textprops={'fontsize': 12, 'color': SECONDARY})
    ax_pie.axis('equal')
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

    # --- Q2〜Q6: 横棒グラフ ---
    questions = [
        {
            'q': 'Q2　現在、気になっていることを教えてください',
            'items': ['睡眠', '疲労感', 'ストレス', '将来への不安', 'お金', '特になし'],
            'values': [40, 40, 40, 20, 20, 40]
        },
        {
            'q': 'Q3　今後、変えていきたいことは何ですか',
            'items': ['仕事の進め方', '睡眠', 'ストレス対策', '人間関係', 'コミュニケーション', '時間管理'],
            'values': [60, 40, 40, 20, 20, 20]
        },
        {
            'q': 'Q4　困った時に相談する相手を教えてください',
            'items': ['自分で解決する', '友人', '上司', '家族', '同僚', '専門家'],
            'values': [80, 60, 60, 40, 40, 0]
        },
        {
            'q': 'Q5　会社にあったら嬉しいサポートを教えてください',
            'items': ['仕事の整理や考え方', '特に必要ない', 'メンタル相談', '個別相談'],
            'values': [40, 40, 20, 20]
        },
        {
            'q': 'Q6　オンライン保健室に今後期待することを教えてください',
            'items': ['健康相談', 'ストレス相談', 'よく分からない'],
            'values': [60, 60, 20]
        },
    ]

    for q_data in questions:
        fig = plt.figure(figsize=(8.27, 11.69))
        fig.patch.set_facecolor('white')
        fig.text(0.5, 0.92, q_data['q'],
                 ha='center', fontsize=13, color=SECONDARY, fontweight='bold')
        fig.text(0.5, 0.88, '複数回答・回答 5件',
                 ha='center', fontsize=10, color='#666666')

        n = len(q_data['items'])
        height = min(0.45, n * 0.08)
        top = 0.82
        ax_bar = fig.add_axes([0.3, top - height, 0.55, height])

        items = q_data['items'][::-1]
        values = q_data['values'][::-1]
        y_pos = np.arange(len(items))

        bars = ax_bar.barh(y_pos, values, color=PRIMARY, height=0.5)
        ax_bar.set_yticks(y_pos)
        ax_bar.set_yticklabels(items, fontsize=11)
        ax_bar.set_xlim(0, 105)
        ax_bar.set_xlabel('%', fontsize=10)
        ax_bar.spines['top'].set_visible(False)
        ax_bar.spines['right'].set_visible(False)

        for bar, val in zip(bars, values):
            if val > 0:
                ax_bar.text(val + 1, bar.get_y() + bar.get_height() / 2,
                            f'{val}%', va='center', fontsize=11, color=SECONDARY)

        pdf.savefig(fig, bbox_inches='tight')
        plt.close()

    # --- Q7: 自由記述 ---
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.patch.set_facecolor('white')
    fig.text(0.5, 0.92, 'Q7　会社をより働きやすくするために改善したいことがあれば教えてください',
             ha='center', fontsize=11, color=SECONDARY, fontweight='bold')
    fig.text(0.5, 0.88, '自由記述・記入 1件',
             ha='center', fontsize=10, color='#666666')

    ax_q7 = fig.add_axes([0.1, 0.6, 0.8, 0.22])
    ax_q7.axis('off')
    ax_q7.text(0.5, 0.5,
               '「社長の意見が絶対になってしまうため、\n社長のいない会話の場を設ける\n必要があると考えている」',
               ha='center', va='center', fontsize=13, color=SECONDARY,
               style='italic',
               bbox=dict(boxstyle='round,pad=0.8', facecolor=LIGHT, alpha=0.5))

    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

print("PDF作成完了")
