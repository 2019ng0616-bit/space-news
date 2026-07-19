from collections import defaultdict
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader


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

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(
        output_dir / "index.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    shutil.copy(
        "static/style.css",
        output_dir / "style.css"
    )

    print("Static site generated.")