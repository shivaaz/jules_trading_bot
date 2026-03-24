import feedparser
from datetime import datetime
import config

def fetch_news(feed_url, max_items=10):
    """
    Fetches news from a given RSS feed URL.
    """
    try:
        feed = feedparser.parse(feed_url)
        news_items = []
        for entry in feed.entries[:max_items]:
            news_items.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published if hasattr(entry, 'published') else datetime.now().isoformat(),
                'summary': entry.summary if hasattr(entry, 'summary') else ''
            })
        return news_items
    except Exception as e:
        print(f"Error fetching news from {feed_url}: {e}")
        return []

def get_all_news():
    """
    Fetches news from all configured sources and categorizes them.
    """
    all_news = {}
    for category, url in config.NEWS_FEEDS.items():
        print(f"Fetching news for {category}...")
        all_news[category] = fetch_news(url)
    return all_news

if __name__ == '__main__':
    news_data = get_all_news()
    for category, items in news_data.items():
        print(f"\n--- {category.upper()} NEWS ({len(items)} items) ---")
        for item in items[:2]: # Just print top 2 for testing
            print(f"- {item['title']}")
