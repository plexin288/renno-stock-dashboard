import streamlit as st
import feedparser
import requests
import streamlit.components.v1 as components
import pandas as pd
from streamlit_option_menu import option_menu

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RENNO TERMINAL",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="collapsedControl"] {
    z-index: 999999 !important;
}

.block-container {
    padding-top: 1rem;
}

/* MAIN BACKGROUND */
.stApp {
    background-color: #0b1120;
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

/* METRIC CARD */
[data-testid="metric-container"] {

    background: linear-gradient(
        135deg,
        #111827,
        #1e293b
    );

    border: 1px solid #374151;

    padding: 18px;

    border-radius: 20px;

    box-shadow:
        0 0 15px rgba(59,130,246,0.15);
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

/* TITLE */
.big-title {

    font-size: 50px;

    font-weight: 800;

    color: white;
}

/* SUBTITLE */
.sub-title {

    color: #9ca3af;

    font-size: 18px;
}

/* GLOW */
.glow {

    color: #8b5cf6;

    font-weight: bold;
}

/* REMOVE TOP SPACE */
.block-container {
    padding-top: 1rem;
}

[data-testid="collapsedControl"] {

    transform: scale(1.15);

    background-color: rgba(255,255,255,0.12) !important;

    border-radius: 12px;

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

selected = "Dashboard"

with st.sidebar:

    st.image("logo.png", width=180)

    selected = option_menu(

        menu_title="MENU",

        options=[
            "Dashboard",
            "Market Scanner",
            "Watchlist",
            "AI Signal",
            "News",
            "Portfolio",
            "Settings"
        ],

        icons=[
            "house",
            "bar-chart",
            "star",
            "robot",
            "newspaper",
            "briefcase",
            "gear"
        ],

        menu_icon="rocket",

        default_index=0,

        styles={

            "container": {
                "padding": "0!important",
                "background-color": "#111827",
            },

            "icon": {
                "color": "#8b5cf6",
                "font-size": "18px"
            },

            "nav-link": {

                "font-size": "16px",

                "text-align": "left",

                "margin": "8px",

                "--hover-color": "#1e293b",

                "border-radius": "12px",

                "color": "white",
            },

            "nav-link-selected": {

                "background":
                "linear-gradient(135deg,#7c3aed,#4f46e5)",

                "font-weight": "bold",
            },
        }
    )

# =========================================================
# DASHBOARD
# =========================================================

if selected == "Dashboard":

    # HEADER

    st.title("RENNO STOCK TERMINAL")

    st.caption("Premium AI Powered IDX Dashboard")

    st.success("🟢 LIVE MARKET ACTIVE")

    st.write("")

    # METRICS

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

    # MAIN SECTION

    left, right = st.columns([2.2, 1])

    # LEFT

    with left:

        st.subheader("📈 TradingView Chart")

        tradingview_chart = """
        <div class="tradingview-widget-container">
          <div id="tradingview_chart"></div>

          <script type="text/javascript"
          src="https://s3.tradingview.com/tv.js">
          </script>

          <script type="text/javascript">

          new TradingView.widget({

            "width": "100%",
            "height": 600,

            "symbol": "IDX:BBCA",

            "interval": "D",

            "timezone": "Asia/Jakarta",

            "theme": "dark",

            "style": "1",

            "locale": "id",

            "toolbar_bg": "#0b1120",

            "enable_publishing": false,

            "allow_symbol_change": true,

            "container_id": "tradingview_chart"

          });

          </script>

        </div>
        """

        components.html(
            tradingview_chart,
            height=600
        )

        st.write("")

        st.subheader("📋 MARKET SCANNER")

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
            ]

        })

        st.dataframe(
            scanner_df,
            use_container_width=True
        )

    # RIGHT

    with right:

        st.subheader("🔥 WATCHLIST")

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

      st.markdown("""
     <style>

.watchlist-card {

    background: linear-gradient(
        145deg,
        #111827,
        #1e293b
    );

    padding: 16px;

    border-radius: 16px;

    border: 1px solid #374151;

    margin-bottom: 12px;

}

.watchlist-stock {

    font-size: 18px;

    font-weight: bold;

    color: white;
}

.watchlist-change {

    font-size: 15px;

    font-weight: bold;

    color: #22c55e;
}

</style>
""", unsafe_allow_html=True)

for i, row in watchlist_df.iterrows():

    st.markdown(f"""
    <div class="watchlist-card">

        <div class="watchlist-stock">
            {row['Stock']}
        </div>

        <div class="watchlist-change">
            {row['Change']}
        </div>

    </div>
    """, unsafe_allow_html=True)

        st.write("")

        st.subheader("🤖 AI SIGNAL")

        st.metric(
            "AI SCORE",
            "8/10"
        )

        st.success("🚀 STRONG BUY")

        st.write("")

        st.write("✅ MACD Bullish")
        st.write("✅ RSI Healthy")
        st.write("✅ Volume Surge")
        st.write("✅ Price Above MA20")

# =========================================================
# OTHER PAGES
# =========================================================

elif selected == "Market Scanner":

    st.title("📈 Market Scanner")

    st.write("Realtime IDX Stock Scanner")

    scanner_df = pd.DataFrame({

        "Stock": [
            "BBCA",
            "BMRI",
            "BBRI",
            "TLKM",
            "ASII",
            "ANTM",
            "GOTO"
        ],

        "Price": [
            9250,
            6450,
            4850,
            3200,
            5150,
            1620,
            89
        ],

        "Change": [
            "+2.41%",
            "+3.11%",
            "+1.21%",
            "-0.51%",
            "+0.87%",
            "+5.22%",
            "+7.11%"
        ],

        "Trend": [
            "Bullish",
            "Bullish",
            "Bullish",
            "Bearish",
            "Bullish",
            "Bullish",
            "Bullish"
        ],

        "Volume": [
            "12.45M",
            "15.21M",
            "18.32M",
            "25.11M",
            "8.12M",
            "22.17M",
            "55.61M"
        ],

        "Value": [
            "1.15T",
            "980B",
            "892B",
            "803B",
            "211B",
            "356B",
            "510B"
        ]

    })

    st.dataframe(
        scanner_df,
        use_container_width=True
    )

    st.write("")

    st.subheader("🔥 Top Gainers")

    gainers_df = pd.DataFrame({

        "Stock": [
            "GOTO",
            "ANTM",
            "BMRI"
        ],

        "Change": [
            "+7.11%",
            "+5.22%",
            "+3.11%"
        ]

    })

    st.dataframe(
        gainers_df,
        use_container_width=True
    )

    st.write("")

    st.subheader("📉 Top Losers")

    losers_df = pd.DataFrame({

        "Stock": [
            "TLKM",
            "UNVR",
            "ICBP"
        ],

        "Change": [
            "-0.51%",
            "-1.12%",
            "-0.77%"
        ]

    })

    st.dataframe(
        losers_df,
        use_container_width=True
    )

elif selected == "Watchlist":

    st.title("🔥 Watchlist")

elif selected == "AI Signal":

    st.title("🤖 AI Signal")

elif selected == "News":

    st.title("📰 Market News")

    st.write("Berita market terbaru hari ini")

    # ======================================
    # RSS NEWS
    # ======================================

    rss_url = "https://www.cnbcindonesia.com/market/rss"

    feed = feedparser.parse(rss_url)

    for entry in feed.entries[:10]:

        st.subheader(entry.title)

        st.caption(entry.published)

        st.write(entry.link)

        st.divider()

    # ======================================
    # MARKET UPDATE
    # ======================================

    st.subheader("📊 Market Update")

    market_data = {

        "Asset": [
            "IHSG",
            "NASDAQ",
            "S&P500",
            "BTC",
            "GOLD"
        ],

        "Change": [
            "+1.22%",
            "+0.88%",
            "+0.74%",
            "+2.51%",
            "-0.12%"
        ]
    }

    st.dataframe(
        market_data,
        use_container_width=True
    )

elif selected == "Portfolio":

    st.title("💼 Portfolio")

elif selected == "Settings":

    st.title("⚙ Settings")
