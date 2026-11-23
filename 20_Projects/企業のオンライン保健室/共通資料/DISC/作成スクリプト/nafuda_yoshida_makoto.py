r"""吉田誠さんのトリセツ名札。元データ：Downloads\shinshiki01_rInthQ8vmwZMa6h7oDpijFZxDLD21731657380.pdf（プロファイリング）。2026-11-22作成。"""
from nafuda_core import build

OUT = r"C:\Users\y-takahashi\MyBrain\20_Projects\BNI_REALIZE\121記録\吉田誠_トリセツ名札_v0.1.pptx"

# (氏名, パワーカラー, 色の説明, 深層心理, アクティビティレベル, シンキングパターン, ひとこと（仮）, ラッキーナンバー)
PEOPLE = [
    ("吉田 誠", "藍", "センスの良さ・美的感覚が高い・器用", "宙", 1454305745, 78,
     "思いついたら、すぐ動きたくなります。\n気持ちを込めて話してもらえると響きます！", 8),
]

# 利き脳：勇＝切りひらく（2026-11-22 由香さん判定）
KIKINOU = {"吉田 誠": (0, 0)}

if __name__ == "__main__":
    print(build(OUT, PEOPLE, KIKINOU))
