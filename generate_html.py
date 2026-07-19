import os
import shutil
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


def generate_html(articles, total_articles, total_sources, average_score, updated_at):

    grouped_articles = defaultdict(list)
    for article in articles:
        grouped_articles[article["source"]].append(article)

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")

    html = template.render(
        grouped_articles=grouped_articles,
        total_articles=total_articles,
        total_sources=total_sources,
        average_score=average_score,
        updated_at=updated_at
    )

    os.makedirs("docs/static", exist_ok=True)

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    shutil.copy("static/style.css", "docs/static/style.css")

    print("Generated docs/index.html")
