import yfinance as yf
import requests

# Pastikan nama fungsinya adalah 'get_stock_metrics'
def get_stock_metrics(ticker):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        session = requests.Session()
        stock = yf.Ticker(f"{ticker}.JK", session=session)
        hist = stock.history(period="5d")
        if hist.empty: return {"price": 0, "pct": 0, "error": "No Data"}
        curr = float(hist['Close'].iloc[-1])
        prev = float(hist['Close'].iloc[-2])
        chg = ((curr - prev) / prev) * 100
        return {"price": curr, "pct": chg, "error": None}
    except Exception as e:
        return {"price": 0, "pct": 0, "error": str(e)}
