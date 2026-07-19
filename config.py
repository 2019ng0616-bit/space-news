"""
Application Configuration
"""

# ------------------------
# Development Settings
# ------------------------

# 開発モード
DEBUG_MODE = True

# RSS取得件数
MAX_ARTICLES = 1

# AI要約を有効化
ENABLE_SUMMARY = True

# 使用するLLM
MODEL_NAME = "gemma4:latest"

# JSON保存先
OUTPUT_JSON = "data/news.json"

# AI Scoring
ENABLE_SCORING = True