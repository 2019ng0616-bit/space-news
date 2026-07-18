from news.fetch import fetch_all_feeds
from news.save import save_to_json

articles = fetch_all_feeds()

save_to_json(articles)

print("保存完了")