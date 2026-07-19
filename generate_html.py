from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import os


def generate_html(articles):

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("index.html")

    html = template.render(
        grouped_articles=grouped_articles
    )

    os.makedirs("output", exist_ok=True)

    with open(
        "output/index.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print("Static HTML generated.")