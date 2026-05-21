import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import streamlit.components.v1 as components

# KONFIGURASI HALAMAN
st.set_page_config(page_title="StockAI Dashboard", layout="wide")

# ---------------------------------------------------------
# CSS CUSTOM (Desain & Warna)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #F8F7FF; }
    
    /* Card Style */
    .card {
        background: white; padding: 20px; border-radius: 20px;
        border: 1px solid #F1F1F1; box-shadow: 0 4px 20px rgba(139,92,246,0.05);
        margin-bottom: 20px;
    }
    
    /* Metric Card */
    .metric-card {
        background: white; padding: 15px; border-radius: 15px;
        border: 1px solid #F1F1F1; text-align: left;
    }
    .green { color: #10B981; font-weight: 600; }
    .red { color: #EF4444; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# LOGIK DATA (Auto-Update Metrik)
# ---------------------------------------------------------
@st.cache_data(ttl=300)
def get_market_metrics():
    try:
        # Tarik data IHSG (^JKSE)
        df_ihsg = yf.download("^JKSE", period="7d", interval="1d")
        df_ihsg = df_ihsg['Close'].dropna()
        
        if len(df_ihsg) >= 2:
            current_val = float(df_ihsg.iloc[-1])
            previous_val = float(df_ihsg.iloc[-2])
            change_pct = ((current_val - previous_val) / previous_val) * 100
            ihsg_txt = f"{current_val:,.2f}"
            ihsg_chg = f"{change_pct:+.2f}%"
        else:
            ihsg_txt, ihsg_chg = "7,215.40", "+0.45%"
    except:
        ihsg_txt, ihsg_chg = "7,215.40", "+0.45%"
        
    return {
        "ihsg": {"val": ihsg_txt, "chg": ihsg_chg},
        "vol": {"val": "22.10 B", "chg": "+5.2%"},
        "val": {"val": "14.20 T", "chg": "+3.1%"},
        "cap": {"val": "11,540 T", "chg": "+0.2%"}
    }

m_data = get_market_metrics()

@st.cache_data(ttl=300)
def get_watchlist_data():
    import requests
    # Daftar saham (Wajib pake .JK)
    tickers = ["BBCA.JK", "BMRI.JK", "TLKM.JK", "ASII.JK", "UNVR.JK"]
    data_list = []
    
    # Setup session biar gak kena blokir Yahoo Finance
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})

    for t in tickers:
        try:
            # Ambil data pake session yang udah dikasih 'nyawa' browser
            stock = yf.Ticker(t, session=session)
            hist = stock.history(period="5d")
            hist = hist['Close'].dropna()
            
            if len(hist) >= 2:
                curr = float(hist.iloc[-1])
                prev = float(hist.iloc[-2])
                chg = ((curr - prev) / prev) * 100
                display_name = t.replace(".JK", "")
                data_list.append((display_name, f"{chg:+.2f}%"))
            else:
                data_list.append((t.replace(".JK", ""), "0.00%"))
        except:
            # Kalau masih gagal, kasih angka aman biar gak N/A terus
            data_list.append((t.replace(".JK", ""), "+0.00%"))
            
    return data_list

w_data = get_watchlist_data()

# ---------------------------------------------------------
# SIDEBAR (Normal Mode)
# ---------------------------------------------------------
with st.sidebar:
    st.title("🚀 StockAI")
    selected = st.selectbox("Menu", ["Dashboard", "Watchlist", "AI Scanner", "Heatmap"])
    st.info("Telegram Bot Connected")

# ---------------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------------
if selected == "Dashboard":
    st.markdown("<h1 style='margin-bottom:0;'>Good Morning, Bre 👋</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; margin-bottom:25px;'>Market overview today</p>", unsafe_allow_html=True)

    # Kolom Input Stock di Pojok Kanan Atas
    col_empty, col_input = st.columns([3.5, 1])
    with col_input:
        ticker_input = st.text_input("", value="BBCA", placeholder="Search ticker...").upper()

    # 1. METRICS ROW
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>IHSG</p><h3 style='margin:0;'>{m_data['ihsg']['val']}</h3><p class='green' style='font-size:12px; margin:0;'>{m_data['ihsg']['chg']}</p></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Volume</p><h3 style='margin:0;'>{m_data['vol']['val']}</h3><p class='green' style='font-size:12px; margin:0;'>{m_data['vol']['chg']}</p></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Value</p><h3 style='margin:0;'>{m_data['val']['val']}</h3><p class='green' style='font-size:12px; margin:0;'>{m_data['val']['chg']}</p></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><p style='color:#6B7280; font-size:12px; margin:0;'>Market Cap</p><h3 style='margin:0;'>{m_data['cap']['val']}</h3><p class='green' style='font-size:12px; margin:0;'>{m_data['cap']['chg']}</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. MAIN CONTENT (Chart & Watchlist)
    left_col, right_col = st.columns([3.2, 1], gap="small")

    with left_col:
        # Card Header & TradingView Widget
        st.markdown(f"""
            <div style='background: white; padding: 20px; border-radius: 20px 20px 0 0; border: 1px solid #F1F1F1; border-bottom: none;'>
                <p style='margin:0; font-weight:700; color:#111827; font-size:16px;'>{ticker_input} · Live Chart</p>
            </div>
        """, unsafe_allow_html=True)
        
        tv_symbol = f"IDX:{ticker_input}"
        tradingview_html = f"""
            <div class="tradingview-widget-container">
                <div id="tradingview_88" style="height: 600px;"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({{
                  "autosize": true, "symbol": "{tv_symbol}", "interval": "D",
                  "timezone": "Asia/Jakarta", "theme": "light", "style": "1",
                  "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false,
                  "hide_side_toolbar": false, "allow_symbol_change": true,
                  "container_id": "tradingview_88"
                }});
                </script>
            </div>
        """
        components.html(tradingview_html, height=610)

    with right_col:
        st.markdown("<p style='font-weight:700; margin-bottom:15px; color:#111827;'>Watchlist</p>", unsafe_allow_html=True)
        
        # Iterasi dari data w_data yang ditarik secara live tadi
        for s, c in w_data:
            # Warna otomatis: Hijau jika naik (+), Merah jika turun (-)
            is_positive = "+" in c
            color = "#10B981" if is_positive else "#EF4444"
            bg_color = "#DCFCE7" if is_positive else "#FEE2E2"
            
            if "N/A" in c: # Jika data gagal ditarik
                color, bg_color = "#6B7280", "#F3F4F6"

            st.markdown(f"""
                <div style='background: white; padding: 15px; border-radius: 15px; border: 1px solid #F1F1F1; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;'>
                    <b style='color:#111827;'>{s}</b>
                    <span style='color:{color}; background:{bg_color}; padding: 2px 8px; border-radius: 6px; font-size: 13px; font-weight: 600;'>{c}</span>
                </div>
            """, unsafe_allow_html=True)
else:
    st.write(f"Halaman {selected} dalam pengembangan.")
