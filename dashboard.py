import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="StockAI Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;

    position: fixed !important;
    top: 20px !important;
    left: 20px !important;

    background: white !important;
    border-radius: 12px !important;
    padding: 8px !important;

    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.95);
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

    # =========================
    # TRADINGVIEW CHART
    # =========================

    tradingview_widget = """
    <div class="tradingview-widget-container">
      <div id="tradingview_chart"></div>

      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>

      <script type="text/javascript">
      new TradingView.widget({
        "width": "100%",
        "height": 600,
        "symbol": "IDX:BBCA",
        "interval": "D",
        "timezone": "Asia/Jakarta",
        "theme": "light",
        "style": "1",
        "locale": "id",
        "toolbar_bg": "#F8F7FF",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "hide_top_toolbar": false,
        "hide_legend": false,
        "save_image": false,
        "container_id": "tradingview_chart",
        "studies": [
          "MASimple@tv-basicstudies",
          "Volume@tv-basicstudies"
        ]
      });
      </script>
    </div>
    """

    components.html(tradingview_widget, height=620)

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
