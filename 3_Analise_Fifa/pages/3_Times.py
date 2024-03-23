#%%
import streamlit as st
import pandas as pd

# Carregar o favicon
favicon = '🎮'

# Definir o favicon
st.set_page_config(page_title='Fifa', page_icon=favicon, layout="wide")

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox("Clube", clubes)

df_filtrado = df_data[(df_data["Club"] == clube)].set_index("Name")

st.image(df_filtrado.iloc[0]["Club Logo"])
st.markdown(f'## {clube}')

colunas = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtrado[colunas]
             , column_config={"Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100)
                            , "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filtrado["Wage(£)"].max())
                            , "Photo": st.column_config.ImageColumn()
                            , "Flag": st.column_config.ImageColumn("Country")
                            
                              
                              }
             )