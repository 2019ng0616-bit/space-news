from collections import defaultdict
from datetime import datetime
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader


def generate_html(articles):

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    total_articles = len(articles)

    total_sources = len(grouped_articles)

    average_score = round(
        sum(a["score"] for a in articles) / total_articles,
        1
    ) if articles else 0

    top_story = max(
        articles,
        key=lambda x: x["score"]
    ) if articles else None

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("index.html")

    html = template.render(
        grouped_articles=grouped_articles,
        total_articles=total_articles,
        total_sources=total_sources,
        average_score=average_score,
        top_story=top_story,
        updated_at=updated_at,
    )

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    with open(output_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html)

    shutil.copy(
        "static/style.css",
        output_dir / "style.css"
    )