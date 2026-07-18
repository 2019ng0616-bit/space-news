from news.summarizer import summarize_article


sample = """
NASA is testing a new lightweight wing called SWEET-15.

The goal is to reduce fuel consumption for future commercial aircraft.

Researchers pushed the wing beyond its design limit and collected valuable structural data.
"""


summary = summarize_article(sample)

print("===== Summary =====")
print(summary)