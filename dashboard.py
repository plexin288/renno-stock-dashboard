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
# MODERN CSS
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

/* MAIN TITLE */

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
}

/* HERO */

.hero-box {
    background: linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    );

    padding: 40px;
    border-radius: 30px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 0 30px rgba(99,102,241,0.25);

    margin-bottom: 25px;
}

/* METRIC CARD */

.metric-card {
    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);

    padding: 28px;

    border-radius: 24px;

    text-align: center;

    transition: 0.3s;

    box-shadow:
        0 0 20px rgba(0,0,0,0.25);
}

.metric-card:hover {

    transform: translateY(-5px);

    box-shadow:
        0 0 30px rgba(99,102,241,0.35);
}

.metric-title {
    color: #94a3b8;
    font-size: 15px;
}

.metric-value {
    font-size: 36px;
    font-weight: 700;
    color: white;
}

.green {
    color: #22c55e;
}

.red {
    color: #ef4444;
}

/* SIGNAL BOX */

.signal-box {

    background: linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    border-radius: 30px;

    padding: 40px;

    color: white;

    text-align: center;

    box-shadow:
        0 0 30px rgba(99,102,241,0.35);
}

/* SECTION */

.section-box {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 25px;

    margin-top: 25px;

    box-shadow:
        0 0 20px rgba(0,0,0,0.2);
}

/* WATCHLIST */

.watch-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 20px;

    margin-bottom: 15px;

    transition: 0.3s;
}

.watch-card:hover {

    transform: scale(1.02);

    box-shadow:
        0 0 20px rgba(99,102,241,0.3);
}

/* BLINK */

.blink {
    animation: blink-animation 1s infinite;
}

@keyframes blink-animation {

    0% {
        opacity: 1;
    }

    50% {
        opacity: 0.4;
    }

    100% {
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# 🚀 RENNO TERMINAL")

stock = st.sidebar.selectbox(
    "Select Stock",
    [
        "BBCA",
        "BBRI",
        "BMRI",
        "TLKM",
        "ASII",
        "GOTO",
        "BRIS",
        "ANTM"
    ]
)

interval = st.sidebar.selectbox(
    "Select Timeframe",
    [
        "1D",
        "1W",
        "1M",
        "3M"
    ]
)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero-box">

    <div class="main-title">
        RENNO STOCK TERMINAL
    </div>

    <div class="sub-title">
        Premium AI Powered IDX Dashboard
    </div>

    <br>

    <div class="blink">
        🟢 REALTIME MARKET ACTIVE
    </div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Stock
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
            Price
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
            Change
        </div>

        <div class="metric-value green">
            +2.41%
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">
            Trend
        </div>

        <div class="metric-value green">
            Bullish
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MAIN GRID
# =========================================================

left, right = st.columns([2.3, 1])

# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.markdown("""
    <div class="section-box">
    """, unsafe_allow_html=True)

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

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="signal-box">

        <h1>
            🚀 STRONG BUY
        </h1>

        <h2>
            AI SCORE 8/10
        </h2>

        <p>
            MACD Bullish • RSI Healthy • Volume Surge
        </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.markdown("""
    <div class="section-box">
    """, unsafe_allow_html=True)

    st.subheader("🔥 Watchlist")

    watchlist = [

        ("BBCA", "+2.41%"),
        ("BBRI", "+1.82%"),
        ("BMRI", "+3.11%"),
        ("TLKM", "-0.51%"),
        ("ANTM", "+5.22%"),
        ("GOTO", "+7.11%")

    ]

    for symbol, change in watchlist:

        color = "green" if "+" in change else "red"

        st.markdown(f"""
        <div class="watch-card">

            <h3>
                {symbol}
            </h3>

            <div class="{color}">
                {change}
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="section-box">

        <h2>
            📊 AI Signal
        </h2>

        <br>

        <h1 style="
            color:#22c55e;
        ">
            BUY
        </h1>

        <p>
            Market momentum still strong.
        </p>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MARKET OVERVIEW
# =========================================================

st.markdown("""
<div class="section-box">

<h2>
📋 Market Overview
</h2>

</div>
""", unsafe_allow_html=True)

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
        "+1.21%",
        "+3.11%",
        "-0.51%",
        "+0.87%",
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
