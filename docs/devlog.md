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

## Issue #10

READMEを全面的に改善。

### 実装

- プロジェクト概要追加
- 技術スタック整理
- ディレクトリ構成追加
- セットアップ手順追加
- Roadmap追加
- ワークフロー図追加

### 学び

READMEは単なる説明ではなく、
プロジェクトの入口となる重要なドキュメントであることを理解した。

## Issue #11

AIによるニュース重要度判定を実装。

### 実装

- score_article()追加
- AIへ重要度判定を依頼
- JSONへscore保存
- Webへ星表示

### 結果

ニュースごとに
★1〜5
の重要度が表示されるようになった。

## Issue #12

AI処理をリファクタリング。

### 実装

- analyze_article()を新規作成
- 要約と重要度判定を1回の推論へ統合
- fetch.pyを更新
- JSON形式の出力へ変更

### 効果

記事1件あたりのLLM呼び出し回数を

2回

↓

1回

へ削減。

### 学び

AIアプリでは
「推論回数」が性能へ大きく影響する。

同じ推論で取得できる情報は
まとめて取得した方が高速かつ保守しやすい。

# Issue #13

## RSS取得基盤の安定化

### 実施内容

- RSS取得例外処理追加
- RSS取得件数ログ追加
- RSS取得状況表示追加
- RSS失敗時も処理継続

### 成果

ニュース取得基盤の堅牢性が向上。

RSS取得失敗時でも
他サイトの記事取得が継続できるようになった。

# Issue #14

## RSS設定の外部化

### 実施内容

- RSS一覧をJSONへ移動
- config_loader追加
- fetch.pyを設定読込方式へ変更

### 成果

RSS追加・削除が
rss_sources.jsonのみで可能となった。

コードを編集せずに
ニュースソースを管理できる構成へ改善した。

# Issue #15

## 記事キャッシュ

### 実施内容

記事URLをキーとして
AI要約結果を保存。

再実行時は
キャッシュを利用するため
Gemmaを呼び出さない。

### 効果

開発速度が大幅向上。

毎朝更新時も
新着記事のみ要約する構成となった。

# Issue #16

## Static HTML Generation

### 実施内容

Jinja2を利用して
news.jsonから静的HTMLを生成する
処理を実装。

Flaskを使用しなくても
ニュース一覧を閲覧できる構成へ変更した。

### 効果

GitHub Pages公開へ向けた
基盤を整備。

# 2026-07-20

## Issue #17
GitHub Pagesでスマホ公開

### 目的

生成した静的HTMLをGitHub Pagesで公開し、
スマートフォンから閲覧できるようにする。

### 実施内容

- docsフォルダへHTML生成
- GitHub Pages設定
- スマホから表示確認

### 結果

Space News AIをインターネット経由で公開できた。

PCだけでなくスマートフォンからも閲覧できることを確認。

### 学んだこと

GitHub Pagesは静的サイトを簡単に公開できる。

PythonやFlaskを常時起動しなくても、
HTMLだけで公開できることを理解した。

# 2026-07-20

## Issue #18
UIをポートフォリオレベルへ改善

### 目的

Space News AIのUIを改善し、
ポートフォリオとして見栄えするデザインへ変更する。

### 実施内容

- ダークテーマ導入
- カードレイアウト採用
- 更新日時表示
- 記事リンクをボタン化
- スコア表示改善
- レスポンシブ対応

### 結果

PC・スマートフォンともに視認性が向上した。

### 学んだこと

機能だけでなく、UI/UXもポートフォリオ評価において重要であることを実感した。