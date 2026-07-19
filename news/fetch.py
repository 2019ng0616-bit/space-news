import requests
import feedparser
from bs4 import BeautifulSoup

from config import MAX_ARTICLES
from news.config_loader import load_rss_sources
from news.summarizer import analyze_article
from news.cache import load_cache, save_cache

RSS_FEEDS = load_rss_sources()


# ============================================================
# JAXA fallback（HTMLスクレイピング）
# ============================================================
def fetch_html_fallback(source, url):
    print(f"[{source}] HTML fallback mode (RSS broken)")

    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []

    for item in soup.select(".pressList li"):
        a = item.select_one("a")
        if not a:
            continue

        title = a.get_text(strip=True)
        link = "https://www.jaxa.jp" + a["href"]

        date_tag = item.select_one(".date")
        published = date_tag.get_text(strip=True) if date_tag else ""

        articles.append({
            "source": source,
            "title": title,
            "link": link,
            "published": published,
            "summary": "(JAXA記事は要約対象外)",
            "score": 3
        })

    return articles


# ============================================================
# 通常の RSS 取得（ESA対策で User-Agent 追加）
# ============================================================
def fetch_feed(source, url):

    print(f"Connecting -> {source}")

    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    feed = feedparser.parse(resp.text)

    if feed.bozo:
        print(f"[WARNING] {source}: RSS parse error")
        print(feed.bozo_exception)

    # ESA / JAXA 対策：RSSが空なら fallback
    if len(feed.entries) == 0:
        return fetch_html_fallback(source, url)

    entries = feed.entries[:MAX_ARTICLES]
    print(f"{source}: {len(entries)} article(s)")

    cache = load_cache()
    articles = []

    for i, entry in enumerate(entries, start=1):

        print(f"[{source}] {i}/{len(entries)}")

        title = entry.get("title", "")
        summary_text = entry.get("summary", "")
        link = entry.get("link", "")
        published = entry.get("published", "")

        content = f"""
Title:
{title}

Summary:
{summary_text}
"""

        # キャッシュ利用
        if link in cache:
            print("Already summarized")
            analysis = cache[link]
        else:
            analysis = analyze_article(content)
            cache[link] = analysis

        articles.append({
            "source": source,
            "title": title,
            "link": link,
            "published": published,
            "summary": analysis["summary"],
            "score": analysis["score"],
        })

    save_cache(cache)
    return articles


# ============================================================
# 全RSS取得
# ============================================================
def fetch_all_feeds():

    all_articles = []

    for rss in RSS_FEEDS:
        source = rss["name"]
        url = rss["url"]

        try:
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
