r"""吉田和歩さんのトリセツ名札。元データ：Downloads\shinshiki01_rInthQ8vmwZMa6h7oDpijFZxDLD21730431750.pdf（プロファイリング）。2026-11-22作成。"""
from nafuda_core import build

OUT = r"C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\共通資料\DISC\吉田和歩_トリセツ名札_v0.1.pptx"

# (氏名, パワーカラー, 色の説明, 深層心理, アクティビティレベル, シンキングパターン, ひとこと（仮）, ラッキーナンバー)
PEOPLE = [
    ("吉田 和歩", "橙", "周りを元気にする明るさ・聞き上手・細やかな気遣い", "陽", 148821624, 29,
     "支えるのが得意です。\n先に全体の流れを教えてもらえると、安心して動けます！", 1),
]

# 利き脳：誠＝組み立てる（2026-11-22 由香さん判定）
KIKINOU = {"吉田 和歩": (0, 1)}

if __name__ == "__main__":
    print(build(OUT, PEOPLE, KIKINOU))
