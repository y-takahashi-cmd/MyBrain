# -*- coding: utf-8 -*-
"""
クラウドパワー株式会社 3ページ統合版（サステナ版ベース）
Page1: パワーカラー相関図 + アクティビティ
Page2: 思考パターン・意思決定マップ
Page3: 適材適所 役割マッピング（長谷川・佐治・青木・林・中丸・有田・古崎）
"""
import math
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
    {'id': '長', 'name': '長谷川', 'nine': '空',
     'power_color': '紫', 'grid': (1, 2),
     'fc': '#6A1B9A', 'ec': '#4A148C', 'tc': 'white',
     'activity': 304_873_991, 'activity_type': '直感型',
     'thought_pos': 4.0, 'speed_pos': 7.2,
     'thinking': 34, 'thinking_type': 'フィーリングタイプ'},
    {'id': '佐', 'name': '佐治', 'nine': '創',
     'power_color': '黒', 'grid': (1, 1),
     'fc': '#212121', 'ec': '#000000', 'tc': 'white',
     'activity': 123_056_640, 'activity_type': '過去型',
     'thought_pos': 1.0, 'speed_pos': 4.8,
     'thinking': 44, 'thinking_type': '両方タイプ'},
    {'id': '青', 'name': '青木', 'nine': '守',
     'power_color': '黒', 'grid': (1, 1),
     'fc': '#424242', 'ec': '#212121', 'tc': 'white',
     'activity': 127_251_753, 'activity_type': '現在型',
     'thought_pos': 2.0, 'speed_pos': 5.4,
     'thinking': 26, 'thinking_type': 'フィーリングタイプ'},
    {'id': '林', 'name': '林', 'nine': '王',
     'power_color': '赤', 'grid': (2, 1),
     'fc': '#C62828', 'ec': '#B71C1C', 'tc': 'white',
     'activity': 484_768_582, 'activity_type': '未来型',
     'thought_pos': 3.0, 'speed_pos': 6.2,
     'thinking': 64, 'thinking_type': '両方タイプ'},
    {'id': '中', 'name': '中丸', 'nine': '全',
     'power_color': '紫', 'grid': (1, 2),
     'fc': '#7B1FA2', 'ec': '#4A148C', 'tc': 'white',
     'activity': 1_676_127_325, 'activity_type': '未来型',
     'thought_pos': 3.0, 'speed_pos': 6.3,
     'thinking': 88, 'thinking_type': 'ロジカルタイプ'},
    {'id': '有', 'name': '有田', 'nine': '守',
     'power_color': '白', 'grid': (2, 2),
     'fc': '#FAFAFA', 'ec': '#757575', 'tc': '#333333',
     'activity': 39_474_013, 'activity_type': '過去型',
     'thought_pos': 1.0, 'speed_pos': 4.2,
     'thinking': 81, 'thinking_type': 'ロジカルタイプ'},
    {'id': '古', 'name': '古崎', 'nine': '智',
     'power_color': '黒', 'grid': (1, 1),
     'fc': '#212121', 'ec': '#000000', 'tc': 'white',
     'activity': 2_824_149_888, 'activity_type': '未来型',
     'thought_pos': 3.0, 'speed_pos': 6.9,
     'thinking': 98, 'thinking_type': 'ロジカルタイプ'},
]

AVERAGE = 240_000_000
OUTPUT = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\クラウドパワー株式会社\02_報告会記録\クラウドパワー株式会社_プロファイリング関係図.pdf'

COLOR_GRID = {
    (0, 2): ('藍', '#283593', 'white'),
    (1, 2): ('紫', '#6A1B9A', 'white'),
    (2, 2): ('白', '#FAFAFA', '#333333'),
    (0, 1): ('青', '#1565C0', 'white'),
    (1, 1): ('黒', '#212121', 'white'),
    (2, 1): ('赤', '#C62828', 'white'),
    (0, 0): ('緑', '#2E7D32', 'white'),
    (1, 0): ('黄', '#F9A825', '#333333'),
    (2, 0): ('橙', '#E65100', 'white'),
}

BOX = 2.0
GAP = 0.8
OX  = 0.5
OY  = 0.5

def grid_center(col, row):
    x = OX + col * (BOX + GAP) + BOX / 2
    y = OY + row * (BOX + GAP) + BOX / 2
    return x, y

def draw_arrow(ax, g1, g2, bidirectional=False, color='#B8960C'):
    x1, y1 = grid_center(*g1)
    x2, y2 = grid_center(*g2)
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    pad = BOX / 2 + 0.08
    sx, sy = x1 + ux * pad, y1 + uy * pad
    ex, ey = x2 - ux * pad, y2 - uy * pad
    style = '<->' if bidirectional else '->'
    ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=2, mutation_scale=13))

def member_badge(ax, x, y, m, r=0.30):
    circ = mpatches.Circle((x, y), r, facecolor=m['fc'],
                            edgecolor=m['ec'], linewidth=2, zorder=10)
    ax.add_patch(circ)
    ax.text(x, y, m['id'], ha='center', va='center', fontsize=8,
            fontweight='bold', color=m['tc'], zorder=11)

# ========================
# PAGE 1: カラー相関図 + アクティビティ
# ========================
fig1 = plt.figure(figsize=(16, 10))
fig1.patch.set_facecolor('#FFFFFF')
fig1.suptitle('クラウドパワー株式会社　可能性から見る関係図（7名版）',
              fontsize=17, fontweight='bold', y=0.98)

ax_c = fig1.add_axes([0.02, 0.05, 0.50, 0.88])
ax_c.set_xlim(0, 9.5)
ax_c.set_ylim(0, 9.5)
ax_c.axis('off')

tb = mpatches.FancyBboxPatch((0.2, 8.5), 5.0, 0.8,
                              boxstyle='round,pad=0.15',
                              facecolor='#FBCECC', edgecolor='#E57373', lw=1.5)
ax_c.add_patch(tb)
ax_c.text(2.7, 8.9, 'パワーカラーからわかる話が伝わりやすい相関図',
          ha='center', va='center', fontsize=9.5, fontweight='bold')
ax_c.text(5.8, 8.9, 'あなたは、どこのポジション？\nよくベクトルをみてみましょう！',
          ha='center', va='center', fontsize=8.5)

member_grid_map = {}
for m in MEMBERS:
    member_grid_map.setdefault(m['grid'], []).append(m)

for (col, row), (label, fc, tc) in COLOR_GRID.items():
    x = OX + col * (BOX + GAP)
    y = OY + row * (BOX + GAP)
    box = FancyBboxPatch((x, y), BOX, BOX,
                         boxstyle='round,pad=0.12',
                         facecolor=fc, edgecolor='white', linewidth=2.5, zorder=3)
    ax_c.add_patch(box)
    members_here = member_grid_map.get((col, row), [])

    if len(members_here) == 0:
        ax_c.text(x + BOX/2, y + BOX/2, label,
                  ha='center', va='center', fontsize=16, fontweight='bold',
                  color=tc, zorder=4)
    elif len(members_here) == 1:
        m = members_here[0]
        ax_c.text(x + BOX/2, y + BOX*0.72, label,
                  ha='center', va='center', fontsize=14, fontweight='bold',
                  color=tc, zorder=4)
        ax_c.text(x + BOX/2, y + BOX*0.28, f"{m['id']}（{m['name']}）",
                  ha='center', va='center', fontsize=8.5,
                  fontweight='bold', color=tc, zorder=4)
        member_badge(ax_c, x + BOX - 0.28, y + BOX - 0.28, m, r=0.26)
    elif len(members_here) == 2:
        ax_c.text(x + BOX/2, y + BOX*0.90, label,
                  ha='center', va='center', fontsize=11, fontweight='bold',
                  color=tc, zorder=4)
        m0 = members_here[0]
        ax_c.text(x + BOX/2, y + BOX*0.66, f"{m0['id']}（{m0['name']}）",
                  ha='center', va='center', fontsize=7.5,
                  fontweight='bold', color=tc, zorder=4)
        member_badge(ax_c, x + BOX*0.25, y + BOX*0.50, m0, r=0.22)
        ax_c.plot([x+0.2, x+BOX-0.2], [y+BOX*0.42, y+BOX*0.42],
                  color='#AAAAAA', lw=0.8, zorder=4)
        m1 = members_here[1]
        ax_c.text(x + BOX/2, y + BOX*0.28, f"{m1['id']}（{m1['name']}）",
                  ha='center', va='center', fontsize=7.5,
                  fontweight='bold', color=tc, zorder=4)
        member_badge(ax_c, x + BOX*0.75, y + BOX*0.15, m1, r=0.22)
    else:
        # 3人以上（黒ブロック：佐治・青木・古崎）
        ax_c.text(x + BOX/2, y + BOX*0.93, label,
                  ha='center', va='center', fontsize=10, fontweight='bold',
                  color=tc, zorder=4)
        offsets = [(0.22, 0.72), (0.78, 0.72), (0.50, 0.30)]
        for i, m in enumerate(members_here[:3]):
            ox, oy = offsets[i]
            member_badge(ax_c, x + BOX*ox, y + BOX*oy, m, r=0.20)
            ax_c.text(x + BOX*ox, y + BOX*oy - 0.28,
                      m['name'], ha='center', va='center',
                      fontsize=6.5, fontweight='bold', color=tc, zorder=4)

# ── 矢印（サステナ版と同じパターン） ──
draw_arrow(ax_c, (0,2), (1,2))
draw_arrow(ax_c, (1,2), (2,2))
draw_arrow(ax_c, (1,1), (0,1))
draw_arrow(ax_c, (1,1), (2,1))
draw_arrow(ax_c, (0,0), (1,0))
draw_arrow(ax_c, (1,0), (2,0))
draw_arrow(ax_c, (0,0), (0,1))
draw_arrow(ax_c, (0,1), (0,2))
draw_arrow(ax_c, (2,0), (2,1))
draw_arrow(ax_c, (2,1), (2,2))
draw_arrow(ax_c, (1,1), (1,2))
draw_arrow(ax_c, (1,1), (1,0))
draw_arrow(ax_c, (1,1), (0,2))
draw_arrow(ax_c, (1,1), (2,2))
draw_arrow(ax_c, (1,1), (0,0))
draw_arrow(ax_c, (1,1), (2,0))

# -- 右: アクティビティレベル --
ax_a = fig1.add_axes([0.54, 0.08, 0.43, 0.84])
ax_a.set_xlim(0, 10)
ax_a.set_ylim(0, 10)
ax_a.axis('off')

ax_a.text(5, 9.7, 'アクティビティーレベル', ha='center', va='top',
          fontsize=12, fontweight='bold', color='#B8860B')
ax_a.annotate('', xy=(5, 9.2), xytext=(5, 0.8),
              arrowprops=dict(arrowstyle='<->', color='#B8860B', lw=2.5, mutation_scale=16))
ax_a.text(5, 9.5, '営業・対面・講師', ha='center', va='center',
          fontsize=9, fontweight='bold', color='#E67E22')
ax_a.text(5, 0.4, '事務作業・スピリチュアル', ha='center', va='center',
          fontsize=9, fontweight='bold', color='#E67E22')
ax_a.text(1.2, 8.2, 'オープン\nマインド', ha='center', va='center',
          fontsize=8.5, fontweight='bold', color='#E67E22')
ax_a.text(1.2, 1.8, '心開き\nにくい', ha='center', va='center',
          fontsize=8.5, fontweight='bold', color='#E67E22')

avg_y = 2.8
ax_a.axhline(y=avg_y, xmin=0.3, xmax=0.75, color='#999999', linestyle='--', linewidth=1.2)
ax_a.text(8.5, avg_y + 0.15, f'平均基準\n{AVERAGE:,}', ha='center',
          va='bottom', fontsize=7.5, color='#888888')

all_vals = [m['activity'] for m in MEMBERS] + [AVERAGE]
v_min = min(all_vals) * 0.75
v_max = max(all_vals) * 1.08

def to_y(val):
    return 1.2 + (val - v_min) / (v_max - v_min) * 7.5

sorted_members = sorted(MEMBERS, key=lambda x: x['activity'])
y_positions = {}
for m in sorted_members:
    yp = to_y(m['activity'])
    for existing_yp in y_positions.values():
        if abs(yp - existing_yp) < 0.6:
            yp = existing_yp + 0.7
    y_positions[m['id']] = yp

for m in MEMBERS:
    yp = y_positions[m['id']]
    ax_a.plot([3.8, 6.2], [yp, yp], color='#CCCCCC', lw=0.8, zorder=2)
    member_badge(ax_a, 5.0, yp, m, r=0.38)
    ax_a.text(3.5, yp, f"{m['activity']:,}", ha='right', va='center',
              fontsize=7.5, color='#333333')
    ax_a.text(6.5, yp, f"{m['id']}（{m['name']}）\n{m['activity_type']}",
              ha='left', va='center', fontsize=7.5, color='#333333')

fig1.text(0.54, 0.03,
          '長：長谷川誠（空）　佐：佐治麻里（創）　青：青木智弘（守）　林：林美由紀（王）　中：中丸哲哉（全）　有：有田基志（守）　古：古崎晴貴（智）',
          fontsize=7.5, ha='left', va='bottom', color='#555555',
          bbox=dict(boxstyle='round', facecolor='#F5F5F5', alpha=0.8))

# ========================
# PAGE 2: 思考パターン・意思決定マップ
# ========================
fig2 = plt.figure(figsize=(16, 10))
fig2.patch.set_facecolor('#FFFFFF')
fig2.suptitle('クラウドパワー株式会社　思考パターン・意思決定マップ（7名版）',
              fontsize=17, fontweight='bold', y=0.98)

ax_th = fig2.add_axes([0.06, 0.58, 0.88, 0.36])
ax_th.set_xlim(-0.5, 5.5)
ax_th.set_ylim(-2.2, 1.5)
ax_th.axis('off')
ax_th.text(-0.4, 1.3, '思考型', fontsize=13, fontweight='bold', color='#E67E22')
ax_th.annotate('', xy=(5.4, 0), xytext=(-0.4, 0),
               arrowprops=dict(arrowstyle='<->', color='#B8860B', lw=2.5, mutation_scale=16))
types = ['精神型', '過去型', '現在型', '未来型', '直観', '創造']
for i, t in enumerate(types):
    ax_th.text(i, 0.25, t, ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax_th.plot(i, 0, 'k|', markersize=12, markeredgewidth=1.5)
ax_th.text(-0.4, -0.6, 'リスクマネジメント\n的存在', ha='center', va='top', fontsize=8.5, color='#555555')
ax_th.text(5.4, -0.6, '改革的\n存在', ha='center', va='top', fontsize=8.5, color='#555555')

thought_groups = {}
for m in MEMBERS:
    thought_groups.setdefault(round(m['thought_pos'], 1), []).append(m)
for pos, group in thought_groups.items():
    for i, m in enumerate(group):
        badge_y = -0.7 - i * 0.75
        member_badge(ax_th, pos, badge_y, m, r=0.32)
        ax_th.text(pos, badge_y - 0.4, f"{m['name']}（{m['nine']}）",
                   ha='center', va='top', fontsize=7.5, fontweight='bold', color='#333333')
        ax_th.text(pos, badge_y - 0.8, types[max(0, min(5, int(round(pos))))],
                   ha='center', va='top', fontsize=7.5, color='#666666')

ax_sp = fig2.add_axes([0.06, 0.22, 0.88, 0.32])
ax_sp.set_xlim(-0.5, 10.5)
ax_sp.set_ylim(-2.2, 1.5)
ax_sp.axis('off')
ax_sp.text(-0.4, 1.3, '気持ちの決定速度', fontsize=13, fontweight='bold', color='#E67E22')
ax_sp.text(5, 1.3, '数値０はすべてのマインド速度にあわせられる',
           ha='center', va='center', fontsize=8.5, color='#888888')
ax_sp.annotate('', xy=(10.4, 0), xytext=(-0.4, 0),
               arrowprops=dict(arrowstyle='<->', color='#B8860B', lw=2.5, mutation_scale=16))
for i in range(11):
    ax_sp.plot(i, 0, 'k|', markersize=10, markeredgewidth=1.5)
ax_sp.axvline(x=4, ymin=0.5, ymax=0.75, color='#888888', lw=1, linestyle='--')
ax_sp.text(4, 0.5, '標準４', ha='center', va='bottom', fontsize=8.5, color='#888888', fontweight='bold')
ax_sp.text(-0.4, -0.5, 'のんびり\n決められない', ha='center', va='center', fontsize=8.5, color='#555555')
ax_sp.text(10.4, -0.5, '決断早い\nイライラしやすい', ha='center', va='center', fontsize=8.5, color='#555555')

speed_groups = {}
for m in MEMBERS:
    speed_groups.setdefault(round(m['speed_pos'], 1), []).append(m)
for pos, group in speed_groups.items():
    for i, m in enumerate(group):
        badge_y = -0.7 - i * 0.75
        member_badge(ax_sp, pos, badge_y, m, r=0.32)
        desc = 'じっくり' if pos <= 3 else ('標準' if pos <= 5 else 'せっかち')
        ax_sp.text(pos, badge_y - 0.4, m['name'], ha='center', va='top', fontsize=7.5, fontweight='bold', color='#333333')
        ax_sp.text(pos, badge_y - 0.8, desc, ha='center', va='top', fontsize=7.5, color='#666666')

ax_sk = fig2.add_axes([0.06, 0.03, 0.88, 0.17])
ax_sk.set_xlim(10, 100)
ax_sk.set_ylim(-1.5, 1.2)
ax_sk.axis('off')
ax_sk.text(55, 1.1, 'シンキングパターン　pattern of thinking',
           ha='center', va='top', fontsize=11, fontweight='bold', color='#E67E22')
ax_sk.add_patch(mpatches.FancyBboxPatch((11, -0.25), 78, 0.5, boxstyle='round,pad=0.1',
                facecolor='#F0F4C3', edgecolor='#CDDC39', lw=1))
ax_sk.add_patch(mpatches.FancyBboxPatch((11, -0.25), 28, 0.5, boxstyle='round,pad=0.1',
                facecolor='#C8E6C9', edgecolor='none'))
ax_sk.add_patch(mpatches.FancyBboxPatch((39, -0.25), 31, 0.5, boxstyle='round,pad=0.1',
                facecolor='#FFF9C4', edgecolor='none'))
ax_sk.add_patch(mpatches.FancyBboxPatch((70, -0.25), 19, 0.5, boxstyle='round,pad=0.1',
                facecolor='#FFE0B2', edgecolor='none'))
for v in [11, 20, 30, 40, 50, 60, 70, 80, 90, 99]:
    ax_sk.plot(v, -0.25, 'k|', markersize=8)
    ax_sk.text(v, -0.5, str(v), ha='center', va='top', fontsize=7.5, color='#555555')
ax_sk.text(25, 0.0, 'フィーリングタイプ', ha='center', va='center', fontsize=9, color='#2E7D32')
ax_sk.text(54, 0.0, '両方タイプ', ha='center', va='center', fontsize=9, color='#F9A825')
ax_sk.text(84, 0.0, 'ロジカルタイプ', ha='center', va='center', fontsize=9, color='#E65100')

thinking_groups = {}
for m in MEMBERS:
    thinking_groups.setdefault(m['thinking'], []).append(m)
for sc, group in thinking_groups.items():
    for i, m in enumerate(group):
        badge_y = -1.0 - i * 0.45
        member_badge(ax_sk, sc, badge_y, m, r=0.28)
        ax_sk.text(sc, badge_y - 0.35, f"{m['id']}{sc}",
                   ha='center', va='top', fontsize=7.5, color='#333333')

# ========================
# PAGE 3: 役割マッピング（長谷川・佐治・青木・林・中丸・有田・古崎）
# ========================
MAPPING_MEMBERS = [
    {
        'full': '長谷川 誠', 'role_title': '経営判断・ビジョン提示役',
        'sub': '紫・空（直感型）　活動量：304M',
        'color_h': '#6A1B9A', 'color_bg': '#F3E5F5', 'color_edge': '#4A148C',
        'text_color': 'white',
        'fit': ['ビジョン創出・新規アイデア発信',
                '感性を活かした経営判断',
                '変化ある環境でのリーダーシップ'],
        'point': ['直感を大切にした意思決定を尊重',
                  '決めたことへの信念はブレない',
                  '変化・刺激が活力の源',
                  '感情が共鳴しやすい環境づくりが鍵'],
    },
    {
        'full': '佐治 麻里', 'role_title': '実務管理・品質保証役',
        'sub': '黒・創（過去型）　活動量：123M',
        'color_h': '#212121', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': ['実務・タスク管理・品質保証',
                '過去データ活用・実績管理',
                '黙々と確実に進める業務'],
        'point': ['感情への共感を大切に',
                  '白黒明確な指示が合う',
                  '結果を認めてモチベーションアップ',
                  '過去型→実績ベースの提案が刺さる'],
    },
    {
        'full': '青木 智弘', 'role_title': '現場維持・安定運営役',
        'sub': '黒・守（現在型）　活動量：127M',
        'color_h': '#424242', 'color_bg': '#FAFAFA', 'color_edge': '#616161',
        'text_color': 'white',
        'fit': ['現場維持・ルーティン管理',
                'チームの安定運営・調和',
                '着実な業務遂行'],
        'point': ['現在に集中した具体的指示が合う',
                  'チームの雰囲気に馴染む適応力',
                  '感情に寄り添うサポートが効果的',
                  'フィーリング最低値→安心感が最重要'],
    },
    {
        'full': '林 美由紀', 'role_title': 'リーダーシップ・育成役',
        'sub': '赤・王（未来型）　活動量：484M',
        'color_h': '#C62828', 'color_bg': '#FFEBEE', 'color_edge': '#B71C1C',
        'text_color': 'white',
        'fit': ['チームリーダー・人材育成',
                '情熱で引っ張るまとめ役',
                '誠実なコミュニケーション推進'],
        'point': ['情熱に火をつける課題設定',
                  '真面目さ・誠実さを認める',
                  'リーダーとして活躍できる機会を',
                  '「ありがとう・助かった」が最大の原動力'],
    },
    {
        'full': '中丸 哲哉', 'role_title': '未来志向・プランニング役',
        'sub': '紫・全（未来型）　活動量：1,676M',
        'color_h': '#7B1FA2', 'color_bg': '#F3E5F5', 'color_edge': '#4A148C',
        'text_color': 'white',
        'fit': ['未来ビジョン構築・新規開拓',
                'チームへのビジョン共有',
                '変化への素早い適応'],
        'point': ['未来の可能性を語って動機づけ',
                  '論理的根拠も合わせて提示',
                  '感情の波に寄り添いながら',
                  'ロジカル高値→データと根拠で動く'],
    },
    {
        'full': '有田 基志', 'role_title': '情報収集・サポート役',
        'sub': '白・守（過去型）　活動量：39M',
        'color_h': '#757575', 'color_bg': '#FAFAFA', 'color_edge': '#9E9E9E',
        'text_color': 'white',
        'fit': ['情報収集・サポート業務',
                '多様な役割への柔軟な適応',
                'ロジカル分析・資料整理'],
        'point': ['じっくり考える時間を与える',
                  'ロジカルな説明で動きやすい',
                  '義理人情に応える関わりが効果的',
                  '活動量最低値→負担のない役割設定が鍵'],
    },
    {
        'full': '古崎 晴貴', 'role_title': '突破力・問題解決役',
        'sub': '黒・智（未来型）　活動量：2,824M',
        'color_h': '#212121', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': ['問題解決・障壁突破',
                'ロジカル分析＋即実行',
                '新規挑戦・スピード推進'],
        'point': ['感情の波を受け止め率直に対話',
                  '明確な目標設定で本領発揮',
                  '活躍の場を与えることが重要',
                  'SP最高値（98）→データ・論理が動力'],
    },
]

fig3 = plt.figure(figsize=(16, 10.5))
fig3.patch.set_facecolor('#F7F8FC')

header = FancyBboxPatch((0.01, 0.92), 0.98, 0.07,
                         boxstyle='round,pad=0.005',
                         facecolor='#3949AB', edgecolor='none',
                         transform=fig3.transFigure, zorder=5)
fig3.add_artist(header)
fig3.text(0.5, 0.958, '適材適所　各メンバーの役割マッピング',
         ha='center', va='center', fontsize=17, fontweight='bold',
         color='white', transform=fig3.transFigure, zorder=6)
fig3.text(0.5, 0.930, 'LifeProfiling® から導く「最も力を発揮できる役割と関わり方のポイント」',
         ha='center', va='center', fontsize=9, color='#C5CAE9',
         transform=fig3.transFigure, zorder=6)

def draw_card(fig, left, bottom, width, height, member):
    ax = fig.add_axes([left, bottom, width, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
                                boxstyle='round,pad=0.02',
                                facecolor=member['color_bg'],
                                edgecolor=member['color_edge'], linewidth=1.5))
    ax.add_patch(FancyBboxPatch((0.02, 0.78), 0.96, 0.20,
                                boxstyle='round,pad=0.01',
                                facecolor=member['color_h'], edgecolor='none'))
    ax.text(0.50, 0.915, member['full'], ha='center', va='center',
            fontsize=13, fontweight='bold', color=member['text_color'])
    ax.text(0.50, 0.820, member['role_title'], ha='center', va='center',
            fontsize=9.5, fontweight='bold', color=member['text_color'])
    ax.text(0.50, 0.740, member['sub'], ha='center', va='center',
            fontsize=7.5, color='#555555')
    ax.plot([0.05, 0.95], [0.715, 0.715], color=member['color_edge'],
            linewidth=0.8, alpha=0.5)
    ax.text(0.06, 0.690, '■ 向いている仕事：', ha='left', va='center',
            fontsize=8, fontweight='bold', color=member['color_h'])
    y = 0.640
    for line in member['fit']:
        ax.text(0.08, y, f'・{line}', ha='left', va='center',
                fontsize=7.5, color='#333333')
        y -= 0.075
    ax.plot([0.05, 0.95], [y + 0.02, y + 0.02], color=member['color_edge'],
            linewidth=0.8, alpha=0.3)
    y -= 0.045
    ax.text(0.06, y, '■ 関わり方のポイント：', ha='left', va='center',
            fontsize=8, fontweight='bold', color=member['color_h'])
    y -= 0.055
    for line in member['point']:
        ax.text(0.08, y, f'・{line}', ha='left', va='center',
                fontsize=7.2, color='#333333')
        y -= 0.068

# 上段4名・下段3名（中央揃え）
card_w, card_h, gap = 0.230, 0.415, 0.018
for i, m in enumerate(MAPPING_MEMBERS[:4]):
    left = 0.020 + i * (card_w + gap)
    draw_card(fig3, left, 0.490, card_w, card_h, m)

left_bottom = (1.0 - (card_w * 3 + gap * 2)) / 2
for i, m in enumerate(MAPPING_MEMBERS[4:]):
    left = left_bottom + i * (card_w + gap)
    draw_card(fig3, left, 0.060, card_w, card_h, m)

fig3.text(0.5, 0.025,
         'クラウドパワー株式会社　　│　　海音〜心体の調律〜　　髙橋由香　　2026年7月',
         ha='center', va='center', fontsize=8.5, color='#777777',
         transform=fig3.transFigure)

# ========================
# 3ページを1PDFに統合して保存
# ========================
with PdfPages(OUTPUT) as pdf:
    pdf.savefig(fig1, bbox_inches='tight')
    pdf.savefig(fig2, bbox_inches='tight')
    pdf.savefig(fig3, bbox_inches='tight')

plt.close('all')
print(f'保存完了: {OUTPUT}')
