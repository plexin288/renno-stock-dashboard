# =================================================
# RENNO STOCK TERMINAL
# =================================================

import streamlit as st
import pandas as pd

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="RENNO STOCK TERMINAL",
    page_icon="📈",
    layout="wide"
)

# =================================================
# CUSTOM CSS
# =================================================

st.markdown("""
<style>

/* MAIN */
.stApp {
    background-color: #020617;
    color: white;
}

/* REMOVE STREAMLIT HEADER */
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
    background: linear-gradient(180deg,#0f172a,#020617);
    border-right: 1px solid #1e293b;
}

/* METRIC CARD */
.metric-card {
    background: #111827;
    border: 1px solid #22c55e;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 0 20px rgba(34,197,94,0.25);
}

/* METRIC TITLE */
.metric-title {
    color: #9ca3af;
    font-size: 14px;
}

/* METRIC VALUE */
.metric-value {
    color: #22c55e;
    font-size: 42px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =================================================
# SIDEBAR
# =================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2721/2721268.png",
    width=120
)

st.sidebar.markdown("## 🚀 MENU")

selected = st.sidebar.radio(
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

# =================================================
# DASHBOARD PAGE
# =================================================

if selected == "Dashboard":

    st.title("RENNO STOCK TERMINAL")

    st.caption("Premium AI Powered IDX Dashboard")

    st.success("🟢 LIVE MARKET ACTIVE")

    # =================================================
    # METRIC
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">
                STOCK
            </div>

            <div class="metric-value">
                BBCA
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">
                PRICE
            </div>

            <div class="metric-value">
                9,250
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">
                CHANGE
            </div>

            <div class="metric-value">
                +2.41%
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">
                TREND
            </div>

            <div class="metric-value">
                Bullish
            </div>
        </div>
        """, unsafe_allow_html=True)

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
        <iframe
        src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_chart&symbol=IDX:BBCA&interval=D&theme=dark&style=1&locale=en&toolbarbg=f1f3f6&hide_top_toolbar=false&saveimage=false"
        width="100%"
        height="500"
        frameborder="0"
        allowtransparency="true"
        scrolling="no">
        </iframe>
        """

        st.components.v1.html(tradingview_widget, height=500)

    # =================================================
    # WATCHLIST
    # =================================================

    with right:

        st.subheader("🔥 WATCHLIST")

        watchlist = [
            ("BBRI", "+2.4%"),
            ("TLKM", "+1.1%"),
            ("ASII", "+0.9%"),
            ("BMRI", "+3.2%"),
            ("GOTO", "-1.2%")
        ]

        for stock, change in watchlist:

            color = "#22c55e"

            if "-" in change:
                color = "#ef4444"

            st.markdown(f"""
            <div style="
                background:#111827;
                border:1px solid #1e293b;
                padding:15px;
                border-radius:14px;
                margin-bottom:10px;
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
                        font-size:16px;
                        font-weight:bold;
                        color:{color};
                    ">
                        {change}
                    </div>

                </div>
            </div>
            """, unsafe_allow_html=True)

# =================================================
# MARKET SCANNER PAGE
# =================================================

elif selected == "Market Scanner":

    st.title("📈 Market Scanner")

    scanner_df = pd.DataFrame({
        "Stock": ["BBCA", "BBRI", "BMRI", "TLKM", "ASII", "ANTM", "GOTO"],
        "Signal": ["BUY", "BUY", "BUY", "HOLD", "BUY", "BUY", "SPEC BUY"],
        "RSI": [61, 58, 64, 49, 60, 72, 77],
        "Volume": ["2.1x", "1.7x", "2.9x", "0.8x", "1.5x", "3.4x", "4.2x"]
    })

    st.dataframe(scanner_df, use_container_width=True)

# =================================================
# WATCHLIST PAGE
# =================================================

elif selected == "Watchlist":

    st.title("🔥 Watchlist")

    st.info("Custom Watchlist Coming Soon")

# =================================================
# AI SIGNAL PAGE
# =================================================

elif selected == "AI Signal":

    st.title("🤖 AI Signal")

    st.metric("Average AI Score", "8.4/10")

    st.success("Top Signal Today: BBRI")

# =================================================
# PORTFOLIO PAGE
# =================================================

elif selected == "Portfolio":

    st.title("💼 Portfolio")

    st.info("Portfolio Tracker Coming Soon")

# =================================================
# NEWS PAGE
# =================================================

elif selected == "News":

    st.title("📰 News")

    st.info("Realtime Market News Coming Soon")

# =================================================
# SETTINGS PAGE
# =================================================

elif selected == "Settings":

    st.title("⚙️ Settings")

    st.info("Settings Panel Coming Soon")
