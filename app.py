from collections import defaultdict

from flask import Flask, render_template

from news.load import load_from_json

app = Flask(__name__)


@app.route("/")
def home():

    articles = load_from_json()

    grouped_articles = defaultdict(list)

    for article in articles:
        grouped_articles[article["source"]].append(article)

    return render_template(
        "index.html",
        grouped_articles=grouped_articles
    )


if __name__ == "__main__":
    app.run(debug=True)