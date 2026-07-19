## 2026-07-19

### Issue #1

RSSフィード取得

#### Completed

- RSS一覧作成

#### Next

feedparser導入

## Completed

- RSS取得処理を実装
- NASA
- JAXA
- ESA
- SpaceNews
- コンソール表示成功

## Next

取得結果をJSONへ保存する

## Issue #2

### Goal

RSS取得結果をJSONへ保存

### Completed

- save.py作成
- news.json生成
- UTF-8保存確認

### Next

HTMLへ一覧表示

## Issue #3

### Goal

JSONをHTMLへ表示

### Completed

- JSON読込
- Flask導入
- HTML一覧表示
- ブラウザ確認

### Next

UI改善

## Issue #4

### Goal

ニュース画面を改善

### Completed

- CSS追加
- カード表示
- AI Summary欄追加
- レスポンシブ確認

### Next

Ollama要約

## Issue #5-#6

Skip (サブイシューを別で作成し、削除してしまったため)

## Issue #7
AI要約機能を実装。

### 実装内容

- Ollama(Gemma4)との連携
- RSS記事をAIで日本語要約
- news.jsonへsummaryを追加

### 動作確認

NASA・ESA・SpaceNewsの記事について要約生成を確認。

JSON例

```json
{
  "title": "...",
  "summary": "..."
}
```

### 課題

- RSSによっては本文が取得できずタイトルのみになる。
- 将来的には本文取得やキャッシュ機能を追加予定。

### 学び

ローカルLLMをPythonから呼び出す流れを理解できた。

RSS取得 → AI要約 → JSON保存 → Flask表示

という一連のデータフローを構築できた。

## Issue #8

AI要約をFlask画面へ表示。

### 実装

- summary表示
- HTML改行対応
- CSS改善

### 結果

RSS取得からAI要約生成、Web表示まで一連の流れが完成。

Space News AIとして最低限の閲覧機能を実装。

## Issue #9

ニュースを配信元ごとにグループ化して表示する機能を実装。

### 実装内容

- app.pyで記事をsourceごとにグループ化
- Flaskへgrouped_articlesを渡すよう変更
- Jinja2を二重ループへ変更
- 配信元ごとのセクションを追加
- CSSを調整

### 動作確認

- NASA
- JAXA
- ESA
- SpaceNews

ごとに記事がまとまって表示されることを確認。

### 学び

表示用のデータ構造は、
取得したデータとは別にView向けへ整形すると実装しやすい。

Flaskのテンプレートでは
辞書＋二重ループによる描画方法を理解した。