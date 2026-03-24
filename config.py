# Configuration and Constants for Trading Bot

# Permitted Forex pairs in India (traded on exchanges like NSE/BSE)
FOREX_PAIRS = [
    'USDINR',
    'EURINR',
    'GBPINR',
    'JPYINR'
]

# Major Indian Equities/Indices
INDIAN_STOCKS = [
    'NIFTY 50',
    'SENSEX',
    'RELIANCE',
    'TCS',
    'HDFCBANK',
    'INFY'
]

# Major Cryptocurrencies (Legal status: Taxable as VDAs in India, not legal tender)
CRYPTO_ASSETS = [
    'BTC',
    'ETH',
    'SOL',
    'XRP'
]

# RSS Feeds for News
NEWS_FEEDS = {
    'global_finance': 'https://news.google.com/rss/search?q=global+finance+markets&hl=en-IN&gl=IN&ceid=IN:en',
    'indian_markets': 'https://news.google.com/rss/search?q=indian+stock+market+nifty+sensex&hl=en-IN&gl=IN&ceid=IN:en',
    'forex': 'https://news.google.com/rss/search?q=forex+currency+trading+usdinr&hl=en-IN&gl=IN&ceid=IN:en',
    'crypto': 'https://news.google.com/rss/search?q=cryptocurrency+bitcoin+ethereum&hl=en-IN&gl=IN&ceid=IN:en'
}

# Thresholds for sentiment analysis (-1 to 1 scale)
SENTIMENT_THRESHOLDS = {
    'STRONG_BUY': 0.5,
    'BUY': 0.15,
    'SELL': -0.15,
    'STRONG_SELL': -0.5
}
