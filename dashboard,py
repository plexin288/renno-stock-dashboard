import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="RENNO STOCK",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

/* =========================
MAIN
========================= */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #FAFAFC;
}

/* HIDE STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* APP */
.stApp {
    background-color: #FAFAFC;
}

/* =========================
SIDEBAR
========================= */
section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #ECECEC;
    width: 260px !important;
}

.sidebar-title {
    font-size: 26px;
    font-weight: 700;
    color: #8B5CF6;
    margin-bottom: 30px;
}

.menu-title {
    color: #B0B0B0;
    font-size: 12px;
    margin-top: 25px;
    margin-bottom: 10px;
    font-weight: 600;
}

.menu-item {
    padding: 12px 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    font-size: 15px;
    font-weight: 500;
    color: #444;
    background-color: transparent;
    transition: 0.3s;
}

.menu-item:hover {
    background-color: #F3E8FF;
    color: #8B5CF6;
}

.active-menu {
    background-color: #F3E8FF;
    color: #8B5CF6;
    font-weight: 600;
}

/* =========================
TOPBAR
========================= */
.topbar {
    background: white;
    padding: 18px 25px;
    border-radius: 18px;
    border: 1px solid #ECECEC;
    margin-bottom: 30px;
}

/* =========================
TITLE
========================= */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #111827;
}

.sub-title {
    color: #6B7280;
    margin-bottom: 30px;
}

/* =========================
CARDS
========================= */
.card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #ECECEC;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.card-title {
    color: #6B7280;
    font-size: 15px;
    font-weight: 500;
}

.card-number {
    font-size: 38px;
    font-weight: 700;
    color: #111827;
}

.green {
    color: #22C55E;
    font-weight: 600;
}

.red {
    color: #EF4444;
    font-weight: 600;
}

.purple {
    color: #8B5CF6;
    font-weight: 600;
}

/* =========================
AI PICK
========================= */
.ai-box {
    background: #F8F1FF;
    border: 1px solid #E9D5FF;
    padding: 25px;
    border-radius: 22px;
    margin-top: 25px;
}

.ai-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #F0E7FF;
}

/* =========================
STOCK CARDS
========================= */
.stock-card {
    background: white;
    border-radius: 22px;
    padding: 22px;
    border: 1px solid #ECECEC;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    margin-top: 20px;
}

.stock-price {
    font-size: 40px;
    font-weight: 700;
    color: #111827;
}

.stock-name {
    font-size: 28px;
    font-weight: 700;
}

.buy-badge {
    background: #F3E8FF;
    color: #8B5CF6;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}

/* =========================
BUTTONS
========================= */
.stButton>button {
    background: #8B5CF6;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 18px;
    font-weight: 600;
}

.stButton>button:hover {
    background: #7C3AED;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================
with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
        📈 RENNO STOCK
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="menu-title">MENU UTAMA</div>', unsafe_allow_html=True)

    st.markdown('<div class="menu-item active-menu">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📋 Watchlist</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📊 Market</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔎 Screener</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🤖 AI Scanner</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📰 News</div>', unsafe_allow_html=True)

    st.markdown('<div class="menu-title">ANALISIS</div>', unsafe_allow_html=True)

    st.markdown('<div class="menu-item">📈 Market Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔥 Top Gainers</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📉 Top Losers</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🗺️ Heatmap</div>', unsafe_allow_html=True)

# =========================================
# TOPBAR
# =========================================
st.markdown("""
<div class="topbar">
🔍 Cari saham, sektor, atau indeks...
</div>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================
st.markdown('<div class="main-title">Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ringkasan pasar hari ini</div>', unsafe_allow_html=True)

# =========================================
# MARKET OVERVIEW
# =========================================
col1, col2, col3, col4 = st.columns(4)

cards = [
    ("IHSG", "7,245.62", "+82.45 (+1.15%)"),
    ("LQ45", "932.17", "+12.34 (+1.34%)"),
    ("IDX30", "482.91", "+6.21 (+1.30%)"),
    ("USD/IDR", "15,865", "-25 (-0.16%)")
]

for col, data in zip([col1,col2,col3,col4], cards):

    title, number, change = data

    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <br>
            <div class="card-number">{number}</div>
            <div class="purple">{change}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================
# AI DAILY PICK
# =========================================
st.markdown("""
<div class="ai-box">
    <h2 style="color:#111827;">🤖 AI Daily Pick</h2>
    <p style="color:#6B7280;">Top saham pilihan AI hari ini</p>
</div>
""", unsafe_allow_html=True)

# =========================================
# STOCK LIST
# =========================================
st.markdown("<br>", unsafe_allow_html=True)

stock1, stock2, stock3 = st.columns(3)

with stock1:
    st.markdown("""
    <div class="stock-card">
        <div class="stock-name">BBCA</div>
        <div style="color:#6B7280;">Bank Central Asia</div>

        <br>

        <div class="stock-price">Rp9,250</div>

        <br>

        <span class="buy-badge">STRONG BUY</span>

        <br><br>

        <div class="green">▲ +2.21%</div>
    </div>
    """, unsafe_allow_html=True)

with stock2:
    st.markdown("""
    <div class="stock-card">
        <div class="stock-name">TLKM</div>
        <div style="color:#6B7280;">Telkom Indonesia</div>

        <br>

        <div class="stock-price">Rp2,850</div>

        <br>

        <span class="buy-badge">BULLISH</span>

        <br><br>

        <div class="green">▲ +1.42%</div>
    </div>
    """, unsafe_allow_html=True)

with stock3:
    st.markdown("""
    <div class="stock-card">
        <div class="stock-name">BMRI</div>
        <div style="color:#6B7280;">Bank Mandiri</div>

        <br>

        <div class="stock-price">Rp6,200</div>

        <br>

        <span class="buy-badge">STRONG BUY</span>

        <br><br>

        <div class="green">▲ +3.33%</div>
    </div>
    """, unsafe_allow_html=True)
