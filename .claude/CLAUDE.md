# CLAUDE.md 窶・Second Brain

## About
This repo is my "Second Brain".
Claude Code should act as a thinking partner.

## Folder Structure

| Folder | Purpose |
|---|---|
| 00_Inbox/ | Drop anything here first |
| 10_Journal/ | Daily logs, reflections, conversation logs |
| 20_Projects/ | Active projects |
| 30_Tech_Notes/ | Permanent technical knowledge |
| 99_Archives/ | Completed / old stuff |

## Inbox Rules

| Content | Destination |
|---|---|
| Technical knowledge | 30_Tech_Notes/ |
| Active project related | 20_Projects/ |
| Daily notes / reflections | 10_Journal/ |
| Anything else | 10_Journal/ (temporary) |

## Autonomy

OK to do without asking:
- Create / edit / move / delete files in this repo
- Organize and structure Markdown files
- Git add / commit / push
- Sort 00_Inbox/ contents into appropriate folders

Ask before:
- Any operation outside this repo
- Writing to external services

## Session Start

1. Run `date` to confirm today's date (do not guess)
2. `git pull` to sync latest changes
3. If files exist in `00_Inbox/`, sort them and report
4. Read the latest conversation log from `10_Journal/`
5. Resume naturally from the previous session

## Session End

When user says "done!" or equivalent:
- Commit & push all uncommitted changes
- Save conversation log to `10_Journal/YYYY-MM-DD_conversation.md` and push

## セッションまとめ作成後の必須3ステップ（絶対に省略しない）

どんな案件でも、セッション記録・まとめ・カルテ・資料を作成したら、必ずこの順番で完了させる：

1. **ファイル保存** — MyBrain内の該当フォルダに保存する（デスクトップ禁止）
   - 個人保健室（鹿山美弥子さん等）→ `企業のオンライン保健室/個人_鹿山美弥子/セッションログ/`
   - 企業案件 → 該当会社フォルダの適切なサブフォルダ
2. **ランチャー更新** — `C:\Users\y-takahashi\Desktop\由香個人用\work-launcher.json` の該当セクションのlinksに追記する
3. **報告** — 「保存しました・ランチャーに追加しました」と由香さんに伝える

「まとめを作った」だけでは作業完了ではない。ファイル保存とランチャー更新まで終えて初めて完了。

**Why:** 由香さんがランチャーからファイルを開いて企業のオンライン保健室アプリに添付する運用のため。ファイルが迷子になると毎回渡し直しになる。

---

## 作業開始前の必須ルール（約束事項）

**どんな作業でも、始める前に関連ファイルをすべて読む。読み終わるまで質問しない。**

- 企業名・人名が出たら → そのカルテ・報告書フォルダのファイルを全部・最後まで読む
- 「作業をやるよ」と伝えられたら → まずファイルを読む、推測で動かない
- ファイルに情報がある限り、由香さんに聞かない
- サステナの場合：`01_メンバーカルテ/` と `02_報告会記録/` を全部読んでから動く

これは由香さんとの約束事項。破った場合は時間と信頼を無駄にする。

## Guidelines

- Structure messy notes into bullet points / Markdown
- Mark uncertain information as "needs verification"
- Respond in Japanese
