#%%

## PROJETO 1 - Visualizando dados em um Web App

import streamlit as st
from pathlib import Path
import pandas as pd

pasta_datasets = Path(__file__).parent.parent.parent / r'3_repositorio_estudos\1_Python\2_Trilha_Python_Office\2_4_Python_para_Usuarios_de_Excel\1_Arquivos_do_Curso\Material Aula\datasets'

data_frame = pasta_datasets / 'vendas.csv'
df = pd.read_csv(data_frame, sep=';', decimal=',')
st.dataframe(df)
