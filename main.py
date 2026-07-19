from news.fetch import fetch_all_feeds
from news.save import save_to_json
from generate_html import generate_html


def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()

    save_to_json(articles)

    generate_html(articles)

    print(f"Saved {len(articles)} articles.")
    print("Done.")


if __name__ == "__main__":
    main()