import streamlit as st
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

from src.data.ipea_data import df


tab1, tab2, tab3, tab4 = st.tabs(['Preço do Petróleo', 'Projeção do Preço do Petróleo', 'Distribuição ao Longo do tempo', 'Distribuição Final'])

# Calculando os retornos logarítmicos dos preços
df['Log_Return'] = np.log(df['Preco'] / df['Preco'].shift(1))

# Calculando a média e o desvio padrão dos retornos logarítmicos
mu = df['Log_Return'].mean()
sigma = df['Log_Return'].std()

# Definindo os parâmetros para a simulação de Monte Carlo
num_simulations = 1000  # Número de simulações a serem realizadas
num_days = 252  # Número de dias para simular, aproximadamente um ano de negociação

# Criando um array para armazenar as simulações
simulations = np.zeros((num_simulations, num_days))

# Realizando as simulações
np.random.seed(42)  # Semente para reprodutibilidade
for i in range(num_simulations):
    # Gerando os choques aleatórios para os retornos
    random_shocks = np.random.normal(mu, sigma, num_days)
    # Criando o caminho de preço para cada simulação
    price_series = [df['Preco'].iloc[-1]]  # Iniciando com o último preço conhecido
    for shock in random_shocks:
        price_series.append(price_series[-1] * np.exp(shock))

    # Correção: Armazenando a simulação sem o primeiro elemento (último preço conhecido)
    simulations[i, :] = price_series[1:]

# Convertendo as simulações para um DataFrame para facilitar a análise
simulations_df = pd.DataFrame(simulations)


with tab1: 
    # Visualizando as simulações
    plt.figure(figsize=(10, 5))
    plt.plot(simulations_df.T, alpha=0.2, color='blue')
    plt.title('Simulação de Monte Carlo para o Preço do Petróleo')
    plt.xlabel('Dias')
    plt.ylabel('Preço Simulado')
    plt.show()

    st.pyplot(plt)


with tab2:
    # Defina o nível de confiança
    confidence_level = 0.95

    # Calcule o VaR
    sorted_simulations = np.sort(simulations, axis=0)
    index_at_confidence_level = int((1-confidence_level) * num_simulations)
    VaR_95 = sorted_simulations[index_at_confidence_level, -1] - df['Preco'].iloc[-1]

    # Exiba o VaR
    # print(f"O VaR a {confidence_level*100}% para o preço do petróleo é ${-VaR_95:.2f}.")
    # print(f"Isto significa que há uma chance de {100-confidence_level*100}% de perder mais de ${-VaR_95:.2f} no próximo ano.")

    # Calcular a média esperada para cada dia
    mean_projection = simulations_df.mean(axis=0)

    # Calcular a mediana para cada dia
    median_projection = simulations_df.median(axis=0)

    # Calcular os quantis para intervalos de confiança de 95%
    lower_quantile = simulations_df.quantile(0.025, axis=0)
    upper_quantile = simulations_df.quantile(0.975, axis=0)

    # Plotar a projeção
    plt.figure(figsize=(10, 5))

    # Projeção média
    plt.plot(mean_projection, label='Média', color='black')

    # Mediana da projeção
    plt.plot(median_projection, label='Mediana', color='red')

    # Intervalo de confiança de 95%
    plt.fill_between(range(num_days), lower_quantile, upper_quantile, color='blue', alpha=0.1, label='Intervalo de Confiança de 95%')

    # Detalhes do gráfico
    plt.title('Projeção de Preço do Petróleo - Simulação de Monte Carlo')
    plt.xlabel('Dias')
    plt.ylabel('Preço Projetado')
    plt.legend()

    st.pyplot(plt)


with tab3:
    from mpl_toolkits.mplot3d import Axes3D

    # Selecione um subconjunto das simulações para evitar um gráfico muito denso
    step = 10  # Isso escolherá uma em cada 10 simulações
    selected_simulations = simulations_df.iloc[:, ::step]

    # Configuração do gráfico
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Dados para o gráfico
    xpos = np.arange(selected_simulations.shape[0])
    ypos = np.arange(selected_simulations.shape[1])
    xpos, ypos = np.meshgrid(xpos, ypos)

    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    # Altura das barras
    dz = selected_simulations.values.flatten()

    # Largura e profundidade das barras
    dx = dy = 0.8

    # Criando o gráfico de barras 3D
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.5)

    # Rótulos e título
    ax.set_xlabel('Dias')
    ax.set_ylabel('Simulação')
    ax.set_zlabel('Preço Simulado')
    ax.set_title('Distribuição dos Preços do Petróleo ao Longo do Tempo - Simulação de Monte Carlo')

    st.pyplot(plt)

with tab4:
    final_prices = simulations_df.iloc[-1, :]

    # Plotar o histograma dos preços finais
    plt.figure(figsize=(10, 5))
    plt.hist(final_prices, bins=50, alpha=0.7, color='blue')

    # Detalhes do gráfico
    plt.title('Distribuição dos Preços Finais do Petróleo - Simulação de Monte Carlo')
    plt.xlabel('Preço Final')
    plt.ylabel('Frequência')
    plt.grid(True)

    st.pyplot(plt)
