import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# ==========================================
# 1. UI ENGINE & CUSTOM CSS (Premium Look)
# ==========================================
st.set_page_config(page_title="Alpha Intelligence — TumbuhKaya", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    .stApp { background-color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Sidebar Ungu Muda */
    [data-testid="stSidebar"] { background-color: #F8F5FF !important; border-right: 1px solid #E9D5FF; }
    
    /* Card Premium */
    .alpha-card { 
        background: white; border: 1px solid #E9D5FF; border-radius: 16px; padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(124, 58, 237, 0.05);
    }
    
    /* Badge Status */
    .badge-bullish { background: #DCFCE7; color: #15803D; padding: 4px 10px; border-radius: 50px; font-size: 10px; font-weight: 700; }
    
    h1, h2, h3 { color: #1E1B4B; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA ENGINE
# ==========================================
@st.cache_data(ttl=300)
def get_stock_data():
    # Simulasi data untuk 5 saham top picks
    data = [
        {"ticker": "ASPR", "price": 384, "tp": 432, "sl": 368, "prob": "90%"},
        {"ticker": "CMNP", "price": 1560, "tp": 2067, "sl": 1391, "prob": "88%"},
        {"ticker": "KETR", "price": 597, "tp": 672, "sl": 572, "prob": "85%"},
        {"ticker": "GULA", "price": 400, "tp": 451, "sl": 383, "prob": "82%"},
        {"ticker": "OASA", "price": 413, "tp": 464, "sl": 396, "prob": "80%"}
    ]
    return data

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("## 🌱 TumbuhKaya")
    menu = st.radio("MENU UTAMA", ["Dashboard", "Stocks", "Stocks Jurnal", "Bedah Saham"])
    st.markdown("---")
    st.button("✨ Upgrade VIP", use_container_width=True)

# ==========================================
# 4. MAIN DASHBOARD CONTENT
# ==========================================
st.markdown("<h1>Alpha Intelligence — <span style='color:#7C3AED;'>Stock Analysis</span></h1>", unsafe_allow_html=True)
st.write("Analisis 970 saham IDX menggunakan data fundamental, teknikal, dan AI.")

# AI Daily Pick Section
st.markdown("### 🤖 AI Daily Pick <span style='font-size:12px; color:gray;'>TOP 5</span>", unsafe_allow_html=True)

picks = get_stock_data()
cols = st.columns(5)

for i, stock in enumerate(picks):
    with cols[i]:
        st.markdown(f"""
        <div class="alpha-card">
            <div style="display:flex; justify-content:space-between;">
                <b style="font-size:18px;">{stock['ticker']}</b>
                <span style="font-size:10px; color:gray;">{stock['prob']}</span>
            </div>
            <span class="badge-bullish">Bullish</span>
            <div style="margin-top:10px; font-size:12px;">
                <div style="display:flex; justify-content:space-between;"><span>Entry</span> <b>{stock['price']}</b></div>
                <div style="display:flex; justify-content:space-between;"><span>TP3</span> <b style="color:green;">{stock['tp']}</b></div>
                <div style="display:flex; justify-content:space-between;"><span>SL</span> <b style="color:red;">{stock['sl']}</b></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Placeholder untuk listing saham bawah
st.markdown("<br>### 📊 Halaman 1 dari 81 - 970 Saham", unsafe_allow_html=True)
# Sini nanti bisa ditambah grid untuk list saham (LCKM, SURE, APIC) seperti di gambar
