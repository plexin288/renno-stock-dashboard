import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="RENNO TERMINAL",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS SIMPLE & STABLE
# =========================================================

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: #0b1120;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1f2937;
}

/* TEXT */
html, body, [class*="css"] {
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* METRIC */
[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );

    border: 1px solid #374151;

    padding: 20px;

    border-radius: 22px;

    box-shadow:
        0 0 20px rgba(59,130,246,0.15);
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
}

/* BUTTON */
.stButton>button {

    background: linear-gradient(
        135deg,
        #7c3aed,
        #4f46e5
    );

    color: white;

    border: none;

    border-radius: 12px;

    padding: 10px 20px;

    font-weight: bold;
}

/* SELECTBOX */
.stSelectbox div[data-baseweb="select"] {

    background: #1e293b;

    border-radius: 12px;
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
        "ANTM",
        "GOTO"
    ]
)

timeframe = st.sidebar.selectbox(
    "Select Timeframe",
    [
        "1D",
        "1W",
        "1M",
        "3M",
        "1Y"
    ]
)

st.sidebar.write("")

st.sidebar.success("🟢 MARKET OPEN")

# =========================================================
# HEADER
# =========================================================

st.title("RENNO STOCK TERMINAL")

st.caption("Premium AI Powered IDX Dashboard")

st.success("🟢 LIVE MARKET ACTIVE")

st.write("")

# =========================================================
# METRICS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="Stock",
        value=stock
    )

with col2:

    st.metric(
        label="Price",
        value="9,250"
    )

with col3:

    st.metric(
        label="Change",
        value="+2.41%"
    )

with col4:

    st.metric(
        label="Trend",
        value="Bullish"
    )

# =========================================================
# MAIN LAYOUT
# =========================================================

left, right = st.columns([2.3, 1])

# =========================================================
# LEFT SIDE
# =========================================================

with left:

    st.subheader("📈 TradingView Chart")

    tradingview_chart = f"""
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

        "toolbar_bg": "#0b1120",

        "enable_publishing": false,

        "allow_symbol_change": true,

        "container_id": "tradingview_chart"

      }});

      </script>

    </div>
    """

    components.html(
        tradingview_chart,
        height=650
    )

    st.write("")

    st.subheader("🤖 AI SIGNAL")

    signal_col1, signal_col2 = st.columns(2)

    with signal_col1:

        st.metric(
            label="AI SCORE",
            value="8/10"
        )

    with signal_col2:

        st.metric(
            label="Signal",
            value="🚀 STRONG BUY"
        )

# =========================================================
# RIGHT SIDE
# =========================================================

with right:

    st.subheader("🔥 Watchlist")

    watchlist_df = pd.DataFrame({

        "Stock": [
            "BBRI",
            "BMRI",
            "TLKM",
            "ANTM",
            "GOTO"
        ],

        "Change": [
            "+1.21%",
            "+3.11%",
            "-0.51%",
            "+5.22%",
            "+7.11%"
        ]

    })

    st.dataframe(
        watchlist_df,
        use_container_width=True
    )

    st.write("")

    st.subheader("📊 Market Status")

    st.metric(
        label="IHSG",
        value="7,102",
        delta="+1.22%"
    )

# =========================================================
# MARKET SCANNER
# =========================================================

st.write("")

st.subheader("📋 Market Scanner")

scanner_df = pd.DataFrame({

    "Stock": [
        "BBCA",
        "BMRI",
        "BBRI",
        "TLKM",
        "ANTM"
    ],

    "Price": [
        9250,
        6450,
        4850,
        3200,
        1620
    ],

    "Change": [
        "+2.41%",
        "+3.11%",
        "+1.21%",
        "-0.51%",
        "+5.22%"
    ],

    "Trend": [
        "Bullish",
        "Bullish",
        "Bullish",
        "Bearish",
        "Bullish"
    ],

    "Volume": [
        "12.45M",
        "15.21M",
        "18.32M",
        "25.11M",
        "22.17M"
    ]

})

st.dataframe(
    scanner_df,
    use_container_width=True
)
