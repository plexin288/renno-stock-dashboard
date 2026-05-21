import streamlit as st
import pandas as pd
import numpy as np

# --- 1. SETTINGS ---
st.set_page_config(page_title="TumbuhKaya | Jurnal", layout="wide")

# --- 2. CSS KUSTOM (BIAR MIRIP GAMBAR) ---
st.markdown("""
<style>
    .stApp { background-color: #FAFAFA; }
    div[data-testid="stSidebar"] { background-color: #FFFFFF; border-right: 1px solid #E0E0E0; }
    .css-1r6slb0 { padding: 2rem; }
</style>
""", unsafe_allow_html=True)

# --- 3. GENERATE 900 DATA SAHAM ---
def generate_mock_data(n=900):
    tickers = ["MORA", "VAST", "UVCR", "TOOL", "TLKM", "PACK", "OASA", "NTBK", "NEST"]
    data = []
    for i in range(1, n + 1):
        data.append({
            "NO": i,
            "TANGGAL": "21 Mei 2026",
            "SAHAM": np.random.choice(tickers),
            "BIAS": "Bullish",
            "ACTION": "Swing Buy",
            "ENTRY": np.random.randint(100, 8000),
            "STOP LOSS": np.random.randint(90, 7500),
            "TP1": np.random.randint(8000, 9000),
            "TP2": np.random.randint(9000, 10000),
            "TP3": np.random.randint(10000, 11000),
            "R/R": "1 : 3",
            "STATUS": "Active"
        })
    return pd.DataFrame(data)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/growth.png", width=50)
    st.title("TumbuhKaya")
    st.write("MENU UTAMA")
    menu = ["Dashboard", "News", "Porto Terbuka", "Stocks Jurnal"]
    st.radio("Navigasi", menu, index=3)
    st.success("Upgrade VIP")

# --- 5. MAIN CONTENT ---
st.title("Panel Member")

# Filter area
c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
with c1: st.text_input("Cari ticker", placeholder="BBCA, BBRI...")
with c2: st.selectbox("Tahun", ["2026"])
with c3: st.selectbox("Periode", ["Year to Date"])
with c4: st.selectbox("Status", ["Semua Status"])

# Menampilkan Tabel 900 Data
df = generate_mock_data()
st.dataframe(
    df,
    column_config={
        "BIAS": st.column_config.TextColumn("BIAS", help="Analisis arah tren"),
        "STATUS": st.column_config.SelectboxColumn("STATUS", options=["Active", "Closed"]),
    },
    use_container_width=True,
    height=600
)
