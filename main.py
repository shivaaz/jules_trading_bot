import time
import schedule
from news_scraper import get_all_news
from analyzer import process_news_sentiment
from signal_generator import generate_signals, print_signals
import config

def run_bot():
    print("Initiating Ultimate AI Trading Bot cycle...")
    
    # 1. Scrape News
    print("Step 1: Fetching local and international news...")
    raw_news = get_all_news()
    
    # 2. Analyze Sentiment
    print("Step 2: AI Sentiment Analysis running...")
    analyzed_data = process_news_sentiment(raw_news)
    
    # 3. Generate Signals
    print("Step 3: Generating legally compliant trading signals...")
    signals = generate_signals(analyzed_data)
    
    # 4. Output Results
    print_signals(signals)

if __name__ == "__main__":
    print("Bot started. Running initial scan...")
    run_bot()
    
    # Schedule to run every hour
    schedule.every(1).hours.do(run_bot)
    
    print("Scheduler running. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(60)
