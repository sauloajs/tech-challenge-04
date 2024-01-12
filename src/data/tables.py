import pandas as pd

inventory = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='balance')

supply = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='supply')

supplynonopec = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='supply')

demandoecd = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='consump change non ocde')

demandnonoecd = pd.read_excel('ExcelbaseDrivesStreamlit.xlsx', sheet_name='consump change non ocde')

variables = pd.DataFrame({
    'Nome' : [
        'Saudi Production Change',
        'WTI Production Change',
        'Opec Disruption',
        'Non-OPEC Disruption',
        'non-OPEC Production Change',
        'Inventory Change',
        'Spare Capacity',
        'Capacity percent change',
        'FED_FUNDS',
        'FX_dol',
        'S&P',
        'Producers/Merchants long',
        'Producers/Merchants short',
        'Producers/Merchants net',
        'Money Managers Long',
        'Money Managers Short',
        'Money Managers Net',
        'yoy % OECD Consumption Change',
        'non-OECD Consumption Growth',
        'Henry Hub Natural Gas Spot Price',
        'Coal Price',
    ],
    'Descrição': [
        'Mudança na produção de petróleo bruto da Arábia Saudita',
        'Mudança na produção de petróleo bruto WTI',
        'Estimativas de interrupções não planejadas no fornecimento global',
        'Estimativas de interrupções não planejadas no fornecimento de países não membros da OPEP',
        'Mudança na produção de países não membros da OPEP',
        'Mudança no inventário de combustíveis líquidos',
        'Capacidade de reserva',
        'Mudança percentual capacidade de reserva',
        'Taxa de fundos federais',
        'Îndice do Dólar Americano Nominal',
        'S&P 500',
        'Posição de contrato de mercado futuro dos EUA dos participantes físicos (comprado)',
        'Posição de contrato de mercado futuro dos EUA dos participantes físicos (vendido)',
        'Posição líquida de contrato de mercado futuro dos EUA dos participantes físicos',
        'Posição de contrado de mercado futuro dos EUA dos gestores de fundos (comprado)',
        'Posição de contrado de mercado futuro dos EUA dos gestores de fundos (vendido)',
        'Posição líquida de contrato de mercado futuro dos EUA dos gestores de fundos',
        'Mudança no consumo - OECD',
        'Mudança no consumo fora da OECD',
        'Preço do gás natural Henry Hub',
        'Preço do carvão',
    ],
    'Fonte': [
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'FED',
        'FED',
        'FED',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA',
        'EIA'
    ]
})