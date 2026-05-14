import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator
import streamlit.components.v1 as components

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="RENNO STOCK DASHBOARD",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
    margin-top: 0;
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #1f2937;
    text-align: center;
}

.metric-title {
    color: #94a3b8;
    font-size: 14px;
}

.metric-value {
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.green {
    color: #22c55e;
}

.red {
    color: #ef4444;
}

.watchlist-card {
    background: #111827;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    border: 1px solid #1f2937;
}

</style>
""", unsafe_allow_html=True)

# =========================
# STOCK LIST
# =========================
stocks = [
    "BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK",
    "TLKM.JK","ASII.JK","GOTO.JK","BRIS.JK",
    "ICBP.JK","INDF.JK","ANTM.JK","MDKA.JK",
    "ADRO.JK","PGAS.JK","UNVR.JK","CPIN.JK",
    "JPFA.JK","SMGR.JK","KLBF.JK","EXCL.JK"
]

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("# ⚙️ RENNO")

selected_stock = st.sidebar.selectbox(
    "Pilih Saham",
    stocks
)

period = st.sidebar.selectbox(
    "Period",
    ["1mo", "3mo", "6mo", "1y"],
    index=1
)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data(symbol, period):
    df = yf.download(symbol, period=period)
    df.dropna(inplace=True)
    return df

data = load_data(selected_stock, period)

close_series = data['Close'].squeeze()
open_series = data['Open'].squeeze()
high_series = data['High'].squeeze()
low_series = data['Low'].squeeze()
volume_series = data['Volume'].squeeze()

# =========================
# INDICATORS
# =========================
rsi = RSIIndicator(close=close_series)
data['RSI'] = rsi.rsi()

macd = MACD(close=close_series)
data['MACD'] = macd.macd()
data['MACD_SIGNAL'] = macd.macd_signal()

ma20 = SMAIndicator(close=close_series, window=20)
data['MA20'] = ma20.sma_indicator()

ma50 = SMAIndicator(close=close_series, window=50)
data['MA50'] = ma50.sma_indicator()

# =========================
# HEADER
# =========================
st.markdown("""
<div class="main-title">
📈 RENNO STOCK DASHBOARD
</div>
<p class="sub-title">
Realtime IDX Stock Dashboard
</p>
""", unsafe_allow_html=True)

# =========================
# METRICS
# =========================
latest_close = float(close_series.iloc[-1])
latest_open = float(open_series.iloc[-1])

change = latest_close - latest_open
change_percent = (change / latest_open) * 100

trend_status = (
    "Bullish"
    if data['MA20'].iloc[-1] > data['MA50'].iloc[-1]
    else "Bearish"
)

trend_color = "green" if trend_status == "Bullish" else "red"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Stock</div>
        <div class="metric-value">{selected_stock}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Price</div>
        <div class="metric-value">{latest_close:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    color = "green" if change > 0 else "red"

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Change</div>
        <div class="metric-value {color}">
            {change_percent:.2f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Trend</div>
        <div class="metric-value {trend_color}">
            {trend_status}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# TRADINGVIEW CHART
# =========================
st.markdown("## 📊 Trading Chart")

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
    "height": 700,
    "symbol": "IDX:{symbol_tv}",
    "interval": "D",
    "timezone": "Asia/Jakarta",
    "theme": "dark",
    "style": "1",
    "locale": "id",
    "toolbar_bg": "#050816",
    "enable_publishing": false,
    "hide_side_toolbar": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_chart"
  }}
  );
  </script>
</div>
'''

components.html(tv_widget, height=700)

# =========================
# RSI + MACD
# =========================
left, right = st.columns(2)

with left:
    st.markdown("## 📈 RSI")

    rsi_fig = go.Figure()

    rsi_fig.add_trace(go.Scatter(
        x=data.index,
        y=data['RSI'],
        mode='lines',
        name='RSI'
    ))

    rsi_fig.add_hline(y=70)
    rsi_fig.add_hline(y=30)

    rsi_fig.update_layout(
        height=300,
        template="plotly_dark",
        paper_bgcolor="#050816",
        plot_bgcolor="#050816"
    )

    st.plotly_chart(rsi_fig, use_container_width=True)

with right:
    st.markdown("## 🚀 MACD")

    macd_fig = go.Figure()

    macd_fig.add_trace(go.Scatter(
        x=data.index,
        y=data['MACD'],
        mode='lines',
        name='MACD'
    ))

    macd_fig.add_trace(go.Scatter(
        x=data.index,
        y=data['MACD_SIGNAL'],
        mode='lines',
        name='Signal'
    ))

    macd_fig.update_layout(
        height=300,
        template="plotly_dark",
        paper_bgcolor="#050816",
        plot_bgcolor="#050816"
    )

    st.plotly_chart(macd_fig, use_container_width=True)

# =========================
# WATCHLIST
# =========================
st.markdown("## 🔥 Top Watchlist")

watchlist_data = []

for stock in stocks:
    try:
        df = yf.download(stock, period="5d")

        close = df['Close'].squeeze()

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

for _, row in watchlist_df.head(10).iterrows():

    color = "green" if row['Change %'] > 0 else "red"

    st.markdown(f'''
    <div class="watchlist-card">
        <h4>{row['Stock']}</h4>
        <p>Price: {row['Price']}</p>
        <p class="{color}">
            Change: {row['Change %']}%
        </p>
    </div>
    ''', unsafe_allow_html=True)
