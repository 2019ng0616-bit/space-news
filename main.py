from news.fetch import fetch_all_feeds
from news.save import save_to_json


def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()

    save_to_json(articles)

    print(f"Saved {len(articles)} articles.")


if __name__ == "__main__":
    main()