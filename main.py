from news.fetch import fetch_all_feeds
from news.save import save_to_json
from config import ENABLE_SCORING
from news.summarizer import score_article

def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()

    for article in articles:
        if ENABLE_SCORING:
            text = f"""
            {article['title']}
            {article['summary']}
            """
            article["score"] = score_article(text)
        else:
            article["score"] = 0

    print(f"{len(articles)} articles fetched.")

    save_to_json(articles)

    print("Saved to data/news.json")


if __name__ == "__main__":
    main()