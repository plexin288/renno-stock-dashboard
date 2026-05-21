import yfinance as yf
import requests
import logging

class StockAnalyzer:
    def __init__(self, ticker_symbol: str):
        self.ticker_symbol = f"{ticker_symbol}.JK"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
        logging.basicConfig(level=logging.INFO)

    def fetch_market_data(self, period="1mo"):
        try:
            ticker = yf.Ticker(self.ticker_symbol, session=self.session)
            history = ticker.history(period=period)
            if history.empty:
                return None
            return history
        except Exception as e:
            logging.error(f"Error pada engine: {e}")
            return None

    def calculate_metrics(self, data):
        curr = float(data['Close'].iloc[-1])
        prev = float(data['Close'].iloc[-2])
        return {
            "current_price": curr,
            "change_pct": ((curr - prev) / prev) * 100,
            "high": float(data['High'].max()),
            "low": float(data['Low'].min()),
            "volume_avg": float(data['Volume'].mean())
        }
