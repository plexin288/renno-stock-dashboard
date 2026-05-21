import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        :root {
            --primary-ungu: #7C3AED;
            --soft-ungu: #F8F5FF;
            --border-ungu: #E9D5FF;
            --dark-navy: #1E1B4B;
        }
        .stApp { background-color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; }
        
        [data-testid="stSidebar"] { background-color: var(--soft-ungu) !important; border-right: 1px solid var(--border-ungu); }
        
        .card-premium {
            background: white; border: 1px solid var(--border-ungu);
            border-radius: 20px; padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(124, 58, 237, 0.05);
        }
        
        .ticker-name { color: var(--dark-navy); font-size: 18px; font-weight: 700; }
        .text-neutral { color: #6B7280; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)
