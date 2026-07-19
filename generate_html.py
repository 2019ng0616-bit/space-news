import os
import shutil
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader


def generate_html(articles):

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    # templates/index.html を読む
    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("index.html")

    html = template.render(
        grouped_articles=grouped_articles
    )

    # docs/static を作成
    os.makedirs("docs/static", exist_ok=True)

    # docs/index.html に直接出力
    with open(
        "docs/index.html",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(html)

    # CSS を docs/static にコピー
    shutil.copy(
        "static/style.css",
        "docs/static/style.css"
    )

    print("Generated docs/index.html")
