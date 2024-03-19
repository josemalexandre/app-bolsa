
import streamlit as st
from pathlib import Path

img_pasta = Path(__file__).parent / 'img'

def page_config():
    return st.set_page_config(
        layout='wide',
        page_icon='assets\img\grafico.ico',
        page_title='Análise B3'
    )


def page_style():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    return st.markdown(hide_st_style, unsafe_allow_html=True)