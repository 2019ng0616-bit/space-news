import feedparser

from news.summarizer import summarize_article


RSS_FEEDS = {
    "NASA": "https://www.nasa.gov/news-release/feed/",
    "JAXA": "https://global.jaxa.jp/press/rss.xml",
    "ESA": "https://www.esa.int/rssfeed/Our_Activities/Space_Engineering_Technology",
    "SpaceNews": "https://spacenews.com/feed/",
}


def fetch_feed(source, url):

    feed = feedparser.parse(url)

    articles = []

    # 開発中は3件だけ
    entries = feed.entries[:3]

    for i, entry in enumerate(entries, start=1):

        print(f"[{source}] {i}/{len(entries)}")

        title = entry.get("title", "")

        summary = summarize_article(title)

        articles.append({
            "source": source,
            "title": title,
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": summary
        })

    return articles


def fetch_all_feeds():

    all_articles = []

    for source, url in RSS_FEEDS.items():

        print(f"Fetching {source}...")

        all_articles.extend(fetch_feed(source, url))

    return all_articles