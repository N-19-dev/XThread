import feedparser


url = "https://www.lemonde.fr/rss/plus-lus.xml"

try:
    feed = feedparser.parse(url)
    print(feed)

except Exception as e:
    print("Error:", e)