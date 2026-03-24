import config
from collections import defaultdict

def generate_signals(analyzed_data):
    """
    Aggregates sentiment scores per asset and generates trading signals.
    """
    asset_scores = defaultdict(list)
    
    # Aggregate sentiment scores for each tagged asset
    for item in analyzed_data:
        for tag in item['tags']:
            asset_scores[tag].append(item['sentiment'])

    signals = {}
    
    # Calculate average sentiment and map to a signal
    for asset, scores in asset_scores.items():
        if not scores:
            continue
            
        avg_score = sum(scores) / len(scores)
        
        signal = 'HOLD'
        if avg_score >= config.SENTIMENT_THRESHOLDS['STRONG_BUY']:
            signal = 'STRONG_BUY'
        elif avg_score >= config.SENTIMENT_THRESHOLDS['BUY']:
            signal = 'BUY'
        elif avg_score <= config.SENTIMENT_THRESHOLDS['STRONG_SELL']:
            signal = 'STRONG_SELL'
        elif avg_score <= config.SENTIMENT_THRESHOLDS['SELL']:
            signal = 'SELL'
            
        signals[asset] = {
            'average_sentiment': round(avg_score, 4),
            'signal': signal,
            'news_count': len(scores)
        }
        
    return signals

def print_signals(signals):
    print("\n=============================================")
    print("🤖 TRADING BOT AI SIGNALS 🤖")
    print("=============================================")
    print(f"{'ASSET':<15} | {'SIGNAL':<12} | {'SENTIMENT':<10} | {'DATA POINTS'}")
    print("-" * 55)
    
    for asset, data in sorted(signals.items(), key=lambda x: x[1]['average_sentiment'], reverse=True):
        print(f"{asset:<15} | {data['signal']:<12} | {data['average_sentiment']:<10} | {data['news_count']}")
    
    print("=============================================\n")
    print("LEGAL DISCLAIMER:")
    print("1. Signals are for educational purposes only. Not financial advice.")
    print("2. Ensure all Forex trading complies with RBI/FEMA regulations (trade only via Indian exchanges like NSE/BSE).")
    print("3. Cryptocurrency trading in India is taxable under VDA regulations and carries high risk.")
