import streamlit as st
from styles import inject_custom_css
from engine_data import get_stock_metrics
from components import render_stock_card

# 1. Setup
st.set_page_config(page_title="Renno Stocks", layout="wide")
inject_custom_css()

# 2. Sidebar
with st.sidebar:
    st.markdown("## 🚀 Renno Stocks")
    menu = st.radio("MENU UTAMA", ["Dashboard", "Stocks", "Stocks Jurnal"])

# 3. Content
st.title("Alpha Intelligence — Stock Analysis")

tickers = ["BBCA", "BMRI", "TLKM"]
cols = st.columns(3)

for i, ticker in enumerate(tickers):
    data = get_stock_data(ticker)
    if data:
        with cols[i]:
            render_stock_card(ticker, data)
    else:
        st.error(f"Gagal memuat {ticker}")
