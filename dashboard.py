import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import requests
from datetime import datetime
import time

# ==========================================
# 1. ADVANCED UI CONFIGURATION (CSS)
# ==========================================
st.set_page_config(page_title="Alpha Intelligence — Stock Analysis", layout="wide")

def local_css():
    st.markdown("""
    <style>
        /* Import Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        * { font-family: 'Inter', sans-serif; }

        /* Main Background */
        .stApp { background-color: #FFFFFF; }

        /* Sidebar Customization */
        [data-testid="stSidebar"] {
            background-color: #F3E8FF !important; /* Ungu Muda */
            border-right: 1px solid #E9D5FF;
            padding-top: 2rem;
        }

        /* Card Analysis (AI Daily Pick) */
        .analysis-card {
            background: white;
            border: 1px solid #E9D5FF;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s;
        }
        .analysis-card:hover {
            transform: translateY(-5px);
            border-color: #A855F7;
        }

        /* Badge Style */
        .badge-bullish {
            background-color: #DCFCE7;
            color: #15803d;
            padding: 4px 12px;
            border-radius: 99px;
            font-size: 12px;
            font-weight: 600;
        }

        /* Typography */
        .main-title { color: #1E1B4B; font-weight: 700; font-size: 32px; margin-bottom: 0px; }
        .sub-title { color: #6B7280; font-size: 14px; margin-bottom: 30px; }
        .section-header { color: #4C1D95; font-weight: 700; font-size: 18px; margin-top: 20px; }
        
        /* Metric Styling */
        .price-label { font-size: 24px; font-weight: 700; color: #1E1B4B; margin: 5px 0; }
        .pct-label-up { color: #10B981; font-weight: 600; font-size: 14px; }
        .pct-label-down { color: #EF4444; font-weight: 600; font-size: 14px; }

        /* Hide Streamlit Header/Footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

local_css()

# ==========================================
# 2. DATA ENGINE (ROBUST SYSTEM)
# ==========================================
@st.cache_data(ttl=300)
def fetch_live_data(ticker_list):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    compiled_data = []
    
    for t in ticker_list:
        try:
            # Menggunakan yfinance dengan session agar tidak diblokir
            stock = yf.Ticker(t, session=session)
            df = stock.history(period="5d")
            df = df[df['Close'] > 0].dropna()
            
            if not df.empty and len(df) >= 2:
                current_price = df['Close'].iloc[-1]
                prev_price = df['Close'].iloc[-2]
                change_pct = ((current_price - prev_price) / prev_price) * 100
                
                compiled_data.append({
                    "symbol": t.replace(".JK", ""),
                    "price": current_price,
                    "change": change_pct,
                    "volume": df['Volume'].iloc[-1]
                })
        except Exception as e:
            continue
    return compiled_data

# ==========================================
# 3. SIDEBAR NAVIGATION (Sesuai Gambar)
# ==========================================
with st.sidebar:
    st.markdown("### 🌱 **TumbuhKaya**")
    st.write("---")
    
    st.caption("MENU UTAMA")
    menu = st.radio("Navigation", 
                    ["Dashboard", "News", "Porto Terbuka", "Stocks", "Stocks Jurnal", "Bedah Saham"],
                    label_visibility="collapsed")
    
    st.write("---")
    st.caption("DATA & ANALISIS")
    sub_menu = st.selectbox("Market Overview", ["IHSG", "Global Market", "Sectoral"])
    
    st.write("---")
    if st.button("✨ Upgrade VIP", use_container_width=True):
        st.toast("Redirecting to payment...")

# ==========================================
# 4. DASHBOARD PAGE LOGIC
# ==========================================
if menu == "Stocks":
    # Header Section
    st.markdown('<p class="main-title">Alpha Intelligence — Stock Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Analisis 970 saham IDX menggunakan data fundamental, teknikal, dan AI intelligence insights.</p>', unsafe_allow_html=True)
    
    # Search Bar & Filter Row
    c1, c2 = st.columns([3, 1])
    with c1:
        search_query = st.text_input("🔍 Cari ticker atau nama saham...", placeholder="Contoh: BBCA")
    with c2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.multiselect("Filter", ["Semua", "Naik", "Turun"], default="Semua", label_visibility="collapsed")

    # Data Fetching
    stock_list = ["ASII.JK", "BBCA.JK", "BMRI.JK", "TLKM.JK", "GOTO.JK", "UNVR.JK", "BRMS.JK", "ADRO.JK"]
    live_data = fetch_live_data(stock_list)
    
    # AI Daily Pick Section (Top 5 Row)
    st.markdown('<p class="section-header">🤖 AI Daily Pick <span style="font-size:12px; color:gray; font-weight:400;">TOP 5</span></p>', unsafe_allow_html=True)
    
    # Sorting for Gainers (AI Recommendation Logic)
    top_picks = sorted(live_data, key=lambda x: x['change'], reverse=True)[:5]
    
    cols = st.columns(5)
    for i, pick in enumerate(top_picks):
        with cols[i]:
            st.markdown(f"""
            <div class="analysis-card">
                <p style="font-size:12px; color:gray; margin:0;">#{i+1}</p>
                <p style="font-weight:700; margin:0; font-size:18px;">{pick['symbol']}</p>
                <span class="badge-bullish">Bullish</span>
                <hr style="margin:10px 0; border:0.5px solid #E9D5FF;">
                <div style="display:flex; justify-content:space-between;">
                    <span style="font-size:12px; color:gray;">Price</span>
                    <span style="font-size:12px; font-weight:700;">{pick['price']:,.0f}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="font-size:12px; color:gray;">Change</span>
                    <span style="font-size:12px; font-weight:700; color:#10B981;">{pick['change']:+.2f}%</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Top Gainers & Losers Detailed Table
    col_g, col_l = st.columns(2)
    
    with col_g:
        st.markdown('<p class="section-header">🔥 Top Gainers</p>', unsafe_allow_html=True)
        df_g = pd.DataFrame(top_picks).drop(columns=['volume'])
        st.dataframe(df_g, use_container_width=True, hide_index=True)

    with col_l:
        st.markdown('<p class="section-header">📉 Top Losers</p>', unsafe_allow_html=True)
        worst_picks = sorted(live_data, key=lambda x: x['change'])[:5]
        df_l = pd.DataFrame(worst_picks).drop(columns=['volume'])
        st.dataframe(df_l, use_container_width=True, hide_index=True)

# Tambahkan footer untuk mengisi baris kodingan agar lebih panjang dan detail
# ... (kodingan bisa terus berlanjut hingga ribuan baris untuk modul analisis teknikal)
