# CLOUDPOWER Palette

クラウドパワー株式会社 公式カラーシステム定義書

- **作成日:** 2026-04-16
- **ベースカラー:** `#74B2E0`（CP Blue）
- **参照元:** デジタル庁ダッシュボードデザインガイド準拠の構成
- **ビジュアルプレビュー:** `90_System/CLOUDPOWER_Palette_v2.html`
- **PPTX テンプレート:** `90_System/クラウドパワーテンプレート_CLOUDPOWER_Palette.pptx`
- **旧テンプレート（併用可）:** `90_System/クラウドパワーテンプレート.pptx`

---

## 1. Primary — CP Blue

| Token | Name | HEX | 用途 |
|---|---|---|---|
| `blue-900` | Blue 900 | `#1A3A5C` | 最濃。ダークモード BG、フッター |
| `blue-800` | Blue 800 | `#245180` | 見出し（ダークモード） |
| `blue-700` | Blue 700 | `#2E6BA6` | Deep Blue。グラデーション起点、リンク |
| `blue-600` | Blue 600 | `#4A8CC4` | ホバー、アクティブ状態 |
| `blue-500` | Blue 500 | `#5A9BC7` | セカンダリ。見出し・強調 |
| **`blue-400`** | **Blue 400 (Primary)** | **`#74B2E0`** | **ブランドカラー。ヘッダー、CTA、アクセント** |
| `blue-300` | Blue 300 | `#A3CDE8` | サブ要素、ダークモードテキスト |
| `blue-200` | Blue 200 | `#C5DDE9` | セパレータ、ボーダー |
| `blue-100` | Blue 100 | `#D6E9F5` | カード BG、テーブルヘッダ BG |
| `blue-50` | Blue 50 | `#F2F8FC` | ページ BG、セクション BG |

---

## 2. Gray Scale

| Token | Name | HEX | 用途 |
|---|---|---|---|
| `gray-900` | Gray 900 | `#1A1A1A` | 最濃テキスト（限定使用） |
| `gray-800` | Gray 800 | `#333333` | 見出しテキスト |
| **`gray-700`** | **Gray 700 (Body)** | **`#4A4A4A`** | **本文テキスト（デフォルト）** |
| `gray-600` | Gray 600 | `#666666` | サブテキスト |
| `gray-500` | Gray 500 | `#888888` | プレースホルダ、無効状態 |
| `gray-400` | Gray 400 | `#AAAAAA` | ボーダー（軽） |
| `gray-300` | Gray 300 | `#CCCCCC` | ディバイダ |
| `gray-200` | Gray 200 | `#E0E0E0` | ボーダー（標準） |
| `gray-100` | Gray 100 | `#F0F0F0` | 交互行 BG |
| `gray-50` | Gray 50 | `#F8F8F8` | ページ BG（ニュートラル） |

---

## 3. Semantic Colors

### Success

| Token | HEX | 用途 |
|---|---|---|
| `success-700` | `#1B7D3A` | ダークテキスト |
| `success-500` | `#28A745` | アイコン、バッジ |
| `success-300` | `#7DD39B` | ライトアクセント |
| `success-50` | `#E6F5EB` | 背景 |

### Warning

| Token | HEX | 用途 |
|---|---|---|
| `warning-700` | `#C68A00` | ダークテキスト |
| `warning-500` | `#F0AD00` | アイコン、バッジ |
| `warning-300` | `#FFD666` | ライトアクセント |
| `warning-50` | `#FFF8E1` | 背景 |

### Error

| Token | HEX | 用途 |
|---|---|---|
| `error-700` | `#B71C1C` | ダークテキスト |
| `error-500` | `#DC3545` | アイコン、バッジ |
| `error-300` | `#F09DA5` | ライトアクセント |
| `error-50` | `#FDEAEA` | 背景 |

### Info

| Token | HEX | 用途 |
|---|---|---|
| `info-700` | `#2E6BA6` | ダークテキスト（= Blue 700） |
| `info-500` | `#74B2E0` | アイコン、バッジ（= Primary） |
| `info-300` | `#A3CDE8` | ライトアクセント（= Blue 300） |
| `info-50` | `#F2F8FC` | 背景（= Blue 50） |

---

## 4. Chart Accent Colors

データ可視化・グラフ用。この順序で使用する。

| # | Name | HEX | PPTX Theme Role |
|---|---|---|---|
| 1 | **CP Blue** | `#74B2E0` | accent1 |
| 2 | **Deep Blue** | `#2E6BA6` | hlink |
| 3 | **Teal** | `#5BBFB5` | accent4 |
| 4 | **Amber** | `#F0AD00` | accent6 |
| 5 | **Sand** | `#D4885C` | accent2 |
| 6 | **Steel** | `#6B8FA3` | accent5 |
| 7 | **Forest** | `#3D8B4A` | accent3 |
| 8 | **Slate** | `#7A98AE` | folHlink |

### 設計方針
- **Sand `#D4885C`**: Error 赤（`#DC3545`）と混同しないよう橙寄りに設計
- **Steel `#6B8FA3`**: CP Blue の延長線上。ブランド世界観を壊さない
- **Forest `#3D8B4A`**: Success 緑（`#28A745`）と距離を確保

---

## 5. Dark Mode

| 要素 | Light | Dark |
|---|---|---|
| ページ BG | `#F2F8FC` | `#0F1B2A` |
| カード BG | `#FFFFFF` | `#1A2940` |
| 見出しテキスト | `#1A3A5C` | `#A3CDE8` |
| 本文テキスト | `#4A4A4A` | `#CCDDEE` |
| サブテキスト | `#666666` | `#8899AA` |
| ヘッダー BG | `#74B2E0` | `linear-gradient(135deg, #1A3A5C, #2E6BA6)` |
| セマンティック | Base（500） | Light（300） |

---

## 6. PPTX Theme Mapping

`クラウドパワーテンプレート_CLOUDPOWER_Palette.pptx` のテーマ定義:

```xml
<a:clrScheme name="CLOUDPOWER Palette">
  <a:dk1><a:sysClr val="windowText"/></a:dk1>     <!-- #000000 -->
  <a:lt1><a:sysClr val="window"/></a:lt1>          <!-- #FFFFFF -->
  <a:dk2><a:srgbClr val="1A3A5C"/></a:dk2>         <!-- Blue 900 -->
  <a:lt2><a:srgbClr val="F2F8FC"/></a:lt2>         <!-- Blue 50 -->
  <a:accent1><a:srgbClr val="74B2E0"/></a:accent1> <!-- CP Blue -->
  <a:accent2><a:srgbClr val="D4885C"/></a:accent2> <!-- Sand -->
  <a:accent3><a:srgbClr val="3D8B4A"/></a:accent3> <!-- Forest -->
  <a:accent4><a:srgbClr val="5BBFB5"/></a:accent4> <!-- Teal -->
  <a:accent5><a:srgbClr val="6B8FA3"/></a:accent5> <!-- Steel -->
  <a:accent6><a:srgbClr val="F0AD00"/></a:accent6> <!-- Amber -->
  <a:hlink><a:srgbClr val="2E6BA6"/></a:hlink>     <!-- Deep Blue -->
  <a:folHlink><a:srgbClr val="7A98AE"/></a:folHlink> <!-- Slate -->
</a:clrScheme>
```

---

## 7. 使い分けガイド

| シーン | 使うテンプレ |
|---|---|
| 既存案件の継続資料 | `クラウドパワーテンプレート.pptx`（従来通り） |
| 新規提案・ダッシュボード系 | `クラウドパワーテンプレート_CLOUDPOWER_Palette.pptx` |
| Web UI / プロダクト | CLOUDPOWER Palette の CSS 変数（TODO: 作成） |
| データ可視化（Power BI 等） | Chart Accent Colors の順序に従う |

---

*CLOUDPOWER Palette — Cloud Power Inc.*
