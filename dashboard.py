import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RENNO TERMINAL",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0f172a;
    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1f2937;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* CARD */

.custom-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 20px;

    box-shadow:
        0 0 20px rgba(0,0,0,0.25);
}

/* GLOW */

.glow {

    box-shadow:
        0 0 25px rgba(99,102,241,0.35);
}

/* TITLE */

.big-title {

    font-size: 54px !important;

    font-weight: 800 !important;

    color: white !important;
}

/* TEXT */

.white-text {

    color: white !important;
}

.green {

    color: #22c55e !important;
}

.red {

    color: #ef4444 !important;
}

/* TABLE */

[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚀 RENNO TERMINAL")

stock = st.sidebar.selectbox(
    "Select Stock",
    [
        "BBCA",
        "BBRI",
        "BMRI",
        "TLKM",
        "ASII",
        "GOTO",
        "ANTM"
    ]
)

timeframe = st.sidebar.selectbox(
    "Select Timeframe",
    [
        "1D",
        "1W",
        "1M",
        "3M"
    ]
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<p class="big-title">RENNO STOCK TERMINAL</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:#94a3b8;">Premium AI Powered IDX Dashboard</p>',
    unsafe_allow_html=True
)

st.success("🟢 LIVE MARKET ACTIVE")

st.write("")

# =========================================================
# METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown('<div class="custom-card glow">', unsafe_allow_html=True)

    st.metric(
        label="Stock",
        value=stock
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    st.metric(
        label="Price",
        value="9,250"
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col3:

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    st.metric(
        label="Change",
        value="+2.41%"
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col4:

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    st.metric(
        label="Trend",
        value="Bullish"
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# MAIN GRID
# =========================================================

left, right = st.columns([2.3, 1])

# =========================================================
# LEFT
# =========================================================

with left:

    st.markdown('<div class="custom-card glow">', unsafe_allow_html=True)

    st.subheader("📈 TradingView Chart")

    tv_chart = f'''
    <div class="tradingview-widget-container">

      <div id="tradingview_chart"></div>

      <script type="text/javascript"
      src="https://s3.tradingview.com/tv.js">
      </script>

      <script type="text/javascript">

      new TradingView.widget({{

        "width": "100%",
        "height": 650,

        "symbol": "IDX:{stock}",

        "interval": "D",

        "timezone": "Asia/Jakarta",

        "theme": "dark",

        "style": "1",

        "locale": "id",

        "toolbar_bg": "#0f172a",

        "enable_publishing": false,

        "allow_symbol_change": true,

        "container_id": "tradingview_chart"

      }});

      </script>

    </div>
    '''

    components.html(tv_chart, height=650)

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="custom-card glow">', unsafe_allow_html=True)

    st.subheader("🤖 AI SIGNAL")

    st.markdown(
        '<h1 class="green">🚀 STRONG BUY</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="white-text">AI SCORE : 8/10</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#94a3b8;">MACD Bullish • RSI Healthy • Volume Surge</p>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RIGHT
# =========================================================

with right:

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

    st.subheader("🔥 Watchlist")

    watchlist = {
        "Stock": [
            "BBCA",
            "BBRI",
            "BMRI",
            "TLKM",
            "ANTM",
            "GOTO"
        ],

        "Change": [
            "+2.41%",
            "+1.22%",
            "+3.11%",
            "-0.51%",
            "+5.22%",
            "+7.11%"
        ]
    }

    st.dataframe(
        watchlist,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="custom-card glow">', unsafe_allow_html=True)

    st.subheader("📊 Market Status")

    st.metric(
        label="IHSG",
        value="7,102",
        delta="+1.22%"
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# MARKET OVERVIEW
# =========================================================

st.write("")

st.markdown('<div class="custom-card glow">', unsafe_allow_html=True)

st.subheader("📋 Market Overview")

market_data = {

    "Stock": [
        "BBCA",
        "BBRI",
        "BMRI",
        "TLKM",
        "ASII",
        "GOTO"
    ],

    "Price": [
        9250,
        4850,
        6450,
        3200,
        5150,
        89
    ],

    "Change": [
        "+2.41%",
        "+1.22%",
        "+3.11%",
        "-0.51%",
        "+0.82%",
        "+7.11%"
    ],

    "Trend": [
        "Bullish",
        "Bullish",
        "Bullish",
        "Bearish",
        "Bullish",
        "Bullish"
    ]
}

st.dataframe(
    market_data,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)
