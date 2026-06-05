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
3. **けんけんからのお手紙フォルダを確認する**
   - フォルダ: `C:\Users\y-takahashi\LLC株式会社\企業のオンライン保健室のコーチのページ - letter`
   - `letter_to_yucchi_` で始まるファイルが未読の手紙
   - 「けんけんからお手紙が○通来ています。開けますか？」と由香さんに確認してから開ける
4. **`MyBrain/タスク管理.md` を読んで未完了タスクを把握・報告する**
5. If files exist in `00_Inbox/`, sort them and report
6. Read the latest conversation log from `10_Journal/`
7. Resume naturally from the previous session

## Session End

When user says "done!" or equivalent:
- Commit & push all uncommitted changes
- Save conversation log to `10_Journal/YYYY-MM-DD_conversation.md` and push

## セッション文字起こしを渡された時のルール（絶対に守る）

文字起こし（テキストファイル・貼り付け問わず）を受け取ったら、必ずこの順番で動く：

1. **①②③の型で分析・まとめを作成する**
   - ① クライアントに渡すセッションまとめ
   - ② アプリ入力用記録（会話要約・所見・次回へのコメント）
   - ③ 髙橋由香へのアドバイス
2. **由香さんに内容を見せて確認を取る** — 必ず表示して「修正はありますか？」と聞く
3. **確認と同時にファイル保存・ランチャー更新を実行する** — OKでも修正指示でも一旦保存する。修正があれば後で上書き。

---

## セッションまとめ作成後の必須3ステップ（絶対に省略しない）

どんな案件でも、セッション記録・まとめ・カルテ・資料を作成したら、必ずこの順番で完了させる：

1. **ファイル保存** — MyBrain内の該当フォルダに保存する（デスクトップ禁止）
   - 個人クライアント（鹿山美弥子・髙橋慎哉・北原要治・林ようこ等）→ `海音_心体の調律/個人クライアント/{氏名}/{氏名}_カルテ.md` に追記
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

## 月次報告書の作成ルール（絶対に守る）

企業のオンライン保健室の月次報告書は、**必ずWord形式（.docx）で作成する**。Markdownの.mdファイルで出力しない。

### 報告書の構成（サステナ・クラウドパワーと同じ定型フォーマット）

1. **タイトル行**：`企業のオンライン保健室　月次報告書`（太字・14pt）
2. **情報テーブル**（3行×4列・Table Grid）
   - 行1：会社名（列2〜4をマージ）
   - 行2：報告年月日 ／ 対象月
   - 行3：報告者 ／ 月テーマ
3. **【総評】**（太字見出し）＋ 本文
4. **【個別セッションの状況】**（太字見出し）＋ 表（氏名・受診日・現状・課題）
5. **【全体傾向と提言】**（太字見出し）＋ 本文
6. **以上**

### 作成方法

Pythonスクリプト（python-docx）で作成する。テンプレートは：
`MyBrain\20_Projects\企業のオンライン保健室\株式会社サステナ\02_報告会記録\サステナ様_2026年4月_月次報告書.docx`

作成スクリプトの参考：
`MyBrain\create_sugiyama_report.py`

### 保存先

`MyBrain\20_Projects\企業のオンライン保健室\{会社名}\02_報告会記録\{会社名}_{年月}_月次報告書.docx`

---

## Guidelines

- Structure messy notes into bullet points / Markdown
- Mark uncertain information as "needs verification"
- Respond in Japanese
