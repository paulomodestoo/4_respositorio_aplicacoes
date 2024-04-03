#%%

## PROJETO 1 - Visualizando dados em um Web App

import streamlit as st
from pathlib import Path
import pandas as pd

pasta_datasets = Path(__file__).parent.parent.parent.parent / r'3_repositorio_estudos\1_Python\2_Trilha_Python_Office\2_4_Python_para_Usuarios_de_Excel\1_Arquivos_do_Curso\Material Aula\datasets'

df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', sep=';', decimal=',', index_col=0)
df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', sep=';', decimal=',')
df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', sep=';', decimal=',')

df_filiais['cidade/estado'] = df_filiais['cidade'] + '/' + df_filiais['estado']
lista_filiais = sorted(list(df_filiais['cidade/estado']))
filial_selecionada = st.sidebar.selectbox('Selecione a filial:', lista_filiais) 

lista_vendedores = df_filiais.loc[df_filiais['cidade/estado'] == filial_selecionada, 'vendedores'].iloc[0]
lista_vendedores = sorted(lista_vendedores.strip('][').replace("'", '').split(','))
vendedor_selecionado_ = st.sidebar.selectbox('Selecione o vendedor:', lista_vendedores)

lista_produtos = list(df_produtos['nome'])
vendedor_selecionado_ = st.sidebar.selectbox('Selecione o produto:', lista_produtos)

st.dataframe(df_vendas)
st.dataframe(df_filiais)
st.dataframe(df_produtos)