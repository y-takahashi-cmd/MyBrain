# -*- coding: utf-8 -*-
"""
サステナ様 3ページ統合版
Page1: パワーカラー相関図（矢印修正版）+ アクティビティ
Page2: 思考パターン・意思決定マップ
Page3: 適材適所 役割マッピング（三井社長トップ）
"""
import io
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

try:
    import japanize_matplotlib
except ImportError:
    plt.rcParams['font.family'] = ['Yu Gothic', 'MS Gothic', 'Meiryo', 'sans-serif']

plt.rcParams['axes.unicode_minus'] = False

MEMBERS = [
    {'id': 'T', 'name': '樋田', 'nine': '匠',
     'power_color': '黄', 'grid': (1, 0),
     'fc': '#FFD700', 'ec': '#B8860B', 'tc': '#333333',
     'activity': 466_286_780, 'activity_type': '直感型',
     'thought_pos': 2.0, 'speed_pos': 7.5,
     'thinking': 93, 'thinking_type': 'ロジカルタイプ'},
    {'id': 'S', 'name': '佐藤', 'nine': '王',
     'power_color': '赤', 'grid': (2, 1),
     'fc': '#E53935', 'ec': '#B71C1C', 'tc': 'white',
     'activity': 194_706_502, 'activity_type': '思考型',
     'thought_pos': 1.0, 'speed_pos': 7.0,
     'thinking': 46, 'thinking_type': '両方タイプ'},
    {'id': 'A', 'name': '浅野', 'nine': '長',
     'power_color': '白', 'grid': (2, 2),
     'fc': '#F5F5F5', 'ec': '#757575', 'tc': '#333333',
     'activity': 324_465_750, 'activity_type': '直感型',
     'thought_pos': 3.0, 'speed_pos': 2.0,
     'thinking': 36, 'thinking_type': 'フィーリング寄り'},
    {'id': 'M', 'name': '三井', 'nine': '創',
     'power_color': '白', 'grid': (2, 2),
     'fc': '#EEEEEE', 'ec': '#757575', 'tc': '#333333',
     'activity': 139_157_882, 'activity_type': '思考型',
     'thought_pos': 1.0, 'speed_pos': 4.7,
     'thinking': 63, 'thinking_type': '両方タイプ'},
    {'id': 'O', 'name': '大森', 'nine': '王',
     'power_color': '橙', 'grid': (2, 0),
     'fc': '#FF7043', 'ec': '#E64A19', 'tc': 'white',
     'activity': 462_286_440, 'activity_type': '直感型',
     'thought_pos': 3.0, 'speed_pos': 6.1,
     'thinking': 83, 'thinking_type': 'ロジカルタイプ'},
]

AVERAGE = 240_000_000
OUTPUT = r'C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\株式会社サステナ\01_メンバーカルテ\サステナ様_関係図＋役割マッピング.pdf'

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
fig1.suptitle('株式会社サステナ様　可能性から見る関係図（5名版）',
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
    else:
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

# ── 矢印（正式な矢印図に合わせた向き） ──
# 横：上段（藍→紫→白）
draw_arrow(ax_c, (0,2), (1,2))          # 藍→紫
draw_arrow(ax_c, (1,2), (2,2))          # 紫→白
# 横：中段（黒→青、黒→赤）
draw_arrow(ax_c, (1,1), (0,1))          # 黒→青
draw_arrow(ax_c, (1,1), (2,1))          # 黒→赤
# 横：下段（緑→黄→橙）
draw_arrow(ax_c, (0,0), (1,0))          # 緑→黄
draw_arrow(ax_c, (1,0), (2,0))          # 黄→橙
# 縦：左列（緑→青→藍）
draw_arrow(ax_c, (0,0), (0,1))          # 緑→青
draw_arrow(ax_c, (0,1), (0,2))          # 青→藍
# 縦：右列（橙→赤→白）
draw_arrow(ax_c, (2,0), (2,1))          # 橙→赤
draw_arrow(ax_c, (2,1), (2,2))          # 赤→白
# 縦：中央（黒→紫↑、黒→黄↓）
draw_arrow(ax_c, (1,1), (1,2))          # 黒→紫（上）
draw_arrow(ax_c, (1,1), (1,0))          # 黒→黄（下）
# 対角：上（青→紫、赤→紫）
draw_arrow(ax_c, (0,1), (1,2))          # 青→紫（↗）
draw_arrow(ax_c, (2,1), (1,2))          # 赤→紫（↖）
# 対角：下（黒→緑、黒→橙）
draw_arrow(ax_c, (1,1), (0,0))          # 黒→緑（↙）
draw_arrow(ax_c, (1,1), (2,0))          # 黒→橙（↘）

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

avg_y = 4.5
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
          'T：樋田雅史（匠）　S：佐藤洋介（王）　A：浅野航（長）　M：三井康平（創）　O：大森美葉（王）',
          fontsize=8.5, ha='left', va='bottom', color='#555555',
          bbox=dict(boxstyle='round', facecolor='#F5F5F5', alpha=0.8))

# ========================
# PAGE 2: 思考パターン・意思決定マップ
# ========================
fig2 = plt.figure(figsize=(16, 10))
fig2.patch.set_facecolor('#FFFFFF')
fig2.suptitle('株式会社サステナ様　思考パターン・意思決定マップ（5名版）',
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
# PAGE 3: 役割マッピング（三井社長トップ左）
# ========================
MAPPING_MEMBERS = [
    {
        'full': '三井 康平　社長', 'role_title': '黙々集中・独創実行役',
        'sub': '白・創（過去型）　活動量：139M',
        'color_h': '#757575', 'color_bg': '#F5F5F5', 'color_edge': '#424242',
        'text_color': 'white',
        'fit': ['一人で深く掘り下げる専門作業・経営判断',
                '独創的なアイデアの具現化',
                'じっくり考える長期戦略・品質へのこだわり'],
        'point': ['「まっいいか」の放置癖→数値・事実で短く',
                  '過去型→「ずっとこの状態なら」が刺さる',
                  '新習慣より「今の延長」の提案が通りやすい',
                  '右腕・左腕への共有が仕事をはかどらせる'],
    },
    {
        'full': '佐藤 洋介', 'role_title': '意思決定・采配役',
        'sub': '赤・王（過去型）　活動量：194M',
        'color_h': '#E53935', 'color_bg': '#FFEBEE', 'color_edge': '#B71C1C',
        'text_color': 'white',
        'fit': ['経営判断・ビジョン策定・対外交渉',
                '組織采配・クライアント対応',
                '仲間のために動く舵取り'],
        'point': ['過去型×両方タイプ→根拠を示すと動く',
                  '「ありがとう・助かった」が最大の原動力',
                  '府に落ちると一気に動く。感情面も丁寧に',
                  '旅・キャンプ等の一人時間が回復の鍵'],
    },
    {
        'full': '樋田 雅史', 'role_title': '実行・技術推進役',
        'sub': '黄・匠（現在型）　活動量：466M',
        'color_h': '#F9A825', 'color_bg': '#FFFDE7', 'color_edge': '#F57F17',
        'text_color': '#333333',
        'fit': ['システム開発・技術実装・仕組み化',
                '現場での実行・技術課題の解決',
                '人を育てる・後進指導（得意分野）'],
        'point': ['底抜けの明るさがチームを動かす本来の姿',
                  '「楽しい」を先に見せると行動しやすい',
                  'マネジメントより技術・実行者として輝く',
                  '人を育てる・楽しませることに強いパワー'],
    },
    {
        'full': '大森 美葉', 'role_title': 'サポート・品質保証役',
        'sub': '橙・王（未来型）　活動量：462M',
        'color_h': '#FF7043', 'color_bg': '#FBE9E7', 'color_edge': '#BF360C',
        'text_color': 'white',
        'fit': ['品質管理・バックオフィス・マニュアル整備',
                '人のサポート・チームの縁の下の力持ち',
                '計画を立てて丁寧に実行する業務'],
        'point': ['「会社のために・助かりました」が力の源泉',
                  '未来型→「こうなれる」で提案すると届く',
                  'じっくりゆっくり→急かすと逆効果',
                  '褒めること・存在への承認が突破口'],
    },
    {
        'full': '浅野 航', 'role_title': '企画・調整・傾聴役',
        'sub': '白・長（未来型）　活動量：324M',
        'color_h': '#BDBDBD', 'color_bg': '#FAFAFA', 'color_edge': '#757575',
        'text_color': '#222222',
        'fit': ['企画立案・プロジェクト調整・傾聴',
                'きっかけを与える・可能性を引き出す',
                'チームの関係構築・外部との橋渡し'],
        'point': ['仕組み化・自律的な環境づくりが得意',
                  '未来型×フィーリング→ビジョンと感覚で動く',
                  '困ったら人に聞ける・助けを求めるのが得意',
                  '「ながら改善」「思い出した時だけ」が合う'],
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

card_w, card_h, gap = 0.305, 0.415, 0.025
positions_top = [
    (0.025, 0.490),
    (0.025 + card_w + gap, 0.490),
    (0.025 + (card_w + gap) * 2, 0.490),
]
left_bottom = (1.0 - (card_w * 2 + gap)) / 2
positions_bottom = [
    (left_bottom, 0.060),
    (left_bottom + card_w + gap, 0.060),
]
for i, m in enumerate(MAPPING_MEMBERS[:3]):
    draw_card(fig3, *positions_top[i], card_w, card_h, m)
for i, m in enumerate(MAPPING_MEMBERS[3:]):
    draw_card(fig3, *positions_bottom[i], card_w, card_h, m)

fig3.text(0.5, 0.025,
         '株式会社サステナ　　│　　海音〜心体の調律〜　　髙橋由香　　2026年4月',
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
