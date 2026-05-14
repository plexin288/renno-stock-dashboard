import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="RENNO STOCK DASHBOARD", layout="wide")

st.title("📈 RENNO STOCK DASHBOARD")

stocks = [
    "BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK",
    "TLKM.JK","ASII.JK","GOTO.JK","BRIS.JK",
    "ICBP.JK","INDF.JK","ANTM.JK","MDKA.JK",
    "ADRO.JK","PGAS.JK","UNVR.JK","CPIN.JK",
    "JPFA.JK","SMGR.JK","KLBF.JK","EXCL.JK"
]

selected_stock = st.selectbox("Pilih Saham", stocks)

data = yf.download(selected_stock, period="3mo")

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
))

fig.update_layout(
    height=700,
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)
