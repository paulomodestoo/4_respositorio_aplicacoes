#%% 
import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

# Carregar o favicon
favicon = '🎮'

# Definir o favicon
st.set_page_config(page_title='Fifa', page_icon=favicon, layout="wide")



@st.cache_data
def carregar_dados():
    data_base = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv')
    return data_base


if "data" not in st.session_state:
    df_data = pd.read_csv(carregar_dados(), index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.markdown('# FIFA23 OFFICIAL DATASET! ⚽')
st.sidebar.markdown('Desenvolvido por [Paulo Modesto.](https://www.linkedin.com/in/paulo-modesto/)')

botao = st.button('Acesse os dados no Kaggle')
if botao:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    '''
    O conjunto de dados dos jogadores de futebol de **2017 a 2023** apresenta uma ampla gama de informações detalhadas sobre os profissionais deste esporte. Compreendendo **mais de 17.000 registros**, ele abrange desde dados demográficos e características físicas dos jogadores até estatísticas de jogo, detalhes contratuais e afiliações clubísticas. 
    
    Destinado a analistas, pesquisadores e aficionados pelo futebol, este conjunto de dados constitui uma ferramenta valiosa para explorar diversos aspectos do mundo do futebol. Permite uma análise aprofundada dos atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento dos jogadores e a evolução do desenvolvimento do jogador ao longo do período considerado.
    '''

)
