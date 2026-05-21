import streamlit as st
import pandas as pd
import yfinance as yf
import requests

# 1. KONFIGURASI HALAMAN & TEMA (PUTIH + UNGU MUDA)
st.set_page_config(page_title="StockAI Premium", layout="wide")

st.markdown("""
<style>
    /* Background Utama Putih */
    .stApp { background-color: #FFFFFF; }
    
    /* Sidebar Ungu Muda */
    [data-testid="stSidebar"] { background-color: #F3E8FF; }
    
    /* Tombol & Highlight Ungu */
    .stButton>button { background-color: #A855F7; color: white; border-radius: 8px; }
    
    /* Card Style */
    .metric-card { 
        background: #FFFFFF; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #E9D5FF; 
        box-shadow: 2px 2px 10px rgba(168, 85, 247, 0.05);
    }
    
    h1, h2, h3 { color: #6B21A8; } /* Font Ungu Gelap */
</style>
""", unsafe_allow_html=True)

# 2. FUNGSI PENARIK DATA (Satu Pintu Agar Tidak Error N/A)
@st.cache_data(ttl=300)
def get_stock_data(tickers):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    data_list = []
    
    for t in tickers:
        try:
            # Tarik data period 7d untuk antisipasi market tutup
            df = yf.download(t, period="7d", interval="1d", session=session, progress=False)
            df = df[df['Close'] > 0].dropna()
            
            if len(df) >= 2:
                curr = float(df['Close'].iloc[-1])
                prev = float(df['Close'].iloc[-2])
                chg = ((curr - prev) / prev) * 100
                data_list.append({
                    'ticker': t.replace(".JK", ""),
                    'price': f"{curr:,.0f}",
                    'pct': f"{chg:+.2f}%",
                    'raw_chg': chg
                })
        except:
            continue
    return data_list

# 3. SIDEBAR MENU (Sesuai gambar instruksi)
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🚀 StockAI</h1>", unsafe_allow_html=True)
    menu = st.radio("MENU UTAMA", ["Dashboard", "Stocks Journal", "Bedah Saham", "Market Overview"])
    st.markdown("---")
    st.button("✨ Upgrade VIP")

# 4. LOGIKA HALAMAN DASHBOARD
if menu == "Dashboard":
    st.title("Alpha Intelligence — Stock Analysis")
    st.write("Analisis saham IDX menggunakan data real-time.")

    # Ambil data untuk Watchlist & Gainers
    # Kita ambil beberapa saham populer dulu sebagai contoh
    stocks_to_watch = ["BBCA.JK", "BMRI.JK", "TLKM.JK", "ASII.JK", "UNVR.JK", "GOTO.JK", "BRMS.JK", "ADRO.JK"]
    all_data = get_stock_data(stocks_to_watch)
    
    # Sorting untuk Top Gainers & Losers
    top_gainers = sorted(all_data, key=lambda x: x['raw_chg'], reverse=True)[:3]
    top_losers = sorted(all_data, key=lambda x: x['raw_chg'])[:3]

    # Baris 1: Top Gainers & Losers Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔥 Top Gainers")
        cols = st.columns(3)
        for i, stock in enumerate(top_gainers):
            with cols[i]:
                st.markdown(f"""
                <div class='metric-card'>
                    <p style='margin:0; font-weight:bold;'>{stock['ticker']}</p>
                    <h3 style='margin:0; color:#10B981;'>{stock['pct']}</h3>
                    <p style='margin:0; font-size:12px;'>Rp {stock['price']}</p>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.subheader("📉 Top Losers")
        cols = st.columns(3)
        for i, stock in enumerate(top_losers):
            with cols[i]:
                st.markdown(f"""
                <div class='metric-card'>
                    <p style='margin:0; font-weight:bold;'>{stock['ticker']}</p>
                    <h3 style='margin:0; color:#EF4444;'>{stock['pct']}</h3>
                    <p style='margin:0; font-size:12px;'>Rp {stock['price']}</p>
                </div>
                """, unsafe_allow_html=True)
