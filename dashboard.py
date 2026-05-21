import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf

st.set_page_config(
    page_title="StockAI Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="auto"
)

st.sidebar.empty()

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #F8F7FF;
}

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: block;
    color: #8B5CF6;
}

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.9);
    border-right: 1px solid #E5E7EB;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 24px;
    box-shadow: 0 4px 20px rgba(139,92,246,0.08);
    border: 1px solid rgba(139,92,246,0.08);
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 22px;
    box-shadow: 0 4px 15px rgba(139,92,246,0.08);
}

.title {
    font-size: 34px;
    font-weight: 700;
    color: #111827;
}

.subtitle {
    color: #6B7280;
    font-size: 15px;
}

.green {
    color: #10B981;
    font-weight: 600;
}

.red {
    color: #EF4444;
    font-weight: 600;
}

.watchlist-row {
    display:flex;
    justify-content:space-between;
    padding:10px 0;
    border-bottom:1px solid #F3F4F6;
}

.small-title {
    font-size:18px;
    font-weight:700;
    color:#111827;
}

.purple-btn {
    background: linear-gradient(135deg,#8B5CF6,#C084FC);
    padding: 12px;
    border-radius: 14px;
    color: white;
    text-align:center;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("# ✨ StockAI")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Watchlist",
            "AI Scanner",
            "Chart",
            "Top Gainers",
            "Heatmap",
            "News",
            "Alerts",
            "Portfolio",
            "Backtest",
            "Settings"
        ],
        icons=[
            "grid",
            "star",
            "robot",
            "bar-chart",
            "graph-up-arrow",
            "grid-3x3-gap",
            "newspaper",
            "bell",
            "briefcase",
            "activity",
            "gear"
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent"
            },
            "icon": {
                "color": "#8B5CF6",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "6px",
                "padding": "14px",
                "border-radius": "14px",
                "color": "#111827"
            },
            "nav-link-selected": {
                "background-color": "#8B5CF6",
                "color": "white"
            },
        }
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='purple-btn'>
    🚀 Telegram Bot Connected
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
    <h4>👤 Bre</h4>
    <p style='color:#6B7280;'>Premium Plan</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# HEADER
# =========================

col1, col2 = st.columns([4,1])

with col1:
    st.markdown("<div class='title'>Good Morning, Bre 👋</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Market overview today</div>", unsafe_allow_html=True)

with col2:
    st.text_input("", placeholder="Search stock (e.g BBCA)")

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# TOP METRICS
# =========================

m1,m2,m3,m4 = st.columns(4)

metrics = [
    ("IHSG","7,145.23","+0.64%"),
    ("Volume","20.45 B","+12.3%"),
    ("Value","12.35 T","+8.2%"),
    ("Market Cap","11,234 T","+0.7%")
]

for col,metric in zip([m1,m2,m3,m4],metrics):
    with col:
        st.markdown(f"""
        <div class='metric-card'>
        <div style='color:#6B7280;font-size:14px'>{metric[0]}</div>
        <div style='font-size:32px;font-weight:700'>{metric[1]}</div>
        <div class='green'>{metric[2]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# MAIN LAYOUT
# =========================

left,right = st.columns([3,1])

# =========================
# LEFT SIDE
# =========================

with left:

    st.markdown("""
    <div class='card'>
    <div class='small-title'>BBCA · Bank Central Asia Tbk.</div>
    <div style='font-size:42px;font-weight:700;'>9,850 <span style='font-size:18px;color:#10B981;'>+1.29%</span></div>
    </div>
    """, unsafe_allow_html=True)

    # DUMMY CHART
    np.random.seed(1)
    dates = pd.date_range(start="2025-01-01", periods=80)
    prices = np.cumsum(np.random.randn(80)) + 100

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines',
        line=dict(color='#8B5CF6', width=3),
        fill='tozeroy'
    ))

    fig.update_layout(
        height=500,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=10,r=10,t=10,b=10),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#F3F4F6'),
        font=dict(color='#111827')
    )

    st.plotly_chart(fig, use_container_width=True)

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='card'>
        <div class='small-title'>RSI (14)</div>
        <h2>58.3</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
        <div class='small-title'>MACD</div>
        <h2>Bullish</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='card'>
        <div class='small-title'>Volume</div>
        <h2>1.45M</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    bottom1,bottom2 = st.columns(2)

    with bottom1:

        st.markdown("""
        <div class='card'>
        <div class='small-title'>AI Signal</div>
        <br>
        <h2>BBCA</h2>
        <p class='green'>STRONG BUY</p>
        <p>Entry : 9780 - 9850</p>
        <p>TP : 10200</p>
        <p>SL : 9400</p>
        </div>
        """, unsafe_allow_html=True)

    with bottom2:

        scanner = pd.DataFrame({
            'Stock':['ADRO','PTBA','SMGR','UNTR'],
            'Signal':['Breakout','Volume Surge','Bullish','Trend Bullish'],
            'Score':[88,85,82,80]
        })

        st.markdown("<div class='small-title'>Stock Scanner</div>", unsafe_allow_html=True)
        st.dataframe(scanner, use_container_width=True)

# =========================
# RIGHT SIDE
# =========================

with right:

    st.markdown("<div class='small-title'>Watchlist</div>", unsafe_allow_html=True)

    watchlist = [
        ('BBCA','+1.29%'),
        ('BMRI','+1.12%'),
        ('TLKM','-0.34%'),
        ('ASII','+0.84%'),
        ('UNVR','-0.61%')
    ]

    for stock,change in watchlist:

        color = 'green' if '+' in change else 'red'

        st.markdown(f"""
        <div class='card' style='margin-bottom:10px;'>
        <div style='display:flex;justify-content:space-between;'>
        <strong>{stock}</strong>
        <span class='{color}'>{change}</span>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='small-title'>Top Gainers</div>", unsafe_allow_html=True)

    gainers = pd.DataFrame({
        'Stock':['BUKA','GOTO','BRMS','CUAN'],
        'Gain':['+13%','+9%','+7%','+6%']
    })

    st.dataframe(gainers, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='small-title'>Market Heatmap</div>", unsafe_allow_html=True)

    heatmap = pd.DataFrame(np.random.rand(5,5))

    fig2 = px.imshow(
        heatmap,
        text_auto=True,
        aspect='auto',
        color_continuous_scale=['#FCA5A5','#FFFFFF','#4ADE80']
    )

    fig2.update_layout(
        height=250,
        margin=dict(l=0,r=0,t=0,b=0)
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='small-title'>Alerts</div>", unsafe_allow_html=True)

    alerts = [
        'BBCA breakout resistance 9800',
        'BMRI volume surge detected',
        'TLKM RSI oversold',
        'ASII bullish crossover MA20 & MA50'
    ]

    for a in alerts:
        st.markdown(f"""
        <div class='card' style='margin-bottom:10px;'>
        🔔 {a}
        </div>
        """, unsafe_allow_html=True)
