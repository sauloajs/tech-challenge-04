import streamlit as st
from src.data.tables import variables

st.set_page_config(layout="wide", page_title='Variaveis Utilizadas', page_icon='📈')

st.table(variables)