import streamlit as st
import yfinance as yf
import requests
import pandas as pd
import numpy as np

# --- 1. CONFIG & CSS (Bikin Tampilan Premium) ---
st.set_page_config(page_title="Apex Intelligence", layout="wide", page_icon="🚀")

st.markdown("""
<style>
    /* Styling Dasar */
    :root { --bg: #F8F9FF; --side: #E1D5F8; --card: #FFFFFF; --purple: #6A1B9A; }
    .stApp { background-color: var(--bg); font-family: 'Inter', sans-serif; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background: linear-gradient(180deg, var(--side) 0%, #EDE7F6 100%) !important; }
    
    /* Kartu Saham */
    .stock-card {
        background: var(--card); border: 1px solid #D1C4E9; border-radius: 20px;
        padding: 24px; box-shadow: 0 6px 15px rgba(0,0,0,0.06);
        transition: transform 0.2s; margin-bottom: 20px;
    }
    .stock-card:hover { transform: translateY(-5px); }
    .ticker-header { font-size: 20px; font-weight: 800; color: #311B92; margin-bottom: 10px; }
    .price-display { font-size: 28px; font-weight: 900; margin: 5px 0; color: #000; }
    .percentage { font-size: 16px; font-weight: 700; color: #2E7D32; margin-bottom: 15px; }
    .metric-row { display: flex; justify-content: space-between; margin-top: 10px; font-size: 13px; color: #424242; }
</style>
""", unsafe_allow_html=True)

# --- 2. ENGINE (Kalkulasi Saham) ---
def get_stock_data(ticker):
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0'})
        df = yf.Ticker(f"{ticker}.JK", session=session).history(period="3mo")
        if df.empty: return None
        
        # Kalkulasi RSI (Standar Teknis)
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        return {
            "price": float(df['Close'].iloc[-1]),
            "pct": ((df['Close'].iloc[-1] - df['Close'].iloc[-2]) / df['Close'].iloc[-2]) * 100,
            "rsi": round(rsi.iloc[-1], 1),
            "history": df['Close'].tail(20).tolist()
        }
    except: return None

# --- 3. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/rocket.png", width=60)
    st.title("Apex")
    st.radio("Navigation", ["Dashboard", "Stocks Journal", "Bedah Saham"])
    st.button("✨ Upgrade VIP", use_container_width=True)

# --- 4. MAIN CONTENT ---
st.header("Stocks")
st.markdown("---")

tickers = ["LCKM", "SURE", "APIC", "INTD", "MORA", "BAPA"]
cols = st.columns(3)

for idx, ticker in enumerate(tickers):
    data = get_stock_data(ticker)
    if data:
        with cols[idx % 3]:
            # Rendering Kartu dengan HTML Kustom
            st.markdown(f"""
            <div class="stock-card">
                <div class="ticker-header">{ticker}</div>
                <div class="price-display">Rp {data['price']:,.0f}</div>
                <div class="percentage">+{data['pct']:.2f}%</div>
                <div class="metric-row"><span>📈 RSI (14)</span> <b>{data['rsi']}</b></div>
                <div class="metric-row"><span>📊 Vol Ratio</span> <b>1.8x High</b></div>
            </div>
            """, unsafe_allow_html=True)
            # Grafik kecil
            st.line_chart(data['history'], height=100)
    else:
        st.error(f"Gagal memuat {ticker}")
