#%%

## PROJETO 1 - Visualizando dados em um Web App

import streamlit as st
from pathlib import Path
import pandas as pd

pasta_datasets = Path(__file__).parent.parent.parent / r'3_repositorio_estudos\1_Python\2_Trilha_Python_Office\2_4_Python_para_Usuarios_de_Excel\1_Arquivos_do_Curso\Material Aula\datasets'

data_frame = pasta_datasets / 'vendas.csv'
df = pd.read_csv(data_frame, sep=';', decimal=',', index_col=0)


colunas = list(df.columns)
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas:', colunas, colunas)

coluna1, coluna2 = st.sidebar.columns(2)
coluna_filtro = coluna1.selectbox('Selecione a coluna:', sorted(list(colunas_selecionadas))) 
valor_filtro = coluna2.selectbox('Selecione o valor:', sorted(list(df[coluna_filtro].unique()))) 

status_filtrar = coluna1.button('Filtrar')
status_limpar = coluna2.button('Limpar')

if status_filtrar:
    st.dataframe(df.loc[df[coluna_filtro] == valor_filtro, colunas_selecionadas], height=800)
elif status_limpar:
    st.dataframe(df[colunas_selecionadas], height=800)
else:
    st.dataframe(df[colunas_selecionadas], height=800)
