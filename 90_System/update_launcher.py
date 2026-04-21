"""
Work Launcherのカルテセクションを自動更新するスクリプト。
新しい .md ファイルが追加されたとき、work-launcher.json に自動でリンクを追加する。
git post-commit フックから実行される。
"""
import json
import os
import glob
import random
import string
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

MYBRAIN = "C:/Users/y-takahashi/MyBrain"
LAUNCHER_PATH = MYBRAIN + "/work-launcher.json"

# セクションタイトル → カルテフォルダのマッピング
SECTION_FOLDERS = {
    "👤 クラウドパワー カルテ":
        MYBRAIN + "/20_Projects/企業のオンライン保健室/クラウドパワー株式会社/01_メンバーカルテ",
    "👤 グリットワークス カルテ":
        MYBRAIN + "/20_Projects/企業のオンライン保健室/有限会社グリットワークス/01_メンバーカルテ",
    "👤 杉山耕一税理士事務所 カルテ":
        MYBRAIN + "/20_Projects/企業のオンライン保健室/杉山耕一税理士事務所/01_メンバーカルテ",
    "👤 サステナ カルテ":
        MYBRAIN + "/20_Projects/企業のオンライン保健室/株式会社サステナ/01_メンバーカルテ",
}

def generate_id():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=8)) + '-' + ''.join(random.choices(chars, k=6))

def make_label(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace("さん", "")
    return name

def update_launcher():
    if not os.path.exists(LAUNCHER_PATH):
        print("work-launcher.json が見つかりません")
        return

    with open(LAUNCHER_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed = False

    for section in data.get("localSections", []):
        title = section.get("title", "")
        if title not in SECTION_FOLDERS:
            continue

        folder = SECTION_FOLDERS[title]
        if not os.path.exists(folder):
            continue

        existing_paths = {link["path"] for link in section.get("links", [])}

        for md_file in sorted(glob.glob(os.path.join(folder, "*.md"))):
            # _を含むファイルはセッション記録等の補助ファイルなので除外
            if "_" in os.path.basename(md_file):
                continue
            path = md_file.replace("\\", "/")
            if path not in existing_paths:
                label = make_label(os.path.basename(md_file))
                section["links"].append({
                    "id": generate_id(),
                    "label": label,
                    "path": path
                })
                changed = True
                print(f"追加: [{title}] {label}")

    if changed:
        with open(LAUNCHER_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("work-launcher.json を更新しました")
    else:
        print("変更なし（新しいカルテはありません）")

if __name__ == "__main__":
    update_launcher()
