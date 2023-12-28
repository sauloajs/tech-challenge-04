import streamlit as st

st.set_page_config(layout="wide", page_title='Mercado de Petróleo', page_icon='📈')

hide_table_row_index = """
        <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
        </style>
"""
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.title('📈 - Mercado do petróleo')

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.image('./src/images/balance.png')

with col2:
    st.image('./src/images/prices_products.png')
    
with col3:
    st.image('./src/images/markets_interest.png')
    
tab1, tab2 = st.tabs(['⬆️ - Oferta', '⬇️ - Demanda'])

with tab1:
    st.title('Oferta')
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image('./src/images/saudi_production.png')
    
    with col2:
        st.image('./src/images/non_opec_production.png')
        
    
with tab2:
    st.title('Demanda')
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image('./src/images/oecd_consumption.png')
    with col2:
        st.image('./src/images/non_oecd_consumption.png')