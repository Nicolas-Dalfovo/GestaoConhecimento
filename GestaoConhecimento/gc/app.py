import pandas as pd
import datetime as dt
import streamlit as st
import pygwalker as pyg


@st.cache_data
def load_database():
    df = pd.read_excel('Data\AmazonSalesData.xlsx')
    df['Order Month'] = df['Order Date'].astype(str)
    df['Order Year'] = df['Order Date'].astype(str)
    df['Ship Year'] = df['Ship Date'].astype(str)
    df['Ship Month'] = df['Ship Date'].astype(str)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    df =df.drop(columns=['Order ID', 'Order Priority'])
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Ship Year'] = df['Ship Date'].dt.year
    df['Ship Month'] = df['Ship Date'].dt.month
    return df


st.session_state['dimensao_tempo'] = ['Order Date', 'Ship Date', 'Order Month', 'Ship Month']
st.session_state['medida'] = ['Units Sold', 'Total Profit', 'Total Revenue']
st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']
st.set_page_config(page_title="Gestão do Conhecimento", layout="wide")
st.session_state['df'] = load_database()
st.session_state['dimensao'] = [
    'Sales Channel', 'Country', 'Region',  'Item Type'
]
st.title("Gestão do Conhecimento")

pg = st.navigation(
    {
        'Introdução':[
            st.Page(page='Introducao/tabela.py', title='Tabela', icon=':material/house:'),
            st.Page(page='introducao/cubo.py', title='Cubo', icon=':material/help:'),
            st.Page(page='introducao/dashboard.py', title='Dashboard', icon=':material/help:'),
            st.Page(page='introducao/visualizacao.py', title='Visualização', icon=':material/help:'),
        ],
        "Visualização":[
            st.Page(page='visualizacao/descritiva.py', title='Analise Descritiva', icon=':material/house:'),
            st.Page(page='visualizacao/diagnostica.py', title='Analise diagnostica', icon=':material/house:'),
            st.Page(page='visualizacao/preditiva.py', title='Analise Preditiva', icon=':material/house:'),
            st.Page(page='visualizacao/preescritiva.py', title='Analise Preescritiva', icon=':material/house:'),
        ]
    }
)
pg.run()