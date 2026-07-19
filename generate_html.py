from collections import defaultdict
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader


def generate_html(articles):

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    env = Environment(
        loader=FileSystemLoader(".")
    )

    template = env.get_template("index.html")

    html = template.render(
        grouped_articles=grouped_articles
    )

    # GitHub Pages とローカルで共通の構造にする
    output_dir = Path("output")
    static_dir = output_dir / "static"

    output_dir.mkdir(exist_ok=True)
    static_dir.mkdir(exist_ok=True)

    # index.html を出力
    with open(
        output_dir / "index.html",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(html)

    # CSS を output/static にコピー
    shutil.copy(
        "static/style.css",
        static_dir / "style.css"
    )

    print("Static site generated.")
