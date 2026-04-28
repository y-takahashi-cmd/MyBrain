# -*- coding: utf-8 -*-
"""
サステナ様 適材適所 各メンバーの役割マッピング
グリットワークス版と同形式のカードレイアウト
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages

try:
    import japanize_matplotlib
except ImportError:
    plt.rcParams['font.family'] = ['Yu Gothic', 'MS Gothic', 'Meiryo', 'sans-serif']

plt.rcParams['axes.unicode_minus'] = False

MEMBERS = [
    {
        'full': '佐藤 洋介', 'role_title': '意思決定・采配役',
        'sub': '赤・王（過去型）　活動量：194M',
        'color_h': '#E53935', 'color_bg': '#FFEBEE', 'color_edge': '#B71C1C',
        'text_color': 'white',
        'fit': [
            '経営判断・ビジョン策定・対外交渉',
            '組織采配・クライアント対応',
            '仲間のために動く舵取り',
        ],
        'point': [
            '過去型×両方タイプ→根拠を示すと動く',
            '「ありがとう・助かった」が最大の原動力',
            '府に落ちると一気に動く。感情面も丁寧に',
            '旅・キャンプ等の一人時間が回復の鍵',
        ],
    },
    {
        'full': '樋田 雅史', 'role_title': '実行・技術推進役',
        'sub': '黄・匠（現在型）　活動量：466M',
        'color_h': '#F9A825', 'color_bg': '#FFFDE7', 'color_edge': '#F57F17',
        'text_color': '#333333',
        'fit': [
            'システム開発・技術実装・仕組み化',
            '現場での実行・技術課題の解決',
            '人を育てる・後進指導（得意分野）',
        ],
        'point': [
            '底抜けの明るさがチームを動かす本来の姿',
            '「楽しい」を先に見せると行動しやすい',
            'マネジメントより技術・実行者として輝く',
            '人を育てる・楽しませることに強いパワー',
        ],
    },
    {
        'full': '三井 康平', 'role_title': '黙々集中・独創実行役',
        'sub': '白・創（過去型）　活動量：139M',
        'color_h': '#757575', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': [
            '一人で深く掘り下げる専門作業・経営判断',
            '独創的なアイデアの具現化',
            'じっくり考える長期戦略・品質へのこだわり',
        ],
        'point': [
            '「まっいいか」の放置癖→数値・事実で短く',
            '過去型→「ずっとこの状態なら」が刺さる',
            '新習慣より「今の延長」の提案が通りやすい',
            '右腕・左腕への共有が仕事をはかどらせる',
        ],
    },
    {
        'full': '大森 美葉', 'role_title': 'サポート・品質保証役',
        'sub': '橙・王（未来型）　活動量：462M',
        'color_h': '#FF7043', 'color_bg': '#FBE9E7', 'color_edge': '#BF360C',
        'text_color': 'white',
        'fit': [
            '品質管理・バックオフィス・マニュアル整備',
            '人のサポート・チームの縁の下の力持ち',
            '計画を立てて丁寧に実行する業務',
        ],
        'point': [
            '「会社のために・助かりました」が力の源泉',
            '未来型→「こうなれる」で提案すると届く',
            'じっくりゆっくり→急かすと逆効果',
            '褒めること・存在への承認が突破口',
        ],
    },
    {
        'full': '浅野 航', 'role_title': '企画・調整・傾聴役',
        'sub': '白・長（未来型）　活動量：324M',
        'color_h': '#43A047', 'color_bg': '#E8F5E9', 'color_edge': '#1B5E20',
        'text_color': 'white',
        'fit': [
            '企画立案・プロジェクト調整・傾聴',
            'きっかけを与える・可能性を引き出す',
            'チームの関係構築・外部との橋渡し',
        ],
        'point': [
            '仕組み化・自律的な環境づくりが得意',
            '未来型×フィーリング→ビジョンと感覚で動く',
            '困ったら人に聞ける・助けを求めるのが得意',
            '「ながら改善」「思い出した時だけ」が合う',
        ],
    },
]

OUTPUT = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\株式会社サステナ\01_メンバーカルテ\サステナ様_適材適所役割マッピング.pdf'

fig = plt.figure(figsize=(16, 10.5))
fig.patch.set_facecolor('#F7F8FC')

# ヘッダー
header = FancyBboxPatch((0.01, 0.92), 0.98, 0.07,
                         boxstyle='round,pad=0.005',
                         facecolor='#3949AB', edgecolor='none',
                         transform=fig.transFigure, zorder=5)
fig.add_artist(header)
fig.text(0.5, 0.958, '適材適所　各メンバーの役割マッピング',
         ha='center', va='center', fontsize=17, fontweight='bold',
         color='white', transform=fig.transFigure, zorder=6)
fig.text(0.5, 0.930, 'LifeProfiling® から導く「最も力を発揮できる役割と関わり方のポイント」',
         ha='center', va='center', fontsize=9, color='#C5CAE9',
         transform=fig.transFigure, zorder=6)

# カード描画関数
def draw_card(fig, left, bottom, width, height, member):
    ax = fig.add_axes([left, bottom, width, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # カード背景
    bg = FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                         boxstyle='round,pad=0.02',
                         facecolor=member['color_bg'],
                         edgecolor=member['color_edge'],
                         linewidth=1.5)
    ax.add_patch(bg)

    # ヘッダー部分
    hdr = FancyBboxPatch((0.02, 0.78), 0.96, 0.20,
                          boxstyle='round,pad=0.01',
                          facecolor=member['color_h'],
                          edgecolor='none')
    ax.add_patch(hdr)

    ax.text(0.50, 0.915, member['full'],
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=member['text_color'])
    ax.text(0.50, 0.820, member['role_title'],
            ha='center', va='center', fontsize=9.5, fontweight='bold',
            color=member['text_color'])

    # サブ情報（パワーカラー・活動量）
    ax.text(0.50, 0.740, member['sub'],
            ha='center', va='center', fontsize=7.5, color='#555555')

    # 区切り線
    ax.plot([0.05, 0.95], [0.715, 0.715], color=member['color_edge'],
            linewidth=0.8, alpha=0.5)

    # ■向いている仕事
    ax.text(0.06, 0.690, '■ 向いている仕事：',
            ha='left', va='center', fontsize=8, fontweight='bold',
            color=member['color_h'])
    y = 0.640
    for line in member['fit']:
        ax.text(0.08, y, f'・{line}',
                ha='left', va='center', fontsize=7.5, color='#333333')
        y -= 0.075

    # 区切り線
    ax.plot([0.05, 0.95], [y + 0.02, y + 0.02], color=member['color_edge'],
            linewidth=0.8, alpha=0.3)

    # ■関わり方のポイント
    y -= 0.045
    ax.text(0.06, y, '■ 関わり方のポイント：',
            ha='left', va='center', fontsize=8, fontweight='bold',
            color=member['color_h'])
    y -= 0.055
    for line in member['point']:
        ax.text(0.08, y, f'・{line}',
                ha='left', va='center', fontsize=7.2, color='#333333')
        y -= 0.068

# カード配置：3列×1行目 + 2列中央×2行目
card_w = 0.305
card_h = 0.415
gap = 0.025

# 1行目（上段）: 佐藤・樋田・三井
positions_top = [
    (0.025, 0.490),
    (0.025 + card_w + gap, 0.490),
    (0.025 + (card_w + gap) * 2, 0.490),
]
# 2行目（下段）: 大森・浅野（中央寄せ）
total_bottom = card_w * 2 + gap
left_bottom = (1.0 - total_bottom) / 2
positions_bottom = [
    (left_bottom, 0.060),
    (left_bottom + card_w + gap, 0.060),
]

for i, m in enumerate(MEMBERS[:3]):
    l, b = positions_top[i]
    draw_card(fig, l, b, card_w, card_h, m)

for i, m in enumerate(MEMBERS[3:]):
    l, b = positions_bottom[i]
    draw_card(fig, l, b, card_w, card_h, m)

# フッター
fig.text(0.5, 0.025,
         '株式会社サステナ　　│　　海音〜心体の調律〜　　髙橋由香　　2026年4月',
         ha='center', va='center', fontsize=8.5, color='#777777',
         transform=fig.transFigure)

with PdfPages(OUTPUT) as pdf:
    pdf.savefig(fig, bbox_inches='tight')

plt.close(fig)
print(f'保存完了: {OUTPUT}')
