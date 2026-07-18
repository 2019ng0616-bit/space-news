import json


def save_to_json(articles, filename="data/news.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            articles,
            f,
            ensure_ascii=False,
            indent=4
        )