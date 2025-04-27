import time
import json
import yfinance as yf
from opensearchpy import OpenSearch

# Configure OpenSearch connection
from opensearchpy import OpenSearch
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize OpenSearch client with HTTPS
os_client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False  # Set to True if you want to validate certificates
)

# List of stock tickers to track
TICKERS = ["AAPL", "TSLA", "MSFT"]

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1wk")

        if data.empty:
            print(f"No data available for {ticker}.")
            return None

        stock_info = {
            "ticker": ticker,
            "open": round(data["Open"].iloc[0], 2),
            "high": round(data["High"].iloc[0], 2),
            "low": round(data["Low"].iloc[0], 2),
            "close": round(data["Close"].iloc[0], 2),
            "volume": int(data["Volume"].iloc[0]),
            "trend": "bullish" if data["Close"].iloc[-1] > data["Open"].iloc[0] else "bearish",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        return stock_info

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def send_to_opensearch(data):
    try:
        response = os_client.index(index="us_stock", body=data)
        print(f"Data indexed for {data['ticker']}: {response['result']}")
    except Exception as e:
        print(f"Failed to index data in OpenSearch: {e}")

if __name__ == "__main__":
    while True:
        for ticker in TICKERS:
            stock_data = get_stock_data(ticker)
            if stock_data:
                send_to_opensearch(stock_data)

        print("Waiting for 60 seconds before fetching data again...")
        time.sleep(60)

