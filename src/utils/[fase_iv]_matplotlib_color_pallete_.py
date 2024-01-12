# -*- coding: utf-8 -*-
"""[Fase IV] Matplotlib color pallete .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ru9zHOoqbUBpqiuUTDG1LzCdJ-_49dD6
"""

import pandas as pd
import matplotlib as plt
import plotly as pl

import pandas as pd
import matplotlib as plt
import plotly as pl
import plotly.graph_objects as go

"""#Mercado de petróleo"""

inventory = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='balance')

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

fig.update_layout(
    title=dict(
        text='O aumento nos reservatórios de petróleo sussurra prenúncios de um amanhã mais caro, enquanto o esvaziar dos tanques muitas vezes preludeia um custo mais módico',
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
    )
)
# Exibe o gráfico
fig.show()

"""# Oferta (Supply)"""

supply = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='supply')
supply.head()

# prompt: create a beatiful chart with the Saudi Production change and WTI Production change with rgb color but with two differente axes to diferentiate

import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=supply['date'], y=supply['Saudi Production Change'], name='Saudi Production', line_color='rgb(1, 43, 102)'))
fig.add_trace(go.Scatter(x=supply['date'], y=supply['WTI Production Change'], name='WTI Production', line_color='rgb(255, 82, 22)'))

# Update layout
fig.update_layout(
    title=dict(
        text='Quando a Arábia Saudita ajusta suas fontes de petróleo, o mundo observa: cada movimento lá é um prenúncio para os preços globais do ouro negro',
        font=dict(
            size=14  # Ajustando o tamanho da fonte para 14
        )
    ),
    xaxis_title='Data',
    yaxis_title='Production change'
)
# Show figure
fig.show()

# Read data
supplynonopec = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='supply')
# Cria a figura
fig = go.Figure()

# Adiciona o Preço Real WTI ao eixo y1
fig.add_trace(go.Scatter(
    x=supplynonopec['date'],
    y=supplynonopec['WTI Real Price (GDP Deflated)'],
    name='WTI Real Price (GDP Deflated)',
    mode='lines',
    line=dict(color='rgb(1, 43, 102)'),
    yaxis='y1'
))

# Adiciona a mudança de produção non-OPEC ao eixo y2
fig.add_trace(go.Scatter(
    x=supplynonopec['date'],
    y=supplynonopec['non-OPEC Production change'],
    name='non-OPEC Production change (%)',
    mode='lines',
    line=dict(color='rgb(255, 82, 22)'),
    yaxis='y2'
))

fig.update_layout(
    title=dict(
        text='Movimentos na produção fora da OPEP ecoam pelo mercado, desenhando o futuro dos preços do petróleo',
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
# Atualizar configurações do eixo y1 (WTI Real Price)
fig.update_layout(
    yaxis=dict(
        title_standoff=50
    )
)

# Atualizar configurações do eixo y2 (non-OPEC Production Change)
fig.update_layout(
    yaxis2=dict(
        title_standoff=50
    )
)

# Exibe o gráfico
fig.show()

"""#Demanda"""

demandoecd = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='consump change non ocde')

# Cria a figura
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
fig.update_layout(
    title=dict(
        text='Nos países da OCDE, os cifrões ascendem e o consumo desce: uma dança de números que revela uma nova prudência energética',
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
# Exibe o gráfico
fig.show()

demandnonoecd = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='consump change non ocde')

# Cria a figura
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
fig.update_layout(
    title=dict(
        text='Quando a economia pulsa, o coração do petróleo acelera: cada salto no crescimento econômico bombeia a demanda por energia para novos patamares',
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

# Exibe o gráfico
fig.show()
