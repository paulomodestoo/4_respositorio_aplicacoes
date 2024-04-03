#%%

## PROJETO 1 - Visualizando dados em um Web App

import streamlit as st
from pathlib import Path
import pandas as pd

pasta_datasets = Path(__file__).parent.parent.parent / r'3_repositorio_estudos\1_Python\2_Trilha_Python_Office\2_4_Python_para_Usuarios_de_Excel\1_Arquivos_do_Curso\Material Aula\datasets'

df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', sep=';', decimal=',', index_col=0)
df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', sep=';', decimal=',')
df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', sep=';', decimal=',')

colunas = list(df_vendas.columns)
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas, colunas)

coluna1, coluna2 = st.sidebar.columns(2)
coluna_filtro = coluna1.selectbox('Selecione a coluna:', sorted(list(colunas_selecionadas))) 
valor_filtro = coluna2.selectbox('Selecione o valor:', sorted(list(df_vendas[coluna_filtro].unique()))) 

status_filtrar = coluna1.button('Filtrar')
status_limpar = coluna2.button('Limpar')

if status_filtrar:
    st.dataframe(df_vendas.loc[df_vendas[coluna_filtro] == valor_filtro, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df_vendas[colunas_selecionadas], height=800)
else:
    st.dataframe(df_vendas[colunas_selecionadas], height=800)


