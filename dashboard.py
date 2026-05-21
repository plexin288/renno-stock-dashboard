import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import yfinance as yf

# Konfigurasi Halaman
st.set_page_config(
    page_title="StockAI Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk tampilan persis desain (Rounded Card, Purple Theme)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #F8F7FF; }

/* FIX: Agar tombol >> tetap ada saat sidebar ditutup */
[data-testid="collapsedControl"] { display: block; color: #8B5CF6; }

.card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(139,92,246,0.05);
    border: 1px solid #F1F1F1;
    margin-bottom: 20px;
}
.metric-card {
    background: white; padding: 20px; border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.02); border: 1px solid #F1F1F1;
}
.title { font-size: 28px; font-weight: 700; color: #111827; }
.subtitle { color: #6B7280; font-size: 14px; margin-bottom: 20px; }
.green { color: #10B981; font-weight: 600; }
.red { color: #EF4444; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# Fungsi Ambil Data
@st.cache_data
def load_stock(ticker):
    if not ticker.endswith(".JK"): ticker += ".JK"
    return yf.download(ticker, period="3mo")

# SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#8B5CF6;'>✨ StockAI</h2>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Watchlist", "AI Scanner", "Chart", "Top Gainers", "Heatmap"],
        icons=["grid", "star", "robot", "bar-chart", "graph-up-arrow", "grid-3x3-gap"],
        default_index=0,
        styles={
            "nav-link": {"font-size": "14px", "margin":"5px", "border-radius": "10px"},
            "nav-link-selected": {"background-color": "#8B5CF6"},
        }
    )
    st.markdown("<div style='background:linear-gradient(135deg,#8B5CF6,#C084FC); padding:12px; border-radius:12px; color:white; text-align:center; font-weight:600; font-size:14px;'>🚀 Telegram Bot Connected</div>", unsafe_allow_html=True)

# HEADER
col_h1, col_h2 = st.columns([4,1.5])
with col_h1:
    st.markdown("<div class='title'>Good Morning, Bre 👋</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Market overview today</div>", unsafe_allow_html=True)
with col_h2:
    ticker_input = st.text_input("", value="BBCA", placeholder="Search stock (e.g BBCA)").upper()

if selected == "Dashboard":
    # 1. METRICS ROW
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown("<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>IHSG</p><h3 style='margin:0;'>7,145.23</h3><p class='green' style='font-size:12px; margin:0;'>+0.64%</p></div>", unsafe_allow_html=True)
    with m2: st.markdown("<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Volume</p><h3 style='margin:0;'>20.45 B</h3><p class='green' style='font-size:12px; margin:0;'>+12.3%</p></div>", unsafe_allow_html=True)
    with m3: st.markdown("<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Value</p><h3 style='margin:0;'>12.35 T</h3><p class='green' style='font-size:12px; margin:0;'>+8.2%</p></div>", unsafe_allow_html=True)
    with m4: st.markdown("<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Market Cap</p><h3 style='margin:0;'>11,234 T</h3><p class='green' style='font-size:12px; margin:0;'>+0.7%</p></div>", unsafe_allow_html=True)

    # 2. MAIN CONTENT
    left_col, right_col = st.columns([3, 1.2])

    with left_col:
        df = load_stock(ticker_input)
        if not df.empty:
            last_price = df['Close'].iloc[-1].item()
            # Card Chart Utama (Candlestick biar persis desain)
            st.markdown(f"""<div class='card'><p style='margin:0; font-weight:600;'>{ticker_input} · Data</p><h1 style='margin:0;'>{last_price:,.0f} <span style='font-size:16px;' class='green'>+1.29%</span></h1></div>""", unsafe_allow_html=True)
            
            fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
            fig.update_layout(height=400, margin=dict(l=0,r=0,t=0,b=0), template="plotly_white", xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)

    with right_col:
        st.markdown("<p style='font-weight:700; margin-bottom:10px;'>Watchlist</p>", unsafe_allow_html=True)
        watchlist = [("BBCA", "+1.29%"), ("BMRI", "+1.12%"), ("TLKM", "-0.34%"), ("ASII", "+0.84%")]
        for s, c in watchlist:
            color = "green" if "+" in c else "red"
            st.markdown(f"<div class='card' style='padding:12px; margin-bottom:8px;'><div style='display:flex; justify-content:space-between;'><b>{s}</b><span class='{color}'>{c}</span></div></div>", unsafe_allow_html=True)

else:
    st.write(f"Halaman {selected} dalam pengembangan.")
