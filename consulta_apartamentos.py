import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração inicial
st.title("Consulta de Apartamentos em Alphaville")
st.subheader("Encontre apartamentos na faixa de preço desejada")

# Função para carregar os dados
@st.cache
def load_data():
    return pd.read_csv('apartamentos_certo.csv')

data = load_data()

# Configuração de faixas de preço
st.sidebar.header("Filtros de Preço")
faixas = {
    "R$ 150.000 - R$ 379.000": (150000, 379000),
    "R$ 379.001 - R$ 759.000": (379001, 759000),
    "R$ 759.001 - R$ 1.280.000": (759001, 1280000),
    "Acima de R$ 1.280.001": (1280001, 5500000)
}

# Filtro baseado em faixas predefinidas
faixa_selecionada = st.sidebar.selectbox("Selecione uma faixa de preço", list(faixas.keys()))
min_preco, max_preco = faixas[faixa_selecionada]

filtered_data_faixa = data[(data['Preço'] >= min_preco) & (data['Preço'] <= max_preco)]
st.write(f"Apartamentos na faixa de preço: **{faixa_selecionada}**")
st.write(f"Número de apartamentos encontrados: {len(filtered_data_faixa)}")
st.dataframe(filtered_data_faixa)

# Gráfico para os dados filtrados pela faixa
if not filtered_data_faixa.empty:
    st.bar_chart(filtered_data_faixa['Preço'])
else:
    st.write("Nenhum apartamento encontrado nesta faixa de preço.")

# Filtro personalizado usando um slider
st.sidebar.header("Filtro Personalizado de Preço")
min_value = int(data['Preço'].min())
max_value = int(data['Preço'].max())

faixa_preco = st.sidebar.slider(
    "Selecione a faixa de preço personalizada",
    min_value=min_value,
    max_value=max_value,
    value=(150000, 550000),
    step=10000
)

filtered_data_personalizado = data[(data['Preço'] >= faixa_preco[0]) & (data['Preço'] <= faixa_preco[1])]

# Tabela e gráfico para o filtro personalizado
st.write(f"Apartamentos na faixa de preço personalizada: R$ {faixa_preco[0]:,} a R$ {faixa_preco[1]:,}")
st.write(f"Número de apartamentos encontrados: {len(filtered_data_personalizado)}")
st.dataframe(filtered_data_personalizado)

if not filtered_data_personalizado.empty:
    st.bar_chart(filtered_data_personalizado['Preço'])
else:
    st.write("Nenhum apartamento encontrado na faixa de preço personalizada.")
