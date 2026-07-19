from news.fetch import fetch_all_feeds
from news.save import save_to_json
from generate_html import generate_html
from datetime import datetime


def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()
    save_to_json(articles)

    # ---- ダッシュボード用の数字 ----
    total_articles = len(articles)
    total_sources = len(set(a["source"] for a in articles))
    average_score = round(sum(a["score"] for a in articles) / total_articles, 1) if total_articles else 0
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    # ---- TOPストーリー選定 ----
    top_story = None
    if articles:
        top_story = max(articles, key=lambda a: a["score"])

    # ---- HTML生成 ----
    generate_html(
        articles,
        total_articles,
        total_sources,
        average_score,
        updated_at,
        top_story
    )

    print()
    print("GitHub Pages updated.")


if __name__ == "__main__":
    main()
