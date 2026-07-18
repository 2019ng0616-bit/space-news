from ollama import chat

MODEL_NAME = "gemma4:latest"


def summarize_article(text: str) -> str:
    """
    記事を日本語で3点に要約する
    """

    prompt = f"""
あなたは宇宙ニュース専門の編集者です。

以下の記事を日本語で要約してください。

条件
・箇条書き3点
・各項目40文字以内
・専門用語はできるだけ残す
・前置きは禁止

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

    return response["message"]["content"].strip()