import streamlit as st
from src.data.models_results import xgb, ols

st.set_page_config(layout="wide", page_title='Modelos Utilizados', page_icon='📈')

tab1, tab2 = st.tabs(["OLS", "XGBoost"])

with tab1:
    st.title('OLS (Ordinary Least Squares)')
    st.table(ols)
    
with tab2:
    st.title('XGBoost (Extreme Gradient Boosting)')
    st.table(xgb)