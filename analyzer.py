from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import config

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using VADER.
    Returns the compound score (-1 to +1).
    """
    if not text:
        return 0.0
    scores = analyzer.polarity_scores(text)
    return scores['compound']

def process_news_sentiment(categorized_news):
    """
    Analyzes sentiment for all fetched news items and maps them to potential assets.
    """
    analyzed_data = []

    for category, items in categorized_news.items():
        for item in items:
            # Combine title and summary for better context
            full_text = f"{item['title']} {item['summary']}"
            sentiment_score = analyze_sentiment(full_text)
            
            # Simple keyword extraction to tag relevant assets
            tags = []
            
            # Check Indian Stocks
            for stock in config.INDIAN_STOCKS:
                if stock.lower() in full_text.lower():
                    tags.append(stock)
            
            # Check Forex Pairs
            for pair in config.FOREX_PAIRS:
                if pair.lower() in full_text.lower() or pair[:3].lower() in full_text.lower(): # e.g. 'usd'
                    tags.append(pair)
            
            # Check Crypto Assets
            for crypto in config.CRYPTO_ASSETS:
                if crypto.lower() in full_text.lower():
                    tags.append(crypto)

            # If no specific tags found, use broad category
            if not tags:
                if category == 'indian_markets':
                    tags.append('NIFTY 50') # Proxy for broad market
                elif category == 'crypto':
                    tags.append('BTC') # Proxy for crypto
                elif category == 'forex':
                    tags.append('USDINR') # Proxy for forex in India
            
            analyzed_item = {
                'title': item['title'],
                'category': category,
                'sentiment': sentiment_score,
                'tags': list(set(tags)) # Unique tags
            }
            analyzed_data.append(analyzed_item)
            
    return analyzed_data

if __name__ == '__main__':
    # Test
    sample_text = "Nifty 50 crashes as inflation fears mount, creating panic among investors."
    score = analyze_sentiment(sample_text)
    print(f"Sample Score: {score}")
