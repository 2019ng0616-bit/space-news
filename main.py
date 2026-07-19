from shutil import copy2
import os

from news.fetch import fetch_all_feeds
from news.save import save_to_json
from generate_html import generate_html


def main():

    print("Fetching latest space news...")

    articles = fetch_all_feeds()

    save_to_json(articles)

    generate_html(articles)

    os.makedirs("docs", exist_ok=True)

    copy2(
        "output/index.html",
        "docs/index.html"
    )

    copy2(
        "style.css",
        "docs/style.css"
    )

    print()

    print("GitHub Pages updated.")


if __name__ == "__main__":
    main()