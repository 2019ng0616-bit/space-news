from collections import defaultdict
from datetime import datetime

from flask import Flask, render_template

from news.load import load_from_json

app = Flask(__name__)


@app.route("/")
def home():

    articles = load_from_json()

    grouped_articles = defaultdict(list)

    total_articles = len(articles)

    total_sources = len(grouped_articles)

    average_score = round(
        sum(a["score"] for a in articles) / total_articles,
        1
    ) if articles else 0

    top_story = None

    if articles:
        top_story = max(
            articles,
            key=lambda x: x["score"]
        )

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    for article in articles:
        grouped_articles[article["source"]].append(article)

    return render_template(
        "index.html",
        grouped_articles=grouped_articles,
        total_articles=total_articles,
        total_sources=total_sources,
        average_score=average_score,
        top_story=top_story,
        updated_at=updated_at,
    )


if __name__ == "__main__":
    app.run(debug=True)