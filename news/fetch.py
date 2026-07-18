import feedparser

RSS_FEEDS = {
    "NASA": "https://www.nasa.gov/news-release/feed/",
    "JAXA": "https://global.jaxa.jp/press/rss.xml",
    "ESA": "https://www.esa.int/rssfeed/Our_Activities/Space_Engineering_Technology",
    "SpaceNews": "https://spacenews.com/feed/",
}


def fetch_feed(source, url):
    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries:
        articles.append({
            "source": source,
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", "")
        })

    return articles


def fetch_all_feeds():
    all_articles = []

    for source, url in RSS_FEEDS.items():
        all_articles.extend(fetch_feed(source, url))

    return all_articles