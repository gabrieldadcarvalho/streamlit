import streamlit as st
import requests

# URL do arquivo README.md no repositório do GitHub
raw_url = "https://raw.githubusercontent.com/gabrieldacarvalho/gabrieldacarvalho/main/README.md"

# Fazendo a requisição para obter o conteúdo do arquivo
response = requests.get(raw_url)


st.image("https://www.example.com/sua_foto.jpg", caption='Sua Foto', use_column_width=True)

st.markdown(response.text)
