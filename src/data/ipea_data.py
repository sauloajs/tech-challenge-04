import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página com os dados
url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view"

# Fazer a requisição para obter o conteúdo da página
page = requests.get(url)

# Analisar o conteúdo da página com BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Encontrar a tabela pelo ID (ajuste conforme necessário com base na estrutura HTML real)
table = soup.find('table', {'id': 'grd_DXMainTable'})

# Converter a tabela HTML para um DataFrame do pandas
# Isso só vai funcionar se o BeautifulSoup encontrar a tabela correta
# e se essa tabela estiver em um formato que o pandas possa ler diretamente.
# Se a tabela usar JavaScript para carregar os dados, isso não funcionará.
if table:
    df = pd.read_html(str(table))[0]
    # print('Conteúdo localizado')
else:
    df = pd.DataFrame()
    # print('Tabela não encontrada')


# Supondo que df seja o DataFrame criado a partir da tabela HTML

# Passo 1: Renomear Colunas
# Se as colunas não foram nomeadas automaticamente, você pode renomeá-las manualmente
df.columns = ['Data', 'Preco']

# Passo 2: Conversão de Tipos de Dados
# Converter a coluna 'Data' para datetime
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')  # Ajustar o parâmetro 'dayfirst' conforme necessário

# Converter a coluna 'Preco' para float
df['Preco'] = pd.to_numeric(df['Preco'].str.replace(',', '.'), errors='coerce')  # Substituir vírgula por ponto se necessário

# Passo 3: Ordenação dos Dados
# Ordenar o DataFrame pela coluna 'Data'
df.sort_values('Data', inplace=True)

# Passo 4: Tratamento de Valores Ausentes
# Remover linhas com valores ausentes
df.dropna(inplace=True)

# Resetar o índice do DataFrame após a limpeza
df.reset_index(drop=True, inplace=True)

# Verificar o DataFrame após a limpeza
# print(df.head())