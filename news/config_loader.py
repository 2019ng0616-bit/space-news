import json


def load_rss_sources(filename="config/rss_sources.json"):
    """
    RSS設定ファイルを読み込む
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)