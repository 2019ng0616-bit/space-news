from flask import Flask, render_template

from news.load import load_from_json

app = Flask(__name__)


@app.route("/")
def home():

    articles = load_from_json()

    return render_template(
        "index.html",
        articles=articles
    )


if __name__ == "__main__":
    app.run(debug=True)