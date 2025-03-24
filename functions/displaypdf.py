import streamlit as st
import requests


def downloadPDF(url, name):
    # Fazendo o download do PDF
    response = requests.get(url)

    if response.status_code == 200:
        # Criando um botão para download do PDF
        st.download_button(
            label="📥 Baixar PDF",
            data=response.content,
            file_name=f"{name}.pdf",
            mime="application/pdf",
        )
    else:
        st.error(f"Erro ao carregar o PDF. Status: {response.status_code}")
