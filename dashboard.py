import streamlit as st
from engine_data import StockAnalyzer
from components import UIComponent
from styles import inject_custom_css

st.set_page_config(page_title="Renno Stocks Pro", layout="wide")
inject_custom_css()

class DashboardApp:
    def __init__(self):
        self.tickers = ["BBCA", "BMRI", "TLKM", "GOTO", "ASII"]
    
    def run(self):
        st.title("Alpha Intelligence System")
        st.write("Professional Stock Analysis Terminal")
        
        cols = st.columns(3)
        for idx, t in enumerate(self.tickers):
            engine = StockAnalyzer(t)
            data = engine.fetch_market_data()
            
            if data is not None:
                metrics = engine.calculate_metrics(data)
                with cols[idx % 3]:
                    UIComponent.create_card(t, metrics)
            else:
                cols[idx % 3].error(f"Engine failed for {t}")

if __name__ == "__main__":
    app = DashboardApp()
    app.run()
