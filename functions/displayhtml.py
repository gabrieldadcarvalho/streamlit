import streamlit as st
import requests


def displayHTML(html_url, name):
    # Faz o download do arquivo HTML
    response = requests.get(html_url)

    if response.status_code == 200:
        # Obtém o conteúdo do HTML
        html_content = response.text
        st.download_button(
            label="📥 Baixar HTML",
            data=html_content,
            file_name=f"{name}.html",
            mime="application/html",
        )
        # Exibe no Streamlit
        st.components.v1.html(html_content, height=900, scrolling=True)

    else:
        st.error(f"Erro ao carregar o HTML. Status: {response.status_code}")
