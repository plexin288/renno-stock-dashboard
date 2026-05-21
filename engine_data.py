import yfinance as yf
import requests

def get_stock_data(ticker):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    try:
        stock = yf.Ticker(f"{ticker}.JK", session=session)
        hist = stock.history(period="5d")
        if hist.empty: return None
        
        curr = float(hist['Close'].iloc[-1])
        prev = float(hist['Close'].iloc[-2])
        chg = ((curr - prev) / prev) * 100
        
        return {"price": curr, "pct": chg}
    except:
        return None
