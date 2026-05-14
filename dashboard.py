import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator
import streamlit.components.v1 as components

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="RENNO STOCK DASHBOARD",
    layout="wide"
)

# ======================================================
# SIMPLE MODERN CSS
# ======================================================

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fe;
}

section[data-testid="stSidebar"] {
    background: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

h1 {
    color: #111827 !important;
    font-size: 60px !important;
    font-weight: 800 !important;
}

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 24px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    text-align: center;
    border: 1px solid #e5e7eb;
}

.metric-title {
    color: #6b7280;
    font-size: 14px;
}

.metric-value {
    color: #111827;
    font-size: 34px;
    font-weight: bold;
}

.green {
    color: #22c55e;
}

.red {
    color: #ef4444;
}

.ai-box {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    padding: 40px;
    border-radius: 30px;
    color: white;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 30px;
}

.watch-card {
    background: white;
    padding: 20px;
    border-radius: 22px;
    margin-bottom: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    border: 1px solid #e5e7eb;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# STOCK LIST
# ======================================================

stocks = [
    "BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK",
    "TLKM.JK","ASII.JK","GOTO.JK","BRIS.JK",
    "ANTM.JK","MDKA.JK","ADRO.JK","PGAS.JK",
    "ICBP.JK","INDF.JK","CPIN.JK","KLBF.JK"
]

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.title("RENNO TERMINAL")

selected_stock = st.sidebar.selectbox(
    "Select Stock",
    stocks
)

period = st.sidebar.selectbox(
    "Period",
    ["1mo", "3mo", "6mo", "1y"],
    index=1
)

# ======================================================
# LOAD DATA
# ======================================================

@st.cache_data
def load_data(symbol, period):
    df = yf.download(symbol, period=period)
    df.dropna(inplace=True)
    return df

data = load_data(selected_stock, period)

close_series = data['Close'].squeeze()
open_series = data['Open'].squeeze()
volume_series = data['Volume'].squeeze()

# ======================================================
# INDICATORS
# ======================================================

rsi = RSIIndicator(close=close_series)
data['RSI'] = rsi.rsi()

macd = MACD(close=close_series)
data['MACD'] = macd.macd()
data['MACD_SIGNAL'] = macd.macd_signal()

ma20 = SMAIndicator(close=close_series, window=20)
data['MA20'] = ma20.sma_indicator()

ma50 = SMAIndicator(close=close_series, window=50)
data['MA50'] = ma50.sma_indicator()

# ======================================================
# AI SCORE
# ======================================================

score = 0

if data['RSI'].iloc[-1] < 70:
    score += 2

if data['MACD'].iloc[-1] > data['MACD_SIGNAL'].iloc[-1]:
    score += 2

if data['MA20'].iloc[-1] > data['MA50'].iloc[-1]:
    score += 2

avg_volume = volume_series.tail(20).mean()

if volume_series.iloc[-1] > avg_volume:
    score += 2

if score >= 8:
    signal = "STRONG BUY"
elif score >= 6:
    signal = "BUY"
elif score >= 4:
    signal = "WATCH"
else:
    signal = "SELL"

# ======================================================
# HEADER
# ======================================================

st.title("RENNO STOCK DASHBOARD")

st.markdown(
    "### Premium AI Powered IDX Market Dashboard"
)

st.success("🟢 Realtime Market Active")

# ======================================================
# METRICS
# ======================================================

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

# ======================================================
# AI SIGNAL
# ======================================================

st.markdown(f"""
<div class="ai-box">
    <h1>{signal}</h1>
    <h2>{score}/8 AI SCORE</h2>
    <p>AI Trading Signal Engine</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# MARKET SCANNER
# ======================================================

scanner_data = []

for stock in stocks:

    try:

        df = yf.download(stock, period="5d")

        close = df['Close'].squeeze()
        volume = df['Volume'].squeeze()

        close_price = float(close.iloc[-1])
        prev_price = float(close.iloc[-2])

        percent = ((close_price - prev_price) / prev_price) * 100

        trend = "Bullish" if percent > 0 else "Bearish"

        scanner_data.append({
            "Stock": stock,
            "Price": round(close_price, 2),
            "Change %": round(percent, 2),
            "Volume": int(volume.iloc[-1]),
            "Trend": trend
        })

    except:
        pass

scanner_df = pd.DataFrame(scanner_data)

scanner_df = scanner_df.sort_values(
    by="Change %",
    ascending=False
)

st.subheader("📈 Market Scanner")

st.dataframe(
    scanner_df,
    use_container_width=True
)

# ======================================================
# TRADINGVIEW CHART
# ======================================================

st.subheader("📊 Trading Chart")

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
    "theme": "light",
    "style": "1",
    "locale": "id",
    "toolbar_bg": "#ffffff",
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

# ======================================================
# RSI + MACD
# ======================================================

left, right = st.columns(2)

with left:

    st.subheader("📈 RSI")

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
        template="plotly_white",
        height=350
    )

    st.plotly_chart(
        rsi_fig,
        use_container_width=True
    )

with right:

    st.subheader("🚀 MACD")

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
        template="plotly_white",
        height=350
    )

    st.plotly_chart(
        macd_fig,
        use_container_width=True
    )

# ======================================================
# WATCHLIST
# ======================================================

st.subheader("🔥 Top Watchlist")

for _, row in scanner_df.head(6).iterrows():

    color = "green" if row['Change %'] > 0 else "red"

    st.markdown(f'''
    <div class="watch-card">

        <h3>{row['Stock']}</h3>

        <p>
            Price: {row['Price']}
        </p>

        <p>
            Volume: {row['Volume']:,}
        </p>

        <p class="{color}">
            Change: {row['Change %']}%
        </p>

    </div>
    ''', unsafe_allow_html=True)
