from ollama import chat
from config import MODEL_NAME

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


def score_article(text: str) -> int:
    """
    記事の重要度を1〜5で評価する
    """

    prompt = f"""
あなたは宇宙ニュース専門の編集者です。

以下の記事の重要度を評価してください。

評価基準

5：宇宙業界全体へ大きな影響
4：かなり重要
3：一般的なニュース
2：小さな話題
1：ほとんど重要ではない

回答は

1
2
3
4
5

の数字だけ。

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

    result = response["message"]["content"].strip()

    try:
        return int(result)
    except ValueError:
        return 3
