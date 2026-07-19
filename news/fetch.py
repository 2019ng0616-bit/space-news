import feedparser

from config import MAX_ARTICLES
from news.summarizer import analyze_article


RSS_FEEDS = {
    "NASA": "https://www.nasa.gov/news-release/feed/",
    "JAXA": "https://global.jaxa.jp/press/rss.xml",
    "ESA": "https://www.esa.int/rssfeed/Our_Activities/Space_Engineering_Technology",
    "SpaceNews": "https://spacenews.com/feed/",
}


def fetch_feed(source, url):

    feed = feedparser.parse(url)

    articles = []

    entries = feed.entries[:MAX_ARTICLES]

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

        articles.append({
            "source": source,
            "title": title,
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": analysis["summary"],
            "score": analysis["score"]
        })

    return articles


def fetch_all_feeds():

    all_articles = []

    for source, url in RSS_FEEDS.items():

        print(f"Fetching {source}...")

        all_articles.extend(fetch_feed(source, url))

    return all_articles