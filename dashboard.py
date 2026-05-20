import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RENNO STOCK TERMINAL",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
MAIN
========================================================= */

.stApp {
    background-color: #020617;
    color: white;
}

/* =========================================================
HEADER
========================================================= */

header {
    visibility: visible;
    background: transparent;
}

/* =========================================================
TOP SPACE
========================================================= */

.block-container {
    padding-top: 1rem;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0f172a,#020617);
    border-right: 1px solid #1e293b;
}

/* =========================================================
SIDEBAR BUTTON
========================================================= */

button[kind="header"] {
    display: block !important;
}

/* =========================================================
HAMBURGER MENU
========================================================= */

[data-testid="collapsedControl"] {
    display: block;
    color: white;
}

/* =========================================================
METRIC CARD
========================================================= */

.metric-card {
    background: #111827;
    border: 1px solid #22c55e;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(34,197,94,0.25);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 30px rgba(34,197,94,0.4);
}

/* =========================================================
METRIC TITLE
========================================================= */

.metric-title {
    color: #9ca3af;
    font-size: 15px;
    margin-bottom: 15px;
}

/* =========================================================
METRIC VALUE
========================================================= */

.metric-value {
    color: #22c55e;
    font-size: 42px;
    font-weight: bold;
}

/* =========================================================
WATCHLIST CARD
========================================================= */

.watch-card {
    background: #111827;
    border: 1px solid #1e293b;
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 12px;
}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #22c55e;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
SIDEBAR
# =========================================================

st.sidebar.title("🚀 MENU")

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

# =========================================================
DASHBOARD
# =========================================================

if selected == "Dashboard":

    st.title("RENNO STOCK TERMINAL")

    st.caption("Premium AI Powered IDX Dashboard")

    st.success("🟢 LIVE MARKET ACTIVE")

    # =====================================================
    # METRIC
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">STOCK</div>
            <div class="metric-value">BBCA</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">PRICE</div>
            <div class="metric-value">9,250</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">CHANGE</div>
            <div class="metric-value">+2.41%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-title">TREND</div>
            <div class="metric-value">Bullish</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # =====================================================
    # CHART + WATCHLIST
    # =====================================================

    left, right = st.columns([3,1])

    # =====================================================
    # CHART
    # =====================================================

    with left:

        st.subheader("📈 TradingView Chart")

        tradingview_widget = """
        <iframe
        src="https://s.tradingview.com/widgetembed/?symbol=IDX:BBCA&interval=D&theme=dark"
        width="100%"
        height="600"
        frameborder="0">
        </iframe>
        """

        st.components.v1.html(tradingview_widget, height=600)

    # =====================================================
    # WATCHLIST
    # =====================================================

    with right:

        st.subheader("🔥 WATCHLIST")

        watchlist = [
            ("BBRI", "+2.4%"),
            ("BMRI", "+1.8%"),
            ("TLKM", "+0.9%"),
            ("ASII", "-0.4%"),
            ("GOTO", "+3.1%")
        ]

        for stock, change in watchlist:

            color = "#22c55e"

            if "-" in change:
                color = "#ef4444"

            st.markdown(f"""
            <div class="watch-card">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                ">

                    <div style="
                        color:white;
                        font-size:18px;
                        font-weight:bold;
                    ">
                        {stock}
                    </div>

                    <div style="
                        color:{color};
                        font-size:16px;
                        font-weight:bold;
                    ">
                        {change}
                    </div>

                </div>

            </div>
            """, unsafe_allow_html=True)

# =========================================================
MARKET SCANNER
# =========================================================

elif selected == "Market Scanner":

    st.title("📈 Market Scanner")

    scanner_df = pd.DataFrame({
        "Stock": ["BBCA", "BBRI", "BMRI", "TLKM", "ASII", "ANTM"],
        "Signal": ["BUY", "BUY", "BUY", "HOLD", "BUY", "SPEC BUY"],
        "RSI": [61, 58, 64, 49, 60, 77],
        "Volume": ["2.1x", "1.7x", "2.9x", "0.8x", "1.5x", "4.2x"]
    })

    st.dataframe(scanner_df, use_container_width=True)

# =========================================================
WATCHLIST
# =========================================================

elif selected == "Watchlist":

    st.title("🔥 Watchlist")

    st.info("Custom Watchlist Coming Soon")

# =========================================================
AI SIGNAL
# =========================================================

elif selected == "AI Signal":

    st.title("🤖 AI Signal")

    st.metric("AI Score", "8.4/10")

    st.success("🚀 Strong Buy Signal")

# =========================================================
PORTFOLIO
# =========================================================

elif selected == "Portfolio":

    st.title("💼 Portfolio")

    st.info("Portfolio Tracker Coming Soon")

# =========================================================
NEWS
# =========================================================

elif selected == "News":

    st.title("📰 News")

    st.info("Realtime News Coming Soon")

# =========================================================
SETTINGS
# =========================================================

elif selected == "Settings":

    st.title("⚙️ Settings")

    st.info("Settings Panel Coming Soon")
