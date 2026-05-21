import streamlit as st

def render_stock_card(ticker, data):
    st.markdown(f"""
    <div class="card-premium">
        <div class="ticker-name">{ticker}</div>
        <div style="font-size:20px; font-weight:800;">Rp {data['price']:,.0f}</div>
        <div style="color: {'green' if data['pct'] >= 0 else 'red'}; font-weight:600;">
            {data['pct']:+.2f}%
        </div>
    </div>
    """, unsafe_allow_html=True)
