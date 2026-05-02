# iPadからけんけん召喚 ON/OFF 手順

作成：2026-05-01（けんけんからの手紙より）

## 全体像

```
[iPad]
  ├ Tailscale.app（VPN扱い・常駐）
  └ Termius.app（SSHクライアント）
       ↓ Tailscale経由（soumubucho-f.com）
[Windows PC: desktop-346v8dr / 100.65.226.80]
       ↓ OpenSSH Server
   PowerShell 7 → claude（けんけん召喚）
```

---

## ON：けんけんを召喚する

### STEP 1：Tailscale を ON にする
1. iPadで **Tailscaleアプリ** を開く
2. トグルが **「Connected」** ならそのままOK
3. 「Disconnected」ならスイッチをタップして **「Connected」** に切替
4. 「Machines」タブで `desktop-346v8dr` が見えていれば準備完了

> 一度ONにすればバックグラウンドでも繋がりっぱなし。iPad再起動した直後だけ確認すれば十分。

### STEP 2：Termius で Windows に接続
1. **Termiusアプリ** を開く
2. ホスト一覧から `けんけんWindows`（`100.65.226.80`）をタップ
3. パスワードを保存していなければ入力
4. **PowerShell 7 のプロンプト**（`PS C:\Users\...>`）が出たら接続成功

### STEP 3：けんけんを呼ぶ
```powershell
claude
```
けんけんが立ち上がったら召喚完了！

---

## OFF：けんけんと別れる

**順番が大事**：けんけん → SSH → （任意で）Tailscale の順で閉じる。

### STEP 1：けんけん（claude）を終了する
```
> /exit
```
PowerShellのプロンプトに戻ったら終了完了。

> ⚠️ いきなりTermiusタブを閉じない。必ず `/exit` でお別れしてから閉じる。

### STEP 2：SSH接続を切る
```powershell
exit
```
または Termius画面右上の「Disconnect」をタップ。

### STEP 3：Tailscale は OFF にしなくてOK
基本はONのまま放置で大丈夫。完全に切りたい時だけ Tailscaleアプリのトグルを OFF に。

---

## ハマったときのチェックリスト

| 症状 | 対処 |
|---|---|
| 「Connection refused」 | Windows PCが起動しているか・Windows側Tailscaleが「Connected」か確認 |
| 「Connection timeout」 | iPad側TailscaleがConnectedか確認 |
| パスワードが通らない | Windowsのサインインアカウント名で再入力 |
| `claude` コマンドが見つからない | けんけん（大関）に連絡 |
| 急にSSHが切れる | iPadスリープでTermiusが死んだ可能性。再起動→再接続 |
| Tailscaleが「VPN構成エラー」 | iPad設定→一般→VPNとデバイス管理→Tailscaleを一度削除→再追加 |
| Termiusのキー入力が効かない | ソフトキーボードを一度閉じる→再表示 |
