# AndroidからWindows PC（けんけん）にSSH接続する手順

作成：2026-05-01（けんけんからの手紙より）

## 全体像

```
[Android] ─Tailscale─→ [Windows PC] ─OpenSSH─→ PowerShell 7 → claude（けんけん）
```

---

## STEP 1：Tailscale をインストール

1. **Google Play ストア** で「Tailscale」を検索してインストール
   - 公式： https://play.google.com/store/apps/details?id=com.tailscale.ipn
2. アプリを起動して「Get Started」
3. **「Sign in with Microsoft」** を選択 → `y-takahashi@soumubucho-f.com` でログイン
   - もし「Sign in with Google」しか押せないUIだったら、画面下の「Other」や「Use SSO」から進む
   - tailnet選択画面で **`soumubucho-f.com`** を選ぶ
4. 「**Connect**」ボタンを押す
5. 初回だけAndroid OSが「**VPN接続のリクエスト**」ダイアログを出すので **「OK / 許可」**
6. アプリ上で「Connected」になったら、「Machines」タブで `desktop-346v8dr` が見えていればOK

---

## STEP 2：SSHクライアントを入れる（Termius）

1. Google Play ストアで **「Termius」** を検索してインストール
2. 起動 → アカウント作成 or ログイン
   - iPhoneでTermius使ってるなら、**同じアカウントでログイン**するとホスト情報が同期される

---

## STEP 3：Windows PC への接続を登録

iPhoneと同期されてれば既に出てくるはず。出てこない場合は新規追加：

1. Termius右下の「**+**」 → 「**New Host**」
2. 以下を入力：

   | 項目 | 値 |
   |---|---|
   | Label（任意） | `けんけんWindows` |
   | Hostname or IP | `100.65.226.80` |
   | Port | `22` |
   | Username | Windowsのユーザー名（例：`y-takahashi`） |
   | Password | Windowsログインパスワード |

3. 「**Save**」（Android版は右上のチェックマーク✓の場合あり）

---

## STEP 4：接続してけんけんを呼ぶ

1. ホスト一覧で `けんけんWindows` をタップ
2. 初回は「The authenticity of host '100.65.226.80' can't be established」→ **「Yes / Continue」**
3. パスワードを入力
4. PowerShell 7 のプロンプトが出たら接続成功
5. `claude` と打てばけんけん起動

---

## ハマったときのチェックリスト

| 症状 | 対処 |
|---|---|
| 「Connection refused」 | Windows PC が起動してるか・Tailscale が「Connected」か確認 |
| 「Connection timeout」 | Android側のTailscaleが Connected か／VPN許可してるか確認 |
| パスワードが通らない | Windowsのサインインアカウント名で入力（メアド形式の場合あり） |
| `claude` コマンドが見つからない | Windows側のPATH問題。けんけん（大関）に連絡 |
| Tailscaleが頻繁に切れる | Android設定 → アプリ → Tailscale → **「バッテリー最適化を無効化」** |

> **重要**：AndroidのバッテリーはTailscaleを殺すことがある。「最適化なし（制限なし）」設定にしておくと安定する。

---

## iPhoneとの違いまとめ

| 項目 | iPhone | Android |
|---|---|---|
| Tailscaleストア | App Store | Google Play |
| VPN許可ダイアログ | iOS設定→VPN許可 | OSダイアログでOK押すだけ |
| バックグラウンド動作 | 安定 | バッテリー最適化を切る必要あり |
| Termius | 同じ操作 | 同じ操作（アカウント同期可） |
