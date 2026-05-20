import streamlit as st
import pandas as pd

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="RENNO STOCK TERMINAL",
    page_icon="📈",
    layout="wide"
)

# ============================================
# CSS
# ============================================

st.markdown("""
<style>

/* MAIN */
.stApp {
    background-color: #020617;
    color: white;
}

/* HIDE STREAMLIT */
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

# ============================================
# SIDEBAR
# ============================================

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

# ============================================
# DASHBOARD
# ============================================

if selected == "Dashboard":

    st.title("RENNO STOCK TERMINAL")

    st.caption("Premium AI Powered IDX Dashboard")

    st.success("🟢 LIVE MARKET ACTIVE")

    # ============================================
    # METRIC
    # ============================================

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

    # ============================================
    # CHART
    # ============================================

    st.subheader("📈 TradingView Chart")

    tradingview_widget = """
    <iframe
    src="https://s.tradingview.com/widgetembed/?symbol=IDX:BBCA&interval=D&theme=dark"
    width="100%"
    height="500"
    frameborder="0">
    </iframe>
    """

    st.components.v1.html(tradingview_widget, height=500)

# ============================================
# MARKET SCANNER
# ============================================

elif selected == "Market Scanner":

    st.title("📈 Market Scanner")

    scanner_df = pd.DataFrame({
        "Stock": ["BBCA", "BBRI", "BMRI", "TLKM", "ASII"],
        "Signal": ["BUY", "BUY", "BUY", "HOLD", "BUY"],
        "RSI": [61, 58, 64, 49, 60]
    })

    st.dataframe(scanner_df, use_container_width=True)

# ============================================
# WATCHLIST
# ============================================

elif selected == "Watchlist":

    st.title("🔥 Watchlist")

    st.info("Watchlist Coming Soon")

# ============================================
# AI SIGNAL
# ============================================

elif selected == "AI Signal":

    st.title("🤖 AI Signal")

    st.metric("AI Score", "8.4/10")

# ============================================
# PORTFOLIO
# ============================================

elif selected == "Portfolio":

    st.title("💼 Portfolio")

    st.info("Portfolio Coming Soon")

# ============================================
# NEWS
# ============================================

elif selected == "News":

    st.title("📰 News")

    st.info("Realtime News Coming Soon")

# ============================================
# SETTINGS
# ============================================

elif selected == "Settings":

    st.title("⚙️ Settings")

    st.info("Settings Coming Soon")
