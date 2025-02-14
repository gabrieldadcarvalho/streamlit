import streamlit as st
import requests


def displayHTML(html_url, name):
    # Faz o download do arquivo HTML
    response = requests.get(html_url)

    if response.status_code != 200:
        # Criando um botão para download do PDF
        st.download_button(
            label="📥 Baixar HTML",
            data=response.content,
            file_name=f"{name}.html",
            mime="application/html",
        )
        st.error("Erro ao carregar o arquivo HTML.")
        return

    # Obtém o conteúdo do HTML
    html_content = response.text

    # Exibe no Streamlit
    st.components.v1.html(html_content, height=900, scrolling=True)
