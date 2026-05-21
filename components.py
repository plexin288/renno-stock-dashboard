import streamlit as st
import pandas as pd

def render_pro_card(ticker, data):
    color = "green" if data['pct'] >= 0 else "red"
    
    st.markdown(f"""
    <div class="card-premium">
        <div style="font-size:18px; font-weight:700;">{ticker}</div>
        <div style="font-size:22px; font-weight:800;">Rp {data['price']:,.0f}</div>
        <div style="color:{color}; font-weight:600;">{data['pct']:+.2f}%</div>
        <div style="font-size:12px; margin-top:10px;">
            RSI: {data['rsi']}<br>
            MACD: {data['macd']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Grafik kecil (Sparkline)
    chart_data = pd.DataFrame(data['history'], columns=['price'])
    st.line_chart(chart_data, use_container_width=True, height=100)
