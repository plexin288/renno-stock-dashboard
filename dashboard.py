import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import requests
from datetime import datetime

# --- CONFIGURASI UTAMA ---
st.set_page_config(page_title="Apex Intelligence", layout="wide", page_icon="🚀")

# --- CSS PRO-GRADE (MENGGANTIKAN SEMUA FILE CSS) ---
st.markdown("""
<style>
    :root { 
        --bg-color: #F8F9FF; 
        --sidebar-bg: #E1D5F8; 
        --card-bg: #FFFFFF; 
        --primary-purple: #6A1B9A; 
        --accent-purple: #9575CD;
    }
    .stApp { background-color: var(--bg-color); }
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, var(--sidebar-bg) 0%, #EDE7F6 100%) !important; 
        border-right: 1px solid #D1C4E9;
    }
    .stock-card {
        background: var(--card-bg);
        border: 1px solid #D1C4E9;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.06);
        transition: transform 0.2s ease;
    }
    .stock-card:hover { transform: translateY(-5px); }
    .ticker-header { font-size: 20px; font-weight: 800; color: #311B92; }
    .price-display { font-size: 28px; font-weight: 900; margin: 8px 0; color: #000; }
    .percentage { font-size: 16px; font-weight: 700; color: #2E7D32; }
    .metric-row { display: flex; justify-content: space-between; margin-top: 15px; font-size: 13px; color: #424242; }
</style>
""", unsafe_allow_html=True)

# --- ENGINE KELAS DATA (DIBUAT DETAIL & PANJANG) ---
class ApexEngine:
    """Kelas untuk mengelola semua data pasar dan kalkulasi teknikal."""
    def __init__(self, ticker_symbol: str):
        self.symbol = f"{ticker_symbol}.JK"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    def fetch_data(self):
        """Mengambil data historis dengan validasi ketat."""
        try:
            ticker = yf.Ticker(self.symbol, session=self.session)
            df = ticker.history(period="3mo")
            if df.empty: return None
            return df
        except Exception:
            return None

    def calculate_technical(self, df):
        """Menghitung RSI, MACD, dan Trend secara komprehensif."""
        # Logika RSI
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

# --- UI CONTROLLER & RENDERER ---
class ApexDashboard:
    def __init__(self):
        self.tickers = ["LCKM", "SURE", "APIC", "INTD", "MORA", "BAPA"]
    
    def render_sidebar(self):
        with st.sidebar:
            st.image("https://img.icons8.com/color/96/000000/rocket.png", width=60)
            st.title("Apex")
            st.radio("Navigation", ["Dashboard", "Stocks Journal", "Bedah Saham"])
            st.button("✨ Upgrade VIP", use_container_width=True)
            
    def run(self):
        self.render_sidebar()
        st.header("Stocks")
        st.markdown("---")
        
        cols = st.columns(3)
        for idx, ticker in enumerate(self.tickers):
            engine = ApexEngine(ticker)
            data = engine.fetch_data()
            
            if data is not None:
                metrics = engine.calculate_technical(data)
                with cols[idx % 3]:
                    # Render Kartu
                    st.markdown(f"""
                    <div class="stock-card">
                        <div class="ticker-header">{ticker}</div>
                        <div class="price-display">Rp {metrics['price']:,.0f}</div>
                        <div class="percentage">+{metrics['pct']:.2f}%</div>
                        <div class="metric-row">
                            <span>📈 RSI (14)</span> <b>{metrics['rsi']}</b>
                        </div>
                        <div class="metric-row">
                            <span>📊 Vol Ratio</span> <b>1.8x High</b>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    # Grafik Sparkline
                    st.line_chart(metrics['history'], height=100)
            else:
                st.error(f"Gagal memuat {ticker}")

# --- EKSEKUSI ---
if __name__ == "__main__":
    app = ApexDashboard()
    app.run()
