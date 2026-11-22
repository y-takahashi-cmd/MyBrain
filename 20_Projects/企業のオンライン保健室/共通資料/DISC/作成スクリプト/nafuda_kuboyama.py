r"""久保山侑斗さんのトリセツ名札。元データ：Downloads\shinshiki01_rInthQ8vmwZMa6h7oDpijFZxDLD21731320832.pdf（プロファイリング 2024-11-11作成）。2026-11-22作成。"""
from nafuda_core import build

OUT = r"C:\Users\y-takahashi\MyBrain\20_Projects\企業のオンライン保健室\共通資料\DISC\久保山侑斗_トリセツ名札_v0.1.pptx"

# (氏名, パワーカラー, 色の説明, 深層心理, アクティビティレベル, シンキングパターン, ひとこと（仮）, ラッキーナンバー)
PEOPLE = [
    ("久保山 侑斗", "黒", "クールに見える・白黒ハッキリ・やると決めたら率先", "炎", 46146240, 32,
     "クールに見えて、中は熱いです。\n考える時間をもらえると、しっかり動けます！", 5),
]

# 利き脳：礼＝つなぐ（2026-11-22 由香さん判定）
KIKINOU = {"久保山 侑斗": (1, 1)}

if __name__ == "__main__":
    print(build(OUT, PEOPLE, KIKINOU))
