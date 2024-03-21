import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt
from pathlib import Path
from config import *

# Configuraçao da Página
page_config()
# page_style()
path = Path(__file__).parent / 'data'
tickers = pd.read_csv(path / 'tickers_sa.csv')


st.title('Análise de Ações')


dt_end = dt.datetime.today()
dt_start = dt.datetime(dt_end.year - 1, dt_end.month, dt_end.day)


with st.container():
    st.header('Insira as informações solicitadas abaixo')
    col1, col2, col3 = st.columns(3)
    with col1:
        ticker = st.selectbox('Selecione o código da CIA:',tickers, placeholder='Selecione o código')
    with col2:
        dt_start = st.date_input('Data inicial:', value=dt_start, format='DD/MM/YYYY')
    with col3:
        dt_end = st.date_input('Data final:', value=dt_end, format='DD/MM/YYYY')


# Dados da Api
df = yf.download(ticker, start=dt_start, end=dt_end)


# Métricas
ult_atualizacao = df.index.max().strftime('%d/%m/%Y') # última data de fechamento
ult_cotacao = round(df.loc[df.index.max(), 'Adj Close'], 2) # última cotação encontrada
prim_cotacao = round(df.loc[df.index.min(), 'Adj Close'], 2) # primeira cotação encontrada
menor_cotacao = round(df['Adj Close'].min(), 2) # menor cotação
maior_cotacao = round(df['Adj Close'].max(), 2) # maior cotação
delta = round(((ult_cotacao - prim_cotacao) / prim_cotacao) * 100, 2)


with st.container():
    with col1:
        col11, col12, col13 = st.columns(3)
        with col11:
            st.image(f'https://raw.githubusercontent.com/thefintz/icones-b3/main/icones/{ticker.rstrip(".SA")}.png', width=100)
        with col12:
            st.metric(f'Última Cotação - {ult_atualizacao}', value=f"R${'{:,.2f}'.format(ult_cotacao)}", delta=f'{delta}%')
        with col13:
            pass
    with col2:
        st.metric('Menor cotação do Período', value=f'R${"{:,.2f}".format(menor_cotacao)}')
    with col3:
        st.metric('Maior cotação do Período', value=f'R${"{:,.2f}".format(maior_cotacao)}')

st.divider()

with st.container():
    data, graf = st.columns(2)

    data.dataframe(df.tail(10), width=600)
    graf.line_chart(df['Adj Close'], height=400)




