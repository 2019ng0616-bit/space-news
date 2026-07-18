from news.fetch import fetch_all_feeds
from news.save import save_to_json


def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()

    print(f"{len(articles)} articles fetched.")

    save_to_json(articles)

    print("Saved to data/news.json")


if __name__ == "__main__":
    main()