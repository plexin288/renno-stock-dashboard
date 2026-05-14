import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="RENNO DASHBOARD",
    layout="wide"
)

# =====================================================
# SIMPLE CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.metric-box {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

.green {
    color: #22c55e;
}

.red {
    color: #ef4444;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# STOCK LIST
# =====================================================

stocks = [
    "BBCA.JK",
    "BBRI.JK",
    "BMRI.JK",
    "TLKM.JK",
    "ASII.JK",
    "ANTM.JK",
    "ADRO.JK"
]

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("RENNO TERMINAL")

selected_stock = st.sidebar.selectbox(
    "Select Stock",
    stocks
)

period = st.sidebar.selectbox(
    "Select Period",
    ["1mo", "3mo", "6mo", "1y"],
    index=1
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data(symbol, period):

    df = yf.download(symbol, period=period)

    df.dropna(inplace=True)

    return df

data = load_data(selected_stock, period)

close_series = data["Close"].squeeze()
open_series = data["Open"].squeeze()

# =====================================================
# INDICATORS
# =====================================================

rsi = RSIIndicator(close=close_series)

data["RSI"] = rsi.rsi()

macd = MACD(close=close_series)

data["MACD"] = macd.macd()
data["MACD_SIGNAL"] = macd.macd_signal()

ma20 = SMAIndicator(close=close_series, window=20)

data["MA20"] = ma20.sma_indicator()

ma50 = SMAIndicator(close=close_series, window=50)

data["MA50"] = ma50.sma_indicator()

# =====================================================
# HEADER
# =====================================================

st.title("RENNO STOCK DASHBOARD")

st.write("Simple AI Powered IDX Dashboard")

# =====================================================
# METRICS
# =====================================================

latest_close = float(close_series.iloc[-1])
latest_open = float(open_series.iloc[-1])

change = latest_close - latest_open

change_percent = (change / latest_open) * 100

trend = (
    "Bullish"
    if data["MA20"].iloc[-1] > data["MA50"].iloc[-1]
    else "Bearish"
)

trend_color = "green" if trend == "Bullish" else "red"

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="metric-box">
        <h4>Stock</h4>
        <h2>{selected_stock}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-box">
        <h4>Price</h4>
        <h2>{latest_close:.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:

    color = "green" if change > 0 else "red"

    st.markdown(f"""
    <div class="metric-box">
        <h4>Change</h4>
        <h2 class="{color}">
            {change_percent:.2f}%
        </h2>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="metric-box">
        <h4>Trend</h4>
        <h2 class="{trend_color}">
            {trend}
        </h2>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# TRADINGVIEW
# =====================================================

st.subheader("TradingView Chart")

symbol_tv = selected_stock.replace(".JK", "")

tv_widget = f'''
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>

  <script type="text/javascript"
    src="https://s3.tradingview.com/tv.js">
  </script>

  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": 600,
    "symbol": "IDX:{symbol_tv}",
    "interval": "D",
    "timezone": "Asia/Jakarta",
    "theme": "light",
    "style": "1",
    "locale": "id",
    "toolbar_bg": "#ffffff",
    "enable_publishing": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_chart"
  }}
  );
  </script>
</div>
'''

components.html(tv_widget, height=600)

# =====================================================
# RSI + MACD
# =====================================================

left, right = st.columns(2)

with left:

    st.subheader("RSI")

    rsi_fig = go.Figure()

    rsi_fig.add_trace(go.Scatter(
        x=data.index,
        y=data["RSI"],
        mode="lines",
        name="RSI"
    ))

    rsi_fig.add_hline(y=70)
    rsi_fig.add_hline(y=30)

    rsi_fig.update_layout(
        template="plotly_white",
        height=350
    )

    st.plotly_chart(
        rsi_fig,
        use_container_width=True
    )

with right:

    st.subheader("MACD")

    macd_fig = go.Figure()

    macd_fig.add_trace(go.Scatter(
        x=data.index,
        y=data["MACD"],
        mode="lines",
        name="MACD"
    ))

    macd_fig.add_trace(go.Scatter(
        x=data.index,
        y=data["MACD_SIGNAL"],
        mode="lines",
        name="Signal"
    ))

    macd_fig.update_layout(
        template="plotly_white",
        height=350
    )

    st.plotly_chart(
        macd_fig,
        use_container_width=True
    )

# =====================================================
# WATCHLIST
# =====================================================

st.subheader("Top Watchlist")

watchlist_data = []

for stock in stocks:

    try:

        df = yf.download(stock, period="5d")

        close = df["Close"].squeeze()

        close_price = float(close.iloc[-1])

        prev_price = float(close.iloc[-2])

        percent = ((close_price - prev_price) / prev_price) * 100

        watchlist_data.append({
            "Stock": stock,
            "Price": round(close_price, 2),
            "Change %": round(percent, 2)
        })

    except:
        pass

watchlist_df = pd.DataFrame(watchlist_data)

watchlist_df = watchlist_df.sort_values(
    by="Change %",
    ascending=False
)

st.dataframe(
    watchlist_df,
    use_container_width=True
)
