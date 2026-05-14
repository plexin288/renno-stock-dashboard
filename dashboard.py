import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="RENNO STOCK DASHBOARD",
    layout="wide"
)

# =========================
# TITLE
# =========================
st.title("📈 RENNO STOCK DASHBOARD")
st.markdown("Realtime IDX Stock Dashboard")

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
st.sidebar.title("⚙️ Settings")

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

# FIX DATAFRAME
close_series = data['Close'].squeeze()
open_series = data['Open'].squeeze()
high_series = data['High'].squeeze()
low_series = data['Low'].squeeze()
volume_series = data['Volume'].squeeze()

# =========================
# INDICATORS
# =========================

# RSI
rsi = RSIIndicator(close=close_series)
data['RSI'] = rsi.rsi()

# MACD
macd = MACD(close=close_series)
data['MACD'] = macd.macd()
data['MACD_SIGNAL'] = macd.macd_signal()

# MA20
ma20 = SMAIndicator(close=close_series, window=20)
data['MA20'] = ma20.sma_indicator()

# MA50
ma50 = SMAIndicator(close=close_series, window=50)
data['MA50'] = ma50.sma_indicator()

# =========================
# PRICE INFO
# =========================

latest_close = float(close_series.iloc[-1])
latest_open = float(open_series.iloc[-1])

change = latest_close - latest_open
change_percent = (change / latest_open) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Stock", selected_stock)
col2.metric("Price", f"{latest_close:.2f}")
col3.metric("Change", f"{change:.2f}")
col4.metric("Change %", f"{change_percent:.2f}%")

# =========================
# CANDLESTICK
# =========================

st.subheader("📊 Candlestick Chart")

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data.index,
    open=open_series,
    high=high_series,
    low=low_series,
    close=close_series,
    name='Candlestick'
))

fig.add_trace(go.Scatter(
    x=data.index,
    y=data['MA20'],
    mode='lines',
    name='MA20'
))

fig.add_trace(go.Scatter(
    x=data.index,
    y=data['MA50'],
    mode='lines',
    name='MA50'
))

fig.update_layout(
    height=700,
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# RSI
# =========================

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
    height=300,
    template="plotly_dark"
)

st.plotly_chart(rsi_fig, use_container_width=True)

# =========================
# MACD
# =========================

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
    height=300,
    template="plotly_dark"
)

st.plotly_chart(macd_fig, use_container_width=True)

# =========================
# VOLUME
# =========================

st.subheader("📦 Volume")

volume_fig = go.Figure()

volume_fig.add_trace(go.Bar(
    x=data.index,
    y=volume_series,
    name='Volume'
))

volume_fig.update_layout(
    height=300,
    template="plotly_dark"
)

st.plotly_chart(volume_fig, use_container_width=True)

# =========================
# SIGNAL STATUS
# =========================

st.subheader("🤖 Signal Status")

trend_status = (
    "Bullish"
    if data['MA20'].iloc[-1] > data['MA50'].iloc[-1]
    else "Bearish"
)

macd_status = (
    "Bullish"
    if data['MACD'].iloc[-1] > data['MACD_SIGNAL'].iloc[-1]
    else "Bearish"
)

rsi_value = data['RSI'].iloc[-1]

if rsi_value > 70:
    rsi_status = "Overbought"
elif rsi_value < 30:
    rsi_status = "Oversold"
else:
    rsi_status = "Normal"

st.success(f"Trend: {trend_status}")
st.info(f"MACD: {macd_status}")
st.warning(f"RSI Status: {rsi_status}")

# =========================
# WATCHLIST
# =========================

st.subheader("🔥 Watchlist")

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

st.dataframe(watchlist_df, use_container_width=True)
