import yfinance as yf
import requests

def get_stock_metrics(ticker):
    try:
        # Menambahkan User-Agent agar tidak diblokir Yahoo Finance
        headers = {'User-Agent': 'Mozilla/5.0'}
        ticker_symbol = f"{ticker}.JK"
        
        # Menggunakan session agar lebih stabil
        session = requests.Session()
        stock = yf.Ticker(ticker_symbol, session=session)
        
        # Mengambil data 5 hari terakhir
        hist = stock.history(period="5d")
        
        if hist.empty:
            return {"price": 0, "pct": 0, "error": "No Data"}
            
        curr = float(hist['Close'].iloc[-1])
        prev = float(hist['Close'].iloc[-2])
        chg = ((curr - prev) / prev) * 100
        
        return {"price": curr, "pct": chg, "error": None}
    except Exception as e:
        return {"price": 0, "pct": 0, "error": str(e)}
