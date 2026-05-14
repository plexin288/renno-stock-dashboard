import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator
import streamlit.components.v1 as components

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="RENNO STOCK DASHBOARD",
    layout="wide"
)

# ======================================
# CUSTOM CSS
# ======================================
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
    font-size: 58px;
    font-weight: 800;
    color: white;
    margin-bottom: 0;
}

.sub-title {
    color: #94a3b8;
    font-size: 18px;
    margin-top: 0;
}

.hero-box {
    background: linear-gradient(135deg, #111827, #0f172a);
    padding: 30px;
    border-radius: 24px;
    border: 1px solid #1f2937;
    margin-bottom: 25px;
    box-shadow: 0 0 25px rgba(34,197,94,0.15);
}

.metric-card {
    background: linear-gradient(135deg, #111827, #0f172a);
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #1f2937;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 0 15px rgba(0,0,0,0.4);
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(34,197,94,0.25);
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

.badge-buy {
    background: rgba(34,197,94,0.15);
    color: #22c55e;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: bold;
}

.badge-watch {
    background: rgba(250,204,21,0.15);
    color: #facc15;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: bold;
}

.badge-sell {
    background: rgba(239,68,68,0.15);
    color: #ef4444;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: bold;
}

.watchlist-card {
    background: linear-gradient(135deg, #111827, #0f172a);
    padding: 16px;
    border-radius: 18px;
    margin-bottom: 12px;
    border: 1px solid #1f2937;
    transition: all 0.3s ease;
}

.watchlist-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 20px rgba(59,130,246,0.2);
}

.alert-box {
    background: #111827;
    border-left: 5px solid #22c55e;
    padding: 14px;
    border-radius: 14px;
    margin-bottom: 10px;
}

.realtime-dot {
    height: 10px;
    width: 10px;
    background-color: #22c55e;
    border-radius: 50%;
    display: inline-block;
    animation: blink 1s infinite;
}

@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0.3; }
    100% { opacity: 1; }
}

</style>
""", unsafe_allow_html=True)

# ======================================
# STOCK LIST
# ======================================
stocks = [
    "BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK",
    "TLKM.JK","ASII.JK","GOTO.JK","BRIS.JK",
    "ICBP.JK","INDF.JK","ANTM.JK","MDKA.JK",
    "ADRO.JK","PGAS.JK","UNVR.JK","CPIN.JK",
    "JPFA.JK","SMGR.JK","KLBF.JK","EXCL.JK"
]

# ======================================
# SIDEBAR
# ======================================
st.sidebar.markdown("# ⚙️ RENNO TERMINAL")

selected_stock = st.sidebar.selectbox(
    "Pilih Saham",
    stocks
)

period = st.sidebar.selectbox(
    "Period",
    ["1mo", "3mo", "6mo", "1y"],
    index=1
)

# ======================================
# LOAD DATA
# ======================================
@st.cache_data
def load_data(symbol, period):
    df = yf.download(symbol, period=period)
    df.dropna(inplace=True)
    return df

# ======================================
# MAIN DATA
# ======================================
data = load_data(selected_stock, period)

close_series = data['Close'].squeeze()
open_series = data['Open'].squeeze()
high_series = data['High'].squeeze()
low_series = data['Low'].squeeze()
volume_series = data['Volume'].squeeze()

# ======================================
# INDICATORS
# ======================================
rsi = RSIIndicator(close=close_series)
data['RSI'] = rsi.rsi()

macd = MACD(close=close_series)
data['MACD'] = macd.macd()
data['MACD_SIGNAL'] = macd.macd_signal()

ma20 = SMAIndicator(close=close_series, window=20)
data['MA20'] = ma20.sma_indicator()

ma50 = SMAIndicator(close=close_series, window=50)
data['MA50'] = ma50.sma_indicator()

# ======================================
# AI SCORE
# ======================================
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
    signal = "🚀 STRONG BUY"
    signal_class = "badge-buy"
elif score >= 6:
    signal = "✅ BUY"
    signal_class = "badge-buy"
elif score >= 4:
    signal = "⚠ WATCH"
    signal_class = "badge-watch"
else:
    signal = "❌ SELL"
    signal_class = "badge-sell"

# ======================================
# HEADER
# ======================================

st.markdown(f"""
<div class="hero-box">

    <div class="main-title">
        📈 RENNO STOCK DASHBOARD
    </div>

    <p class="sub-title">
        Premium IDX Trading Dashboard
    </p>

    <p>
        <span class="realtime-dot"></span>
        Realtime Market Active
    </p>

</div>
""", unsafe_allow_html=True)

# ======================================
# METRICS
# ======================================
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

# ======================================
# AI SIGNAL PANEL
# ======================================
st.markdown("## 🤖 AI Signal")

st.markdown(f"""
<div class="metric-card">
    <h2>{signal}</h2>
    <h1>{score}/8</h1>
    <p>AI Confidence Score</p>
</div>
""", unsafe_allow_html=True)

# ======================================
# MARKET OVERVIEW
# ======================================
st.markdown("## 🌍 Market Overview")

market_data = []

for stock in stocks:

    try:
        df = yf.download(stock, period="5d")

        close = df['Close'].squeeze()
        volume = df['Volume'].squeeze()

        close_price = float(close.iloc[-1])
        prev_price = float(close.iloc[-2])

        percent = ((close_price - prev_price) / prev_price) * 100

        market_data.append({
            "Stock": stock,
            "Price": round(close_price, 2),
            "Change %": round(percent, 2),
            "Volume": int(volume.iloc[-1])
        })

    except:
        pass

market_df = pd.DataFrame(market_data)

# ======================================
# HEATMAP
# ======================================
st.markdown("## 🔥 IDX Heatmap")

fig_heatmap = px.treemap(
    market_df,
    path=['Stock'],
    values='Volume',
    color='Change %',
    color_continuous_scale=['red', 'gray', 'green']
)

fig_heatmap.update_layout(
    paper_bgcolor="#050816",
    plot_bgcolor="#050816",
    font_color="white",
    height=600
)

st.plotly_chart(fig_heatmap, use_container_width=True)

# ======================================
# AI SCANNER TABLE
# ======================================
st.markdown("## 🚀 AI Scanner")

scanner_data = []

for stock in stocks:

    try:
        df = yf.download(stock, period="3mo")

        close = df['Close'].squeeze()
        volume = df['Volume'].squeeze()

        rsi_calc = RSIIndicator(close=close)
        rsi_val = rsi_calc.rsi().iloc[-1]

        macd_calc = MACD(close=close)
        macd_val = macd_calc.macd().iloc[-1]
        macd_signal = macd_calc.macd_signal().iloc[-1]

        ma20_calc = SMAIndicator(close=close, window=20)
        ma50_calc = SMAIndicator(close=close, window=50)

        ma20_val = ma20_calc.sma_indicator().iloc[-1]
        ma50_val = ma50_calc.sma_indicator().iloc[-1]

        ai_score = 0

        if rsi_val < 70:
            ai_score += 2

        if macd_val > macd_signal:
            ai_score += 2

        if ma20_val > ma50_val:
            ai_score += 2

        if volume.iloc[-1] > volume.tail(20).mean():
            ai_score += 2

        trend = "Bullish" if ma20_val > ma50_val else "Bearish"

        scanner_data.append({
            "Stock": stock,
            "Price": round(float(close.iloc[-1]), 2),
            "RSI": round(rsi_val, 2),
            "Volume": int(volume.iloc[-1]),
            "AI Score": ai_score,
            "Trend": trend
        })

    except:
        pass

scanner_df = pd.DataFrame(scanner_data)
scanner_df = scanner_df.sort_values(by="AI Score", ascending=False)

st.dataframe(scanner_df, use_container_width=True)

# ======================================
# TRADINGVIEW CHART
# ======================================
st.markdown("## 📊 TradingView Chart")

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

# ======================================
# RSI + MACD
# ======================================
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

# ======================================
# ALERT PANEL
# ======================================
st.markdown("## 🚨 Alert Panel")

if data['MACD'].iloc[-1] > data['MACD_SIGNAL'].iloc[-1]:
    st.markdown('''
    <div class="alert-box">
        🚀 MACD Bullish Crossover Detected
    </div>
    ''', unsafe_allow_html=True)

if data['RSI'].iloc[-1] > 70:
    st.markdown('''
    <div class="alert-box">
        ⚠ RSI Overbought Area
    </div>
    ''', unsafe_allow_html=True)

if volume_series.iloc[-1] > avg_volume:
    st.markdown('''
    <div class="alert-box">
        🔥 Volume Surge Detected
    </div>
    ''', unsafe_allow_html=True)

# ======================================
# PREMIUM WATCHLIST
# ======================================
st.markdown("## ⭐ Premium Watchlist")

market_df = market_df.sort_values(
    by="Change %",
    ascending=False
)

for _, row in market_df.head(10).iterrows():

    color = "green" if row['Change %'] > 0 else "red"

    icon = "📈" if row['Change %'] > 0 else "📉"

    st.markdown(f'''
    <div class="watchlist-card">
        <h3>{icon} {row['Stock']}</h3>
        <p>Price: {row['Price']}</p>
        <p>Volume: {row['Volume']:,}</p>
        <p class="{color}">
            Change: {row['Change %']}%
        </p>
    </div>
    ''', unsafe_allow_html=True)
