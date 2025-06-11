import sys

sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient
import json
from datetime import datetime
import os

# Initialize API client
client = ApiClient()

# Define MEGA7 stocks
mega7_stocks = [
    {"name": "Alphabet", "symbol": "GOOGL"},
    {"name": "Amazon", "symbol": "AMZN"},
    {"name": "Apple", "symbol": "AAPL"},
    {"name": "Meta Platforms", "symbol": "META"},
    {"name": "Microsoft", "symbol": "MSFT"},
    {"name": "NVIDIA", "symbol": "NVDA"},
    {"name": "Tesla", "symbol": "TSLA"}
]

# Create directory for data
os.makedirs("mega7_data", exist_ok=True)

# Fetch YTD data for each stock
for stock in mega7_stocks:
    symbol = stock["symbol"]
    print(f"Fetching YTD data for {stock['name']} ({symbol})...")

    # Call Yahoo Finance API to get YTD data
    stock_data = client.call_api('YahooFinance/get_stock_chart', query={
        'symbol': symbol,
        'region': 'US',
        'interval': '1d',  # Daily data
        'range': 'ytd',  # Year-to-date range
        'includeAdjustedClose': True
    })

    # Save raw data to file
    with open(f"mega7_data/{symbol}_ytd_raw.json", "w") as f:
        json.dump(stock_data, f, indent=2)

    # Process data to calculate YTD performance
    try:
        result = stock_data.get("chart", {}).get("result", [{}])[0]
        meta = result.get("meta", {})
        timestamps = result.get("timestamp", [])
        indicators = result.get("indicators", {})

        # Get price data
        quote_data = indicators.get("quote", [{}])[0]
        adj_close_data = indicators.get("adjclose", [{}])[0].get("adjclose", [])

        # Get first and latest trading day data
        if timestamps and adj_close_data:
            first_day_timestamp = timestamps[0]
            latest_day_timestamp = timestamps[-1]

            first_day_date = datetime.fromtimestamp(first_day_timestamp).strftime('%Y-%m-%d')
            latest_day_date = datetime.fromtimestamp(latest_day_timestamp).strftime('%Y-%m-%d')

            first_day_price = adj_close_data[0]
            latest_day_price = adj_close_data[-1]

            # Calculate YTD performance
            ytd_change = latest_day_price - first_day_price
            ytd_percent_change = (ytd_change / first_day_price) * 100

            # Prepare performance summary
            performance = {
                "symbol": symbol,
                "name": stock["name"],
                "first_trading_day": first_day_date,
                "first_day_price": first_day_price,
                "latest_trading_day": latest_day_date,
                "latest_price": latest_day_price,
                "ytd_change": ytd_change,
                "ytd_percent_change": ytd_percent_change,
                "currency": meta.get("currency", "USD")
            }

            # Save performance data
            with open(f"mega7_data/{symbol}_ytd_performance.json", "w") as f:
                json.dump(performance, f, indent=2)

            print(f"✓ {symbol}: YTD change: {ytd_percent_change:.2f}%")
        else:
            print(f"× {symbol}: No data available")

    except Exception as e:
        print(f"× Error processing {symbol}: {str(e)}")
    finally:
        print(f' code block execution complete')

print("All MEGA7 stocks YTD data fetched and processed.")
