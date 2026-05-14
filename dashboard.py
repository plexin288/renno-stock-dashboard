import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator
from ta.trend import MACD, SMAIndicator

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="RENNO STOCK DASHBOARD",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background-color: #f4f5fb;
}

section[data-testid="stSidebar"] {
    background: white;
    border-right: 1px solid #ececec;
}

section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #111827;
}

.sub-title {
    color: #6b7280;
    font-size: 16px;
}

.topbar {
    background: white;
    padding: 25px;
    border-radius: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
}

.card {
    background: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    border: 1px solid #f1f1f1;
}

.metric-card {
    background: white;
    padding: 25px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    border: 1px solid #f1f1f1;
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

.purple-box {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    border-radius: 25px;
    padding: 35px;
    color: white;
}

.small-card {
    background: white;
    padding: 20px;
    border-radius: 22px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    border: 1px solid #f1f1f1;
}

.watch-item {
    background: white;
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 12px;
    border: 1px solid #ececec;
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
    "BBNI.JK",
    "TLKM.JK",
    "ASII.JK",
    "GOTO.JK",
    "BRIS.JK",
    "ADRO.JK",
    "ANTM.JK"
]

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("# 🚀 RENNO TERMINAL")

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

close_series = data['Close'].squeeze()
open_series = data['Open'].squeeze()
volume_series = data['Volume'].squeeze()

# =====================================================
# INDICATORS
# =====================================================

rsi = RSIIndicator(close=close_series)

data['RSI'] = rsi.rsi()

macd = MACD(close=close_series)

data['MACD'] = macd.macd()
data['MACD_SIGNAL'] = macd.macd_signal()

ma20 = SMAIndicator(close=close_series, window=20)

data['MA20'] = ma20.sma_indicator()

ma50 = SMAIndicator(close=close_series, window=50)

data['MA50'] = ma50.sma_indicator()

# =====================================================
# AI SCORE
# =====================================================

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
elif score >= 6:
    signal = "✅ BUY"
elif score >= 4:
    signal = "⚠ WATCH"
else:
    signal = "❌ SELL"

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="topbar">
    <div class="main-title">
        RENNO STOCK DASHBOARD
    </div>

    <div class="sub-title">
        Premium Modern Trading Dashboard
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

latest_close = float(close_series.iloc[-1])
latest_open = float(open_series.iloc[-1])

change = latest_close - latest_open

change_percent = (change / latest_open) * 100

trend = (
    "Bullish"
    if data['MA20'].iloc[-1] > data['MA50'].iloc[-1]
    else "Bearish"
)

trend_color = "green" if trend == "Bullish" else "red"

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
            {trend}
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# MAIN LAYOUT
# =====================================================

left, right = st.columns([2,1])

# =====================================================
# LEFT SIDE
# =====================================================

with left:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Market Trend")

    chart = go.Figure()

    chart.add_trace(go.Scatter(
        x=data.index,
        y=close_series,
        mode='lines',
        line=dict(width=4)
    ))

    chart.update_layout(
        template='plotly_white',
        height=420,
        margin=dict(l=0, r=0, t=20, b=0)
    )

    st.plotly_chart(chart, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    colA, colB = st.columns(2)

    with colA:

        st.markdown(f"""
        <div class="purple-box">
            <h1>{signal}</h1>
            <h2>{score}/8 AI SCORE</h2>
            <p>AI Trading Engine</p>
        </div>
        """, unsafe_allow_html=True)

    with colB:

        st.markdown('<div class="small-card">', unsafe_allow_html=True)

        st.subheader("📊 RSI")

        rsi_fig = go.Figure()

        rsi_fig.add_trace(go.Scatter(
            x=data.index,
            y=data['RSI'],
            mode='lines'
        ))

        rsi_fig.add_hline(y=70)
        rsi_fig.add_hline(y=30)

        rsi_fig.update_layout(
            template='plotly_white',
            height=250,
            margin=dict(l=0, r=0, t=10, b=0)
        )

        st.plotly_chart(rsi_fig, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# RIGHT SIDE
# =====================================================

with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🔥 Watchlist")

    watchlist_data = []

    for stock in stocks:

        try:

            df = yf.download(stock, period='5d')

            close = df['Close'].squeeze()

            latest = float(close.iloc[-1])
            prev = float(close.iloc[-2])

            percent = ((latest - prev) / prev) * 100

            watchlist_data.append({
                'Stock': stock,
                'Price': round(latest, 2),
                'Change': round(percent, 2)
            })

        except:
            pass

    watchlist_df = pd.DataFrame(watchlist_data)

    watchlist_df = watchlist_df.sort_values(
        by='Change',
        ascending=False
    )

    for _, row in watchlist_df.head(8).iterrows():

        color = 'green' if row['Change'] > 0 else 'red'

        st.markdown(f'''
        <div class="watch-item">
            <h4>{row['Stock']}</h4>
            <p>Price: {row['Price']}</p>
            <p class="{color}">
                Change: {row['Change']}%
            </p>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# MARKET TABLE
# =====================================================

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Market Scanner")

scanner_data = []

for stock in stocks:

    try:

        df = yf.download(stock, period='5d')

        close = df['Close'].squeeze()
        volume = df['Volume'].squeeze()

        latest = float(close.iloc[-1])
        prev = float(close.iloc[-2])

        percent = ((latest - prev) / prev) * 100

        scanner_data.append({
            'Stock': stock,
            'Price': round(latest, 2),
            'Change %': round(percent, 2),
            'Volume': int(volume.iloc[-1])
        })

    except:
        pass

scanner_df = pd.DataFrame(scanner_data)

scanner_df = scanner_df.sort_values(
    by='Change %',
    ascending=False
)

st.dataframe(
    scanner_df,
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)
