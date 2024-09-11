import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px


cols = st.columns(3)
colunas = cols[0].multiselect(
        'Dimensões Coluna',
        st.session_state['dimensao'] + st.session_state['dimensao_tempo']
)
valor = cols[1].selectbox(
    'Medidas',
    st.session_state['medida']
)
cor= cols[2].selectbox(
    'cor',
    colunas
)
tabs = st.tabs(['Treemap', 'Sunburst', 'Sankey', 'TimeSeries'])
if len(colunas) > 2:
    with tabs[0]:
        fig = px.treemap(
            st.session_state['df'],
            path=colunas,
            values=valor,
            color=cor,
            height=800,
            width=1200
        )
        fig.update_traces(textinfo='label+value')
        st.plotly_chart(fig)
    with tabs[1]:
        fig = px.sunburst(
            st.session_state['df'],
            path=colunas,
            values=valor,
            color=cor,
            height=800,
            width=1200
        )
        fig.update_traces(textinfo='label+value')
        st.plotly_chart(fig)
