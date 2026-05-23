# -*- coding: utf-8 -*-
"""
杉山耕一税理士事務所 プロファイリング関係図 3ページ統合版（12名）
Page1: パワーカラー相関図 + アクティビティレベル
Page2: 思考パターン・意思決定マップ
Page3: 適材適所 役割マッピング（12名・4列×3行）
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

# ========================
# メンバーデータ（12名）
# ========================
# activity_type: 衝動型(>10億) / 体験型(>4億) / 直感型(>2億) / 思考型(<2億)
# thought_pos: 精神型=0, 過去型=1, 現在型=2, 未来型=3, 直観=4, 創造型=5
# speed_pos: Tempo値（0〜10）
# thinking: シンキングパターン（10〜99）
# ※ 石渡・松崎のシンキングパターン・時間軸は未取得のため推測値

MEMBERS = [
    # ---- 所長 ----
    {'id': '杉山', 'nine': '創',
     'power_color': '黄', 'grid': (1, 0),
     'fc': '#F9A825', 'ec': '#F57F17', 'tc': '#333333',
     'activity': 1_112_637_120, 'activity_type': '体験型',
     'thought_pos': 3.0, 'speed_pos': 6.8,
     'thinking': 57, 'thinking_type': '両方タイプ'},
    # ---- グループA ----
    {'id': '佐々木', 'nine': '空',
     'power_color': '白', 'grid': (2, 2),
     'fc': '#FAFAFA', 'ec': '#757575', 'tc': '#333333',
     'activity': 109_072_931, 'activity_type': '思考型',
     'thought_pos': 1.0, 'speed_pos': 4.3,
     'thinking': 45, 'thinking_type': '両方タイプ'},
    {'id': '王', 'nine': '創',
     'power_color': '藍', 'grid': (0, 2),
     'fc': '#283593', 'ec': '#1A237E', 'tc': 'white',
     'activity': 56_034_720, 'activity_type': '思考型',
     'thought_pos': 2.0, 'speed_pos': 5.0,
     'thinking': 42, 'thinking_type': '両方タイプ'},
    {'id': '梅田', 'nine': '長',
     'power_color': '黄', 'grid': (1, 0),
     'fc': '#F9A825', 'ec': '#F57F17', 'tc': '#333333',
     'activity': 8_763_124, 'activity_type': '思考型',
     'thought_pos': 2.0, 'speed_pos': 5.2,
     'thinking': 21, 'thinking_type': 'フィーリングタイプ'},
    # ---- グループB ----
    {'id': '富永', 'nine': '匠',
     'power_color': '緑', 'grid': (0, 0),
     'fc': '#2E7D32', 'ec': '#1B5E20', 'tc': 'white',
     'activity': 20_392_909, 'activity_type': '思考型',
     'thought_pos': 2.0, 'speed_pos': 5.4,
     'thinking': 13, 'thinking_type': 'フィーリングタイプ'},
    {'id': '松崎', 'nine': '長',
     'power_color': '青', 'grid': (0, 1),
     'fc': '#1565C0', 'ec': '#0D47A1', 'tc': 'white',
     'activity': 1_175_000_000, 'activity_type': '体験型',
     'thought_pos': 3.0, 'speed_pos': 6.2,
     'thinking': 50, 'thinking_type': '両方タイプ'},  # ※シンキング未取得・推測
    {'id': '楠本', 'nine': '公',
     'power_color': '赤', 'grid': (2, 1),
     'fc': '#C62828', 'ec': '#B71C1C', 'tc': 'white',
     'activity': 190_178_444, 'activity_type': '思考型',
     'thought_pos': 2.0, 'speed_pos': 5.3,
     'thinking': 28, 'thinking_type': 'フィーリング寄り'},
    # ---- グループC ----
    {'id': '中尾', 'nine': '王',
     'power_color': '黒', 'grid': (1, 1),
     'fc': '#212121', 'ec': '#000000', 'tc': 'white',
     'activity': 127_251_753, 'activity_type': '思考型',
     'thought_pos': 2.0, 'speed_pos': 5.4,
     'thinking': 26, 'thinking_type': 'フィーリングタイプ'},
    {'id': '澤田', 'nine': '守',
     'power_color': '赤', 'grid': (2, 1),
     'fc': '#C62828', 'ec': '#B71C1C', 'tc': 'white',
     'activity': 79_382_520, 'activity_type': '思考型',
     'thought_pos': 1.0, 'speed_pos': 4.8,
     'thinking': 91, 'thinking_type': 'ロジカルタイプ'},
    # ---- 追加メンバー ----
    {'id': '太田', 'nine': '長',
     'power_color': '藍', 'grid': (0, 2),
     'fc': '#283593', 'ec': '#1A237E', 'tc': 'white',
     'activity': 4_508_347_811, 'activity_type': '衝動型',
     'thought_pos': 5.0, 'speed_pos': 8.6,
     'thinking': 78, 'thinking_type': '両方タイプ'},
    {'id': '塩澤', 'nine': '智',
     'power_color': '白', 'grid': (2, 2),
     'fc': '#FAFAFA', 'ec': '#757575', 'tc': '#333333',
     'activity': 1_196_595_975, 'activity_type': '体験型',
     'thought_pos': 3.0, 'speed_pos': 6.4,
     'thinking': 99, 'thinking_type': 'ロジカルタイプ'},
    {'id': '石渡', 'nine': '−',
     'power_color': '青', 'grid': (0, 1),
     'fc': '#1565C0', 'ec': '#0D47A1', 'tc': 'white',
     'activity': 350_000_000, 'activity_type': '直感型',  # ※アクティビティ「高い」から推測
     'thought_pos': 2.0, 'speed_pos': 7.0,             # ※未取得・推測
     'thinking': 50, 'thinking_type': '両方タイプ'},     # ※未取得・推測
]

AVERAGE = 240_000_000
OUTPUT = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\杉山耕一税理士事務所\02_報告会記録\杉山耕一税理士事務所_プロファイリング関係図.pdf'

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

def draw_arrow(ax, g1, g2, color='#B8960C'):
    x1, y1 = grid_center(*g1)
    x2, y2 = grid_center(*g2)
    dx, dy = x2 - x1, y2 - y1
    dist = math.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    pad = BOX / 2 + 0.08
    sx, sy = x1 + ux * pad, y1 + uy * pad
    ex, ey = x2 - ux * pad, y2 - uy * pad
    ax.annotate('', xy=(ex, ey), xytext=(sx, sy),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=2, mutation_scale=13))

def member_badge(ax, x, y, m, r=0.30):
    circ = mpatches.Circle((x, y), r, facecolor=m['fc'],
                            edgecolor=m['ec'], linewidth=2, zorder=10)
    ax.add_patch(circ)
    ax.text(x, y, m['id'], ha='center', va='center', fontsize=5,
            fontweight='bold', color=m['tc'], zorder=11)

# ========================
# PAGE 1: カラー相関図 + アクティビティ
# ========================
fig1 = plt.figure(figsize=(16, 10))
fig1.patch.set_facecolor('#FFFFFF')
fig1.suptitle('杉山耕一税理士事務所　可能性から見る関係図（12名版）',
              fontsize=16, fontweight='bold', y=0.98)

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
        ax_c.text(x + BOX/2, y + BOX*0.75, label,
                  ha='center', va='center', fontsize=13, fontweight='bold',
                  color=tc, zorder=4)
        ax_c.text(x + BOX/2, y + BOX*0.30, m['id'],
                  ha='center', va='center', fontsize=8,
                  fontweight='bold', color=tc, zorder=4)
        member_badge(ax_c, x + BOX - 0.28, y + BOX - 0.28, m, r=0.24)
    else:
        # 複数名
        n = len(members_here)
        ax_c.text(x + BOX/2, y + BOX*0.92, label,
                  ha='center', va='center', fontsize=11, fontweight='bold',
                  color=tc, zorder=4)
        slot_h = (BOX * 0.85) / n
        for idx, mi in enumerate(members_here):
            sy = y + BOX*0.85 - (idx + 0.5) * slot_h
            badge_x = x + BOX * 0.25
            ax_c.text(x + BOX * 0.60, sy, mi['id'],
                      ha='center', va='center', fontsize=6.5,
                      fontweight='bold', color=tc, zorder=4)
            member_badge(ax_c, badge_x, sy, mi, r=0.20)
            if idx < n - 1:
                ax_c.plot([x+0.15, x+BOX-0.15], [sy - slot_h/2, sy - slot_h/2],
                          color='#AAAAAA', lw=0.6, zorder=4)

# 矢印（正式な相関図の向き）
draw_arrow(ax_c, (0,2), (1,2))   # 藍→紫
draw_arrow(ax_c, (1,2), (2,2))   # 紫→白
draw_arrow(ax_c, (1,1), (0,1))   # 黒→青
draw_arrow(ax_c, (1,1), (2,1))   # 黒→赤
draw_arrow(ax_c, (0,0), (1,0))   # 緑→黄
draw_arrow(ax_c, (1,0), (2,0))   # 黄→橙
draw_arrow(ax_c, (0,0), (0,1))   # 緑→青
draw_arrow(ax_c, (0,1), (0,2))   # 青→藍
draw_arrow(ax_c, (2,0), (2,1))   # 橙→赤
draw_arrow(ax_c, (2,1), (2,2))   # 赤→白
draw_arrow(ax_c, (1,1), (1,2))   # 黒→紫（上）
draw_arrow(ax_c, (1,1), (1,0))   # 黒→黄（下）
draw_arrow(ax_c, (1,1), (0,2))   # 黒→藍（↖）
draw_arrow(ax_c, (1,1), (2,2))   # 黒→白（↗）
draw_arrow(ax_c, (1,1), (0,0))   # 黒→緑（↙）
draw_arrow(ax_c, (1,1), (2,0))   # 黒→橙（↘）

# 右: アクティビティレベル
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

avg_y = 4.2
ax_a.axhline(y=avg_y, xmin=0.3, xmax=0.75, color='#999999', linestyle='--', linewidth=1.2)
ax_a.text(8.8, avg_y + 0.15, f'平均\n{AVERAGE:,}', ha='center',
          va='bottom', fontsize=6.5, color='#888888')

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
        if abs(yp - existing_yp) < 0.55:
            yp = existing_yp + 0.60
    y_positions[m['id']] = yp

for m in MEMBERS:
    yp = y_positions[m['id']]
    ax_a.plot([3.5, 6.5], [yp, yp], color='#CCCCCC', lw=0.8, zorder=2)
    member_badge(ax_a, 5.0, yp, m, r=0.32)
    ax_a.text(3.2, yp, f"{m['activity']:,}", ha='right', va='center',
              fontsize=6.5, color='#333333')
    ax_a.text(6.8, yp, f"{m['id']}　{m['activity_type']}",
              ha='left', va='center', fontsize=6.5, color='#333333')

# 凡例
legend_text = '　'.join([f"{m['id']}（{m['nine']}）" for m in MEMBERS])
fig1.text(0.54, 0.03, legend_text,
          fontsize=7, ha='left', va='bottom', color='#555555',
          bbox=dict(boxstyle='round', facecolor='#F5F5F5', alpha=0.8))

# ========================
# PAGE 2: 思考パターン・意思決定マップ
# ========================
fig2 = plt.figure(figsize=(16, 10))
fig2.patch.set_facecolor('#FFFFFF')
fig2.suptitle('杉山耕一税理士事務所　思考パターン・意思決定マップ（12名版）',
              fontsize=16, fontweight='bold', y=0.98)

ax_th = fig2.add_axes([0.06, 0.60, 0.88, 0.34])
ax_th.set_xlim(-0.5, 5.5)
ax_th.set_ylim(-2.5, 1.5)
ax_th.axis('off')
ax_th.text(-0.4, 1.3, '思考型', fontsize=13, fontweight='bold', color='#E67E22')
ax_th.annotate('', xy=(5.4, 0), xytext=(-0.4, 0),
               arrowprops=dict(arrowstyle='<->', color='#B8860B', lw=2.5, mutation_scale=16))
types = ['精神型', '過去型', '現在型', '未来型', '直観', '創造']
for i, t in enumerate(types):
    ax_th.text(i, 0.25, t, ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax_th.plot(i, 0, 'k|', markersize=12, markeredgewidth=1.5)
ax_th.text(-0.4, -0.5, 'リスクマネジメント\n的存在', ha='center', va='top', fontsize=8, color='#555555')
ax_th.text(5.4, -0.5, '改革的\n存在', ha='center', va='top', fontsize=8, color='#555555')

thought_groups = {}
for m in MEMBERS:
    thought_groups.setdefault(round(m['thought_pos'], 1), []).append(m)
for pos, group in thought_groups.items():
    for i, m in enumerate(group):
        badge_y = -0.7 - i * 0.65
        member_badge(ax_th, pos, badge_y, m, r=0.28)
        ax_th.text(pos, badge_y - 0.35, m['id'],
                   ha='center', va='top', fontsize=6, fontweight='bold', color='#333333')

ax_sp = fig2.add_axes([0.06, 0.24, 0.88, 0.32])
ax_sp.set_xlim(-0.5, 10.5)
ax_sp.set_ylim(-2.5, 1.5)
ax_sp.axis('off')
ax_sp.text(-0.4, 1.3, '気持ちの決定速度（Tempo）', fontsize=13, fontweight='bold', color='#E67E22')
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
        badge_y = -0.7 - i * 0.65
        member_badge(ax_sp, pos, badge_y, m, r=0.28)
        ax_sp.text(pos, badge_y - 0.35, m['id'],
                   ha='center', va='top', fontsize=6, fontweight='bold', color='#333333')

ax_sk = fig2.add_axes([0.06, 0.03, 0.88, 0.19])
ax_sk.set_xlim(10, 100)
ax_sk.set_ylim(-1.8, 1.4)
ax_sk.axis('off')
ax_sk.text(55, 1.3, 'シンキングパターン　pattern of thinking',
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
        member_badge(ax_sk, sc, badge_y, m, r=0.26)
        ax_sk.text(sc, badge_y - 0.32, f"{m['id']}{sc}",
                   ha='center', va='top', fontsize=6, color='#333333')

# 凡例
legend_text = '　'.join([f"{m['id']}（{m['nine']}）" for m in MEMBERS])
fig2.text(0.5, 0.01, legend_text,
          fontsize=7, ha='center', va='bottom', color='#555555',
          bbox=dict(boxstyle='round', facecolor='#F5F5F5', alpha=0.8))

# ========================
# PAGE 3: 役割マッピング（12名・4列×3行）
# ========================

MAPPING_MEMBERS = [
    # 行1（杉山先生が左上トップ）
    {
        'full': '杉山 耕一　所長', 'role_title': '開拓・成長推進・経営判断役',
        'sub': '黄・創（未来型）　Tempo 6.8　活動量：11億',
        'color_h': '#F9A825', 'color_bg': '#FFFDE7', 'color_edge': '#F57F17',
        'text_color': '#333333',
        'fit': ['未来志向の経営判断・新市場開拓',
                '楽しい場の創出・チームの活気づけ',
                '衝動的意思決定力を活かした即断即決業務'],
        'point': ['未来型→「これからこうなります」で伝える',
                  '両方57→数字＋感情エピソードのセットで届く',
                  '旅（飽き性）→毎回新しい視点を加える工夫を',
                  '体験・衝動型→良い話はその場で提案する'],
    },
    {
        'full': '佐々木 麻衣', 'role_title': '品質保証・過去データ参照役',
        'sub': '白・空（過去型）　Tempo 4.3　活動量：109M',
        'color_h': '#757575', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': ['過去データを活用した業務・前例確認',
                '慎重な確認・見直し・コツコツ継続業務',
                '甲状腺傾向→疲れが出やすい時期を先読み'],
        'point': ['過去型→「前回こうでした」が最大の判断軸',
                  '宙の芯→決めたらブレない（コミットで動く）',
                  '白→環境の影響大（良い環境を意識的に選ぶ）',
                  '疲労は体のサイン・自分を責めない'],
    },
    {
        'full': '王 宝梁', 'role_title': '専門知識・情報収集役',
        'sub': '藍・創（現在型）　Tempo 5.0　活動量：56M',
        'color_h': '#283593', 'color_bg': '#E8EAF6', 'color_edge': '#1A237E',
        'text_color': 'white',
        'fit': ['専門知識の深掘り・調査・データ収集',
                '税務専門分野の精度の高い実務',
                '丁寧・慎重な確認業務'],
        'point': ['思考型→情報が揃ってから動く（急かさない）',
                  '現在型→今に集中させると力を発揮',
                  '陽（真面目・バカができない）→定期的な息抜きを',
                  'カフェイン見直しがパフォーマンスの鍵'],
    },
    {
        'full': '梅田 和', 'role_title': 'ムードメーカー・楽しさ発見役',
        'sub': '黄・長（現在型）　Tempo 5.2　活動量：8.7M',
        'color_h': '#F9A825', 'color_bg': '#FFFDE7', 'color_edge': '#F57F17',
        'text_color': '#333333',
        'fit': ['楽しい雰囲気づくり・クライアント対応',
                '何でも楽しいところを見つける強み発揮',
                '継続力を活かした日常の定型業務'],
        'point': ['現在型→「今これが楽しい」が届く入口',
                  '思考型→情報を充分に与えてから動かす',
                  '長+炎→安定時の行動力と崩れリスクに注意',
                  '自己認識と実態のギャップを意識して関わる'],
    },
    # 行2
    {
        'full': '富永 春菜', 'role_title': '技術・専門実行役',
        'sub': '緑・匠（現在型）　Tempo 5.4　活動量：20M',
        'color_h': '#2E7D32', 'color_bg': '#E8F5E9', 'color_edge': '#1B5E20',
        'text_color': 'white',
        'fit': ['慎重な専門作業・技術業務',
                '一人で深く掘り下げる集中業務',
                '変化と多様性のある業務（飽き性防止）'],
        'point': ['フィーリング×現在型→今の感覚で届ける',
                  '超低アクティビティ→情報→イメージ→行動の順',
                  '旅（飽き性）→変化・新しさを取り入れる工夫を',
                  '心理状態が課題→自己受容サポートを優先'],
    },
    {
        'full': '松崎 幸', 'role_title': '計画立案・安定実行役',
        'sub': '青・長（未来型）　Tempo 6.2　活動量：1.17B',
        'color_h': '#1565C0', 'color_bg': '#E3F2FD', 'color_edge': '#0D47A1',
        'text_color': 'white',
        'fit': ['計画を立てて着実に進める業務',
                '仕組みづくり・戦略構築・数字管理',
                '社会・会社のために動く大きなビジョン業務'],
        'point': ['誠タイプ→70%見えてから動く・先に勝算を見せる',
                  '「社会のために・世界のために」で力が湧く',
                  '計画の意義を伝えてから依頼する',
                  '家族優先の働き方・過負荷に注意'],
    },
    {
        'full': '楠本 耕大', 'role_title': '人との橋渡し・現場調整役',
        'sub': '赤・公（現在型）　Tempo 5.3　活動量：190M',
        'color_h': '#C62828', 'color_bg': '#FFEBEE', 'color_edge': '#B71C1C',
        'text_color': 'white',
        'fit': ['クライアント対応・場の空気づくり',
                '現場調整・コミュニケーション担当',
                '人を笑わせる・場を明るくする本来の強み'],
        'point': ['礼タイプ→「一緒に・みんなで」で響く',
                  'シンキング28→空気読んでロジカルに説明',
                  '試験優先中のため自己ケアが最下位（要注意）',
                  '「わーい」で気持ちを高めてから動かす'],
    },
    {
        'full': '中尾 玲沙', 'role_title': '全体把握・組織仲介役',
        'sub': '黒・王（現在型）　Tempo 5.4　活動量：127M',
        'color_h': '#212121', 'color_bg': '#F5F5F5', 'color_edge': '#000000',
        'text_color': 'white',
        'fit': ['チーム全体を見渡す・仲介・情報共有',
                '粘り強い業務・忍耐力が必要な対応',
                '大学院+仕事の二重生活から培った忍耐'],
        'point': ['礼タイプ→「みんなで・一緒に」で響く',
                  '黒→白黒ハッキリ・曖昧な状況がストレス源',
                  '疲れ→血尿パターンあり（疲労サインに注意）',
                  '「わーい」を口癖に・勉強の区切りに活用'],
    },
    # 行3
    {
        'full': '澤田 香織', 'role_title': '精度管理・論理分析役',
        'sub': '赤・守（過去型）　Tempo 4.8　活動量：79M',
        'color_h': '#C62828', 'color_bg': '#FFEBEE', 'color_edge': '#B71C1C',
        'text_color': 'white',
        'fit': ['過去データに基づく分析・精度確認業務',
                'ロジカルな問題解決・根拠を示す提案',
                '感情を表現できる場での強み発揮'],
        'point': ['ロジカル91→論理・根拠・データで伝える',
                  '過去型→実績・前例を示してから提案する',
                  '赤→感情表現できる場が開運ポイント',
                  'Tempo4.8（速め）→待ちや曖昧に注意'],
    },
    {
        'full': '太田 毅', 'role_title': '開拓・新規創造役',
        'sub': '藍・長（創造型）　Tempo 8.6　活動量：45億',
        'color_h': '#283593', 'color_bg': '#E8EAF6', 'color_edge': '#1A237E',
        'text_color': 'white',
        'fit': ['新しいことを切り開く・企画立案',
                'クリエイティブ・直感で動く速決業務',
                '既存の枠にとらわれない発想'],
        'point': ['創造型→まだない未来への関心・改革的存在',
                  'アクティビティ超高→衝動的・方向性を先に定める',
                  'Tempo8.6→決断が早い・相手を待てない面も',
                  '宙→一度決めたら揺るがない信念を尊重'],
    },
    {
        'full': '塩澤 裕己永', 'role_title': '先読み・課題発見役',
        'sub': '白・智（未来型）　Tempo 6.4　活動量：1.19B',
        'color_h': '#757575', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': ['将来リスクの先読み・課題発見',
                'データ分析・ロジカル思考が必要な業務',
                '高いアクティビティを活かした推進役'],
        'point': ['完全ロジカル99→事実・データで伝える',
                  '未来型→「これからどうなるか」で伝える',
                  '感情は内側で素直→体調サインを見逃さない',
                  '1日5分の副交感神経時間（推し活）が最優先'],
    },
    {
        'full': '石渡 美紀', 'role_title': '仲間サポート・対外説明役',
        'sub': '青・勇（思考テンポ早め）　活動量：高め',
        'color_h': '#1565C0', 'color_bg': '#E3F2FD', 'color_edge': '#0D47A1',
        'text_color': 'white',
        'fit': ['外に出る仕事・人への説明・プレゼン',
                '表舞台系の仕事（本来の才能）',
                '家族・仲間のために動くチームサポート'],
        'point': ['勇タイプ→「家族・仲間のために」で動く',
                  '計画は心配対策として立てる→意義を先に伝える',
                  '感情は内側→独り言で感情を出す練習を',
                  '睡眠改善が最優先（子供の咳パターン解消）'],
    },
]

fig3 = plt.figure(figsize=(16, 11))
fig3.patch.set_facecolor('#F7F8FC')

header = FancyBboxPatch((0.01, 0.93), 0.98, 0.065,
                         boxstyle='round,pad=0.005',
                         facecolor='#3949AB', edgecolor='none',
                         transform=fig3.transFigure, zorder=5)
fig3.add_artist(header)
fig3.text(0.5, 0.962, '適材適所　各メンバーの役割マッピング（12名）',
         ha='center', va='center', fontsize=15, fontweight='bold',
         color='white', transform=fig3.transFigure, zorder=6)
fig3.text(0.5, 0.938, 'LifeProfiling® から導く「最も力を発揮できる役割と関わり方のポイント」',
         ha='center', va='center', fontsize=8.5, color='#C5CAE9',
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
    ax.add_patch(FancyBboxPatch((0.02, 0.79), 0.96, 0.19,
                                boxstyle='round,pad=0.01',
                                facecolor=member['color_h'], edgecolor='none'))
    ax.text(0.50, 0.920, member['full'], ha='center', va='center',
            fontsize=11, fontweight='bold', color=member['text_color'])
    ax.text(0.50, 0.832, member['role_title'], ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=member['text_color'])
    ax.text(0.50, 0.752, member['sub'], ha='center', va='center',
            fontsize=6.5, color='#555555')
    ax.plot([0.05, 0.95], [0.725, 0.725], color=member['color_edge'],
            linewidth=0.8, alpha=0.5)
    ax.text(0.06, 0.700, '■ 向いている仕事：', ha='left', va='center',
            fontsize=7.5, fontweight='bold', color=member['color_h'])
    y = 0.655
    for line in member['fit']:
        ax.text(0.08, y, f'・{line}', ha='left', va='center',
                fontsize=6.8, color='#333333')
        y -= 0.068
    ax.plot([0.05, 0.95], [y + 0.02, y + 0.02], color=member['color_edge'],
            linewidth=0.8, alpha=0.3)
    y -= 0.040
    ax.text(0.06, y, '■ 関わり方のポイント：', ha='left', va='center',
            fontsize=7.5, fontweight='bold', color=member['color_h'])
    y -= 0.052
    for line in member['point']:
        ax.text(0.08, y, f'・{line}', ha='left', va='center',
                fontsize=6.5, color='#333333')
        y -= 0.062

# レイアウト: 4列 × 3行（杉山先生が行1左上トップ）
card_w  = 0.228
card_h  = 0.270
gap_x   = 0.015
gap_y   = 0.020
left0   = 0.015
top_row = 0.655  # 行1の下端

# 行1: 4名（杉山先生が左上）
for i, m in enumerate(MAPPING_MEMBERS[:4]):
    l = left0 + i * (card_w + gap_x)
    draw_card(fig3, l, top_row, card_w, card_h, m)

# 行2: 4名
mid_row = top_row - card_h - gap_y
for i, m in enumerate(MAPPING_MEMBERS[4:8]):
    l = left0 + i * (card_w + gap_x)
    draw_card(fig3, l, mid_row, card_w, card_h, m)

# 行3: 4名
bot_row = mid_row - card_h - gap_y
for i, m in enumerate(MAPPING_MEMBERS[8:]):
    l = left0 + i * (card_w + gap_x)
    draw_card(fig3, l, bot_row, card_w, card_h, m)

fig3.text(0.5, 0.015,
         '杉山耕一税理士事務所　│　海音〜心体の調律〜　髙橋由香　2026年5月',
         ha='center', va='center', fontsize=8, color='#777777',
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
