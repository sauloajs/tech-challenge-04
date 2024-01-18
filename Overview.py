import streamlit as st
import plotly as pl

import pandas as pd
import matplotlib as plt
import plotly as pl
import plotly.graph_objects as go

from src.data.tables import inventory, supply, supplynonopec, demandoecd, demandnonoecd



st.set_page_config(layout="wide", page_title='Mercado de Petróleo', page_icon='📈')

hide_table_row_index = """
        <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
        </style>
"""
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.title('📈 - Mercado do petróleo')

# col1, col2, col3 = st.columns([1, 1, 1])

# with col1:
# st.image('./src/images/balance.png')

with st.container(): 
    fig = go.Figure()

    # Adiciona a Mudança de Estoque como um gráfico de barras no eixo y primário
    fig.add_trace(
        go.Bar(
            name='Inventory Change',
            x=inventory['Date'],
            y=inventory['Inventory Change'],
            marker=dict(color='rgb(1, 43, 102)'),  # Azul
        )
    )

    # Adiciona a Variação do Spread como uma linha no eixo y secundário
    fig.add_trace(
        go.Scatter(
            name='Spread Change',
            x=inventory['Date'],
            y=inventory['Spread Change'],
            line=dict(color='rgb(255, 82, 22)'),  # Vermelho
            yaxis='y2'  # Define que esta série usa o segundo eixo y
        )
    )

    st.write('O aumento nos reservatórios de petróleo sussurra prenúncios de um amanhã mais caro, enquanto o esvaziar dos tanques muitas vezes preludeia um custo mais módico')
    fig.update_layout(
        title=dict(
            text='',
            font=dict(
                size=14  # Ajustando o tamanho da fonte do título para 14
            )
        ),
        xaxis=dict(title='Data'),
        yaxis=dict(
            title='Variação de mm de barris',
            titlefont=dict(color='rgb(1, 43, 102)'),
            tickfont=dict(color='rgb(1, 43, 102)'),
            title_standoff=50
        ),
        yaxis2=dict(
            title='$/Barril change',
            titlefont=dict(color='rgb(255, 82, 22)'),
            tickfont=dict(color='rgb(255, 82, 22)'),
            overlaying='y',
            side='right',
            title_standoff=50
        ),
        legend=dict(
            x=0.03,
            y=0.9,
            bgcolor='rgba(255,255,255,0.5)'
        ),
        autosize=False,
        width=1366,
        height=454,
    )

    st.plotly_chart(fig)
    
tab1, tab2 = st.tabs(['⬆️ - Oferta', '⬇️ - Demanda'])

with tab1:
    st.title('Oferta')
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig = go.Figure()

        # Add traces
        fig.add_trace(go.Scatter(x=supply['date'], y=supply['Saudi Production Change'], name='Saudi Production', line_color='rgb(1, 43, 102)'))
        fig.add_trace(go.Scatter(x=supply['date'], y=supply['WTI Production Change'], name='WTI Production', line_color='rgb(255, 82, 22)'))

        # Update layout
        st.write('Quando a Arábia Saudita ajusta suas fontes de petróleo, o mundo observa: cada movimento lá é um prenúncio para os preços globais do ouro negro')
        
        fig.update_layout(
            title=dict(
                text='',
                font=dict(
                    size=14 
                )
            ),
            xaxis_title='Data',
            yaxis_title='Production change'
        )
        
        st.plotly_chart(fig)

    
    with col2:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=supplynonopec['date'],
            y=supplynonopec['WTI Real Price (GDP Deflated)'],
            name='WTI Real Price (GDP Deflated)',
            mode='lines',
            line=dict(color='rgb(1, 43, 102)'),
            yaxis='y1'
        ))

        fig.add_trace(go.Scatter(
            x=supplynonopec['date'],
            y=supplynonopec['non-OPEC Production change'],
            name='non-OPEC Production change (%)',
            mode='lines',
            line=dict(color='rgb(255, 82, 22)'),
            yaxis='y2'
        ))

        st.write('Movimentos na produção fora da OPEP ecoam pelo mercado, desenhando o futuro dos preços do petróleo')

        fig.update_layout(
            title=dict(
                text='',
                font=dict(
                    size=14
                )
            ),
            xaxis=dict(title='Date'),
            yaxis=dict(
                title='WTI Real Price (GDP Deflated) in USD',
                titlefont=dict(color='rgb(1, 43, 102)'),
                tickfont=dict(color='rgb(1, 43, 102)'),
                side='left',
                position=0.05
            ),
            yaxis2=dict(
                title='non-OPEC Production Change (%)',
                titlefont=dict(color='rgb(255, 82, 22)'),
                tickfont=dict(color='rgb(255, 82, 22)'),
                side='right',
                overlaying='y',
                position=0.95
            )
        )
        
        fig.update_layout(
            yaxis=dict(
                title_standoff=50
            )
        )
        
        fig.update_layout(
            yaxis2=dict(
                title_standoff=50
            )
        )
        
        st.plotly_chart(fig)
        
with tab2:
    st.title('Demanda')
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig = go.Figure()

        # Adiciona o Preço Real WTI ao eixo y1
        fig.add_trace(go.Scatter(
            x=demandoecd['date'],
            y=demandoecd['WTI Real Price (GDP Deflated)'],
            name='WTI Real Price (GDP Deflated)',
            mode='lines',
            line=dict(color='rgb(1, 43, 102)'),
            yaxis='y1'
        ))

        # Adiciona a mudança percentual do consumo da OECD ano a ano ao eixo y2
        fig.add_trace(go.Scatter(
            x=demandoecd['date'],
            y=demandoecd['y-o-y % OECD Consumption Change'],
            name='y-o-y % OECD Consumption Change',
            mode='lines',
            line=dict(color='rgb(255, 82, 22)'),
            yaxis='y2'
        ))
        
        st.write('Nos países da OCDE, os cifrões ascendem e o consumo desce: uma dança de números que revela uma nova prudência energética')
        fig.update_layout(
            title=dict(
                text='',
                font=dict(
                    size=14  # Define o tamanho da fonte do título
                )
            ),
            xaxis=dict(title='Date'),
            yaxis=dict(
                title='WTI Real Price (GDP Deflated) in USD',
                titlefont=dict(color='rgb(1, 43, 102)'),
                tickfont=dict(color='rgb(1, 43, 102)'),
                side='left',
                position=0.05,
                title_standoff=50
            ),
            yaxis2=dict(
                title='y-o-y % OECD Consumption Change',
                titlefont=dict(color='rgb(255, 82, 22)'),
                tickfont=dict(color='rgb(255, 82, 22)'),
                side='right',
                overlaying='y',
                position=0.95,
                title_standoff=50
            )
        )
        
        st.plotly_chart(fig)
        
    with col2:
        fig = go.Figure()

        # Adiciona a mudança percentual do consumo non-OECD como barras
        fig.add_trace(go.Bar(
            x=demandnonoecd['date'],
            y=demandnonoecd['non-OECD Consumption Growth'],
            name='non-OECD Consumption Growth (%)',
            marker_color='rgb(1, 43, 102)'  # Azul
        ))

        # Adiciona a mudança percentual do PIB non-OECD como linha
        fig.add_trace(go.Scatter(
            x=demandnonoecd['date'],
            y=demandnonoecd['non-OECD GDP growth'],
            name='non-OECD GDP Growth (%)',
            mode='lines',
            line_color='rgb(255, 82, 22)'  # Vermelho
        ))

        # Define o layout para usar um único eixo y para ambas as variáveis
        
        st.write('Quando a economia pulsa, o coração do petróleo acelera: cada salto no crescimento econômico bombeia a demanda por energia para novos patamares')
        fig.update_layout(
            title=dict(
                text='',
                font=dict(
                    size=14  # Ajuste o tamanho da fonte conforme necessário
                )
            ),
            xaxis=dict(title='Date'),
            yaxis=dict(
                title='Variação percentual (%)',
                side='left',
                title_standoff=15
            ),
            barmode='group'
        )

        st.plotly_chart(fig)