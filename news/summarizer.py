import json
import re

from ollama import chat
from config import MODEL_NAME


def analyze_article(text: str) -> dict:
    """
    記事をAIで解析する

    Returns
    -------
    {
        "summary": "...",
        "score": 5
    }
    """

    prompt = f"""
あなたは宇宙ニュース専門の編集者です。

以下の記事について解析してください。

出力ルールを絶対に守ってください。

【出力形式】
JSONのみを出力してください。
説明文は禁止です。
Markdownは禁止です。
```json は禁止です。

JSON形式は必ず以下です。

{{
  "summary": [
    "40文字以内",
    "40文字以内",
    "40文字以内"
  ],
  "score": 1
}}

scoreは1〜5の整数のみ。

記事

{text}
"""

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response["message"]["content"]

    # 万一 ```json が付いてきても除去
    result = re.sub(r"```json", "", result)
    result = re.sub(r"```", "", result)
    result = result.strip()

    try:

        data = json.loads(result)

        return {
            "summary": "\n".join(data["summary"]),
            "score": int(data["score"])
        }

    except Exception as e:

        print("JSON Parse Error")
        print(result)
        print(e)

        return {
            "summary": "要約失敗",
            "score": 3
        }