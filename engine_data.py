import yfinance as yf
import pandas as pd
import numpy as np

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def get_technical_data(ticker_symbol):
    try:
        df = yf.Ticker(f"{ticker_symbol}.JK").history(period="3mo")
        if df.empty: return None
        
        # RSI
        rsi = calculate_rsi(df).iloc[-1]
        
        # MACD (12, 26, 9)
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        macd_status = "Bullish" if macd.iloc[-1] > signal.iloc[-1] else "Bearish"
        
        return {
            "price": float(df['Close'].iloc[-1]),
            "pct": ((df['Close'].iloc[-1] - df['Close'].iloc[-2]) / df['Close'].iloc[-2]) * 100,
            "rsi": round(rsi, 1),
            "macd": macd_status,
            "history": df['Close'].tail(15).tolist() # Untuk grafik kecil
        }
    except: return None
