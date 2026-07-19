import feedparser

from config import MAX_ARTICLES
from news.config_loader import load_rss_sources
from news.summarizer import analyze_article


RSS_FEEDS = load_rss_sources()


def fetch_feed(source, url):

    print(f"Connecting -> {source}")

    feed = feedparser.parse(url)

    if feed.bozo:
        print(f"[WARNING] {source}: RSS parse error")
        print(feed.bozo_exception)

    entries = feed.entries[:MAX_ARTICLES]

    print(f"{source}: {len(entries)} article(s)")

    articles = []

    for i, entry in enumerate(entries, start=1):

        print(f"[{source}] {i}/{len(entries)}")

        title = entry.get("title", "")
        summary_text = entry.get("summary", "")

        content = f"""
Title:
{title}

Summary:
{summary_text}
"""

        analysis = analyze_article(content)

        articles.append(
            {
                "source": source,
                "title": title,
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": analysis["summary"],
                "score": analysis["score"],
            }
        )

    return articles


def fetch_all_feeds():

    all_articles = []

    for rss in RSS_FEEDS:

        try:

            source = rss["name"]
            url = rss["url"]

            articles = fetch_feed(source, url)

            all_articles.extend(articles)

        except Exception as e:

            print("=" * 50)
            print(f"[ERROR] {source}")
            print(e)
            print("=" * 50)

    print()
    print(f"Total Articles : {len(all_articles)}")

    return all_articles