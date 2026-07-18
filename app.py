from news.fetch import fetch_all_feeds

articles = fetch_all_feeds()

for article in articles:
    print("=" * 60)
    print(article["source"])
    print(article["title"])
    print(article["published"])
    print(article["link"])