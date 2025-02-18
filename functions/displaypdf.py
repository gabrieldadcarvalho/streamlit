import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import requests


def displayPDF(url, name):
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
        # Exibe o PDF utilizando o conteúdo binário
        pdf_viewer(input=response.content, width=700)
    else:
        st.error(f"Erro ao carregar o PDF. Status: {response.status_code}")
