import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="RENNO STOCK TERMINAL",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    margin: 0;
    padding: 0;
}

.stApp {
    margin-top: -95px;
}

/* MAIN */
.stApp {
    background-color: #020617;
    color: white;
}

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

/* REMOVE TOP SPACE */
.block-container {
    padding-top: 1rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #111827);
    border-right: 1px solid #1e293b;
}

/* SIDEBAR BUTTON */
[data-testid="collapsedControl"] {
    background-color: #1e293b !important;
    border-radius: 12px !important;
    padding: 8px !important;
    transform: scale(1.4);
}

[data-testid="collapsedControl"] svg {
    color: #60a5fa !important;
}

/* METRIC CARD */
[data-testid="metric-container"] {
    background: linear-gradient(145deg,#111827,#1e293b);
    border: 1px solid #374151;
    border-radius: 18px;
    padding: 15px;
}

/* TABLE */
[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
        width=120
    )

    st.markdown("## 🚀 MENU")

    selected = st.radio(
        "",
        [
            "Dashboard",
            "Market Scanner",
            "Watchlist",
            "AI Signal",
            "Portfolio",
            "News",
            "Settings"
        ]
    )

# =====================================================
# DASHBOARD
# =====================================================

if selected == "Dashboard":

    st.title("RENNO STOCK TERMINAL")
    st.caption("Premium AI Powered IDX Dashboard")

    st.success("🟢 LIVE MARKET ACTIVE")

    # =================================================
    # METRIC
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("STOCK", "BBCA")

    with col2:
        st.metric("PRICE", "9,250")

    with col3:
        st.metric("CHANGE", "+2.41%")

    with col4:
        st.metric("TREND", "Bullish")

    st.write("")

    # =================================================
    # CHART + WATCHLIST
    # =================================================

    left, right = st.columns([3,1])

    # =================================================
    # CHART
    # =================================================

    with left:

        st.subheader("📈 TradingView Chart")

        tradingview_widget = """
        <div class="tradingview-widget-container">

          <div id="tradingview_chart"></div>

          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>

          <script type="text/javascript">

          new TradingView.widget(
          {
            "width": "100%",
            "height": 620,
            "symbol": "IDX:BBCA",
            "interval": "D",
            "timezone": "Asia/Jakarta",
            "theme": "dark",
            "style": "1",
            "locale": "id",
            "toolbar_bg": "#0f172a",
            "enable_publishing": false,
            "hide_top_toolbar": false,
            "save_image": false,
            "container_id": "tradingview_chart"
          }
          );

          </script>

        </div>
        """

        html(tradingview_widget, height=650)

    # =================================================
    # WATCHLIST
    # =================================================

    with right:

        st.subheader("🔥 WATCHLIST")

        watchlist_df = pd.DataFrame({
            "Stock": ["BBRI", "BMRI", "TLKM", "ANTM", "GOTO"],
            "Change": ["+1.21%", "+3.11%", "-0.51%", "+5.22%", "+7.11%"]
        })

        for i, row in watchlist_df.iterrows():

            stock = row["Stock"]
            change = row["Change"]

            color = "#22c55e" if "+" in change else "#ef4444"

            card_html = f'''
            <div style="
                background: linear-gradient(145deg,#111827,#1e293b);
                padding:16px;
                border-radius:16px;
                border:1px solid #374151;
                margin-bottom:12px;
                box-shadow:0 0 15px rgba(0,0,0,0.25);
            ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                ">

                    <div style="
                        font-size:18px;
                        font-weight:bold;
                        color:white;
                    ">
                        {stock}
                    </div>

                    <div style="
                        font-size:15px;
                        font-weight:bold;
                        color:{color};
                    ">
                        {change}
                    </div>

                </div>

            </div>
            '''

            st.markdown(card_html, unsafe_allow_html=True)

        st.write("")

        # =============================================
        # AI SIGNAL
        # =============================================

        st.subheader("🤖 AI SIGNAL")

        st.metric(
            "AI SCORE",
            "8/10"
        )

        st.success("🚀 STRONG BUY")

        st.write("✅ MACD Bullish")
        st.write("✅ RSI Healthy")
        st.write("✅ Volume Surge")
        st.write("✅ Price Above MA20")

    st.write("")

    # =================================================
    # MARKET SCANNER TABLE
    # =================================================

    st.subheader("📋 MARKET SCANNER")

    scanner_df = pd.DataFrame({
        "Stock": ["BBCA", "BBRI", "BMRI", "TLKM", "ASII"],
        "Price": [9250, 5100, 6450, 3820, 4900],
        "Change": ["+2.41%", "+1.11%", "+0.91%", "-0.31%", "+1.44%"],
        "Trend": ["Bullish", "Bullish", "Bullish", "Neutral", "Bullish"]
    })

    st.dataframe(scanner_df, use_container_width=True)

# =====================================================
# MARKET SCANNER PAGE
# =====================================================

elif selected == "Market Scanner":

    st.title("📈 Market Scanner")

    scanner_df = pd.DataFrame({
        "Stock": ["BBCA", "BBRI", "BMRI", "TLKM", "ASII", "ANTM", "GOTO"],
        "Signal": ["BUY", "BUY", "BUY", "HOLD", "BUY", "BUY", "SPEC BUY"],
        "RSI": [61, 58, 64, 49, 60, 72, 77],
        "Volume": ["2.1x", "1.7x", "2.9x", "0.8x", "1.5x", "3.4x", "4.2x"]
    })

    st.dataframe(scanner_df, use_container_width=True)

# =====================================================
# WATCHLIST PAGE
# =====================================================

elif selected == "Watchlist":

    st.title("🔥 Watchlist")

    st.info("Custom Watchlist Coming Soon")

# =====================================================
# AI SIGNAL PAGE
# =====================================================

elif selected == "AI Signal":

    st.title("🤖 AI Signal")

    st.metric("Average AI Score", "8.4/10")

    st.success("Top Signal Today: BBRI")

# =====================================================
# PORTFOLIO PAGE
# =====================================================

elif selected == "Portfolio":

    st.title("💼 Portfolio")

    st.info("Portfolio Tracker Coming Soon")

# =====================================================
# NEWS PAGE
# =====================================================

elif selected == "News":

    st.title("📰 Market News")

    st.info("BBCA reports strong quarterly earnings")
    st.info("Foreign flow returns to IDX banking sector")
    st.info("Coal sector gains momentum this week")

# =====================================================
# SETTINGS PAGE
# =====================================================

elif selected == "Settings":

    st.title("⚙️ Settings")

    st.toggle("Dark Mode", value=True)
    st.toggle("Telegram Alert", value=True)
    st.toggle("Realtime Scanner", value=True)
