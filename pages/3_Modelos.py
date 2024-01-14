import streamlit as st
from src.data.models_results import xgb, ols
from src.data.ipea_data import df
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title='Modelos Utilizados', page_icon='📈')

tab1, tab2, tab3 = st.tabs(["ARIMA", "OLS", "MLP"])

with tab1:
    st.title('ARIMA (AutoRegressive Integrated Moving Average)')
    from statsmodels.tsa.arima.model import ARIMA

    # Supondo que df['Preco'] é a sua série temporal de preços do petróleo
    model = ARIMA(df['Preco'], order=(5, 1, 0))
    model_fit = model.fit()
    df['forecast'] = model_fit.predict(start=len(df), end=len(df)+365, dynamic=True)
    fig, ax = plt.subplots()
    df[['Preco', 'forecast']].plot(figsize=(12, 8))

    st.pyplot(plt)

with tab2:
    st.title('OLS (Ordinary Least Squares)')
    
    st.image('./src/images/ols.png')
    
with tab3:
    st.title('MLP (Multilayer Perceptron)')
    
    st.image('./src/images/mlp.png')