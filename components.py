import streamlit as st

def render_card(ticker, data):
    if data['error']:
        st.error(f"Gagal memuat {ticker}")
        return

    # Warna tergantung kondisi naik atau turun
    color = "green" if data['pct'] >= 0 else "red"
    
    st.markdown(f"""
    <div class="card-premium">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="ticker-name">{ticker}</div>
            <div style="font-size:12px; color:gray;">{data['pct']:.2f}%</div>
        </div>
        <div style="font-size:24px; font-weight:800; margin:10px 0;">Rp {data['price']:,.0f}</div>
        <div style="background:{color}15; color:{color}; padding:5px; border-radius:8px; text-align:center; font-weight:bold;">
            {data['pct']:.2f}%
        </div>
    </div>
    """, unsafe_allow_html=True)
