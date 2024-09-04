import pandas as pd
import streamlit as st

dimensao = ['Sales Channel','Order Date', 'Ship Date', 'Country', 'Item Type']
medida = ['Units Sold', 'Total Profit']
agregador = ['sum', 'mean', 'count', 'min', 'max']

cols = st.columns(4)
linhas = cols[0].multiselect('Dimensôes Linha', dimensao)
colunas = cols[1].multiselect('Dimensôes Coluna', dimensao)
valor = cols[2].selectbox('Medidas', medida)
agg = cols[3].selectbox('Agregador', agregador)
if (len(linhas) > 0) & (len(colunas) > 0) & (linhas != colunas):
    st.dataframe(
        st.session_state['df'].pivot_table(
            index=linhas,
            columns=colunas,
            values=valor,
            aggfunc=agg,
            fill_value=0
        )
    )
