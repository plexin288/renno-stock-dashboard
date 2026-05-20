import streamlit as st

# ====================================
# PAGE CONFIG
# ====================================
st.set_page_config(
    page_title="RENNO STOCK",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================================
# CUSTOM CSS
# ====================================
st.markdown("""
<style>

/* HIDE STREAMLIT */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* APP */
.stApp {
    background-color: #FAFAFC;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #ECECEC;
    width: 260px !important;
}

/* TITLE */
.title {
    font-size: 38px;
    font-weight: 700;
    color: #111827;
}

.subtitle {
    color: #6B7280;
    margin-bottom: 30px;
}

/* MENU */
.menu-title {
    color: #A1A1AA;
    font-size: 12px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.menu-item {
    padding: 12px 15px;
    border-radius: 14px;
    margin-bottom: 8px;
    font-weight: 500;
    color: #52525B;
}

.active-menu {
    background-color: #F3E8FF;
    color: #8B5CF6;
    font-weight: 700;
}

/* TOP CARD */
.top-card {
    background: white;
    border: 1px solid #ECECEC;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.top-title {
    color: #6B7280;
    font-size: 14px;
    margin-bottom: 10px;
}

.top-number {
    font-size: 34px;
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

/* AI BOX */
.ai-box {
    background: #FAF5FF;
    border: 1px solid #E9D5FF;
    border-radius: 22px;
    padding: 25px;
    margin-top: 25px;
}

/* STOCK CARD */
.stock-card {
    background: white;
    border-radius: 22px;
    border: 1px solid #ECECEC;
    padding: 22px;
    margin-top: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.stock-name {
    font-size: 28px;
    font-weight: 700;
    color: #111827;
}

.stock-company {
    color: #6B7280;
    font-size: 14px;
}

.stock-price {
    font-size: 38px;
    font-weight: 700;
    color: #111827;
}

.badge {
    background: #F3E8FF;
    color: #8B5CF6;
    padding: 7px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# ====================================
# SIDEBAR
# ====================================
with st.sidebar:

    st.markdown("""
    <h1 style='color:#8B5CF6;'>📈 RENNO STOCK</h1>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="menu-title">MENU UTAMA</div>', unsafe_allow_html=True)

    st.markdown('<div class="menu-item active-menu">🏠 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📋 Watchlist</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📊 Market</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔎 Screener</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🤖 AI Scanner</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📰 News</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="menu-title">ANALISIS</div>', unsafe_allow_html=True)

    st.markdown('<div class="menu-item">📈 Market Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🔥 Top Gainers</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">📉 Top Losers</div>', unsafe_allow_html=True)
    st.markdown('<div class="menu-item">🗺️ Heatmap</div>', unsafe_allow_html=True)

# ====================================
# HEADER
# ====================================
st.markdown("""
<div class="title">
Dashboard
</div>
<div class="subtitle">
Ringkasan pasar hari ini
</div>
""", unsafe_allow_html=True)

# ====================================
# TOP MARKET
# ====================================
col1, col2, col3, col4 = st.columns(4)

cards = [
    ("IHSG", "7,245.62", "+1.15%"),
    ("LQ45", "932.17", "+1.34%"),
    ("IDX30", "482.91", "+1.30%"),
    ("USD/IDR", "15,865", "-0.16%"),
]

for col, data in zip([col1, col2, col3, col4], cards):

    title, number, change = data

    color = "green" if "+" in change else "red"

    with col:
        st.markdown(f"""
        <div class="top-card">
            <div class="top-title">{title}</div>
            <div class="top-number">{number}</div>
            <br>
            <div class="{color}">{change}</div>
        </div>
        """, unsafe_allow_html=True)

# ====================================
# AI DAILY PICK
# ====================================
st.markdown("""
<div class="ai-box">
    <h2 style="color:#111827;">🤖 AI Daily Pick</h2>
    <p style="color:#6B7280;">
        Top saham pilihan AI hari ini
    </p>
</div>
""", unsafe_allow_html=True)

# ====================================
# STOCK CARDS
# ====================================
col1, col2, col3 = st.columns(3)

stocks = [
    ("BBCA", "Bank Central Asia", "Rp9,250", "+2.21%"),
    ("TLKM", "Telkom Indonesia", "Rp2,850", "+1.42%"),
    ("BMRI", "Bank Mandiri", "Rp6,200", "+3.33%"),
]

for col, stock in zip([col1, col2, col3], stocks):

    code, company, price, change = stock

    with col:
        st.markdown(f"""
        <div class="stock-card">

            <div class="stock-name">{code}</div>

            <div class="stock-company">
                {company}
            </div>

            <br>

            <div class="stock-price">
                {price}
            </div>

            <br>

            <span class="badge">
                STRONG BUY
            </span>

            <br><br>

            <div class="green">
                ▲ {change}
            </div>

        </div>
        """, unsafe_allow_html=True)
