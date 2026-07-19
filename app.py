from collections import defaultdict
from datetime import datetime

from flask import Flask, render_template

from news.load import load_from_json

app = Flask(__name__)


@app.route("/")
def home():

    articles = load_from_json()

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    return render_template(
        "index.html",
        grouped_articles=grouped_articles,
        updated_at=updated_at,
    )


if __name__ == "__main__":
    app.run(debug=True)