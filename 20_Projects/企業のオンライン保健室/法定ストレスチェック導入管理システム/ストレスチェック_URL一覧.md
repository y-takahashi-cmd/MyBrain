# 法定ストレスチェック（kokorocare）URL一覧

> 出典：けんけんのお手紙 `letter_to_yucchi_20260824_sc_url_ichiran.md`（2026-08-24）
> 記録日：2026-09-04

**覚え方：練習用は `test` が付いている（`sttest` / `applytest`）。付いていなければ本番。**

- 練習用でやったことは本番にいっさい影響しない
- 練習用のメールは**全部けんけん（大関さん）に届く**。お客様や由香さんには届かない
- 練習用メールは件名の先頭に `[TEST→本来:○○さん]`、本文上部に赤枠「これはテスト環境から送信されています」が付く。**この表示があれば練習用、無ければ本番**

---

## 🧪 練習用（検証環境）

| やりたいこと | URL |
|---|---|
| お客様が仮申込するフォーム | https://applytest.kokorocare.business/apply |
| 料金プランナー（お客様が見る画面） | https://sttest.kokorocare.business/planner |
| 運営としてログイン | https://sttest.kokorocare.business/login/staff |
| 仮申込・本申込の一覧 | https://sttest.kokorocare.business/leads |
| 契約企業の管理 | https://sttest.kokorocare.business/dashboard |
| 企業一覧 | https://sttest.kokorocare.business/companies |
| 担当の先生を割り当てる | https://sttest.kokorocare.business/staff-roles |
| 企業のご担当者が見る画面 | https://sttest.kokorocare.business/admin |

## 🚀 本番用

| やりたいこと | URL |
|---|---|
| お客様が仮申込するフォーム | https://apply.kokorocare.business/apply |
| 料金プランナー（お客様が見る画面） | https://sc.kokorocare.business/planner |
| 運営としてログイン | https://sc.kokorocare.business/login/staff |
| 仮申込・本申込の一覧 | https://sc.kokorocare.business/leads |
| 契約企業の管理 | https://sc.kokorocare.business/dashboard |
| 企業一覧 | https://sc.kokorocare.business/companies |
| 担当の先生を割り当てる | https://sc.kokorocare.business/staff-roles |
| 企業のご担当者が見る画面 | https://sc.kokorocare.business/admin |

---

## ログインの入口（同じアプリ・ログイン場所が違うだけ）

| 誰が | URL | ログイン方法 |
|---|---|---|
| 運営スタッフ（由香さん・沢村さん・システム管理者） | `https://sc.kokorocare.business/login/staff` | Microsoft（Entra）アカウント（例：info@kokorocare.business、ロール：保健室管理者） |
| 企業（お客様）側 | `https://sc.kokorocare.business/login/customer` | メールアドレス・パスワード（例：yuka_777@healing-kanon.com、ロール：企業管理者） |

---

## 申込から契約までの流れ（この順番でお試しする）

1. **お客様が仮申込** … `apply.kokorocare.business/apply`（練習は `applytest`）。会社名・担当者名・メール・電話を入力して送信。ログイン不要。→ お客様に自動返信＋運営（`info@kokorocare.business`）にお知らせが届く
2. **お客様が料金試算して本申込** … `sc.kokorocare.business/planner`。メール入力→6桁の確認コード→人数・プラン選択→年間費用が出て本申込まで進む（最後に「利用規約に同意」チェックが必要）
3. **運営が契約企業にする** … `sc.kokorocare.business/leads` から対象を開いて登録
   - ⚠️ **既に登録がある会社（グリットワークスなど）は「既存のテナントに紐づける」を選ぶ**。「新しく作って招待する」を選ぶと認証システム側と重複してエラー
4. 🔴 **担当の先生を割り当てる** … `sc.kokorocare.business/staff-roles`
   - **契約企業にしただけでは担当の割り当ては自動でつかない**。ここで沢村さん・由香さんにその会社を割り当てる
   - 割り当てを忘れると：先生ログインで会社データが1件も見えない／お客様画面の「担当の先生」が空欄／お客様メールの「運営担当」欄も空
   - system_admin 権限だと全部見えてしまうので、**先生の権限で確認しないと気づけない**
5. **企業のご担当者としてログインして確認** … `sc.kokorocare.business/admin`

---

## 困ったとき

- **フォームが開かない** … 仮申込フォームは `apply` から始まるURLでないと開かない（`sc` では開けない）
- **確認コードが届かない** … 迷惑メールフォルダを確認。練習用の場合はけんけんに届いている
- **データが見えない** … 手順4の割り当てが済んでいない可能性

---

## 2026-08-24 時点であわせて直った／追加されたこと

- 🔴 **本申込ができない不具合を修正**：2026-07-27〜08-23 の約4週間、本番で「本申込」が完了できない状態だった（利用規約に同意してもエラー）。この期間に本申込まで進んだお客様はいなかった。8/23 修正・本番反映済み。「申し込もうとしたらエラーが出た」という問い合わせがあればこの件の可能性
- 企業のご担当者が、事前ヒアリング・実施準備台帳の内容を閲覧できるようになった（閲覧のみ）
- 実施準備の台帳が **19章** になった（髙橋さん作の全20章のうち5〜19章も搭載）。章ごとに開け閉め可。高ストレス者対応・医師面接・保健室面談の章はお客様画面には出ない
