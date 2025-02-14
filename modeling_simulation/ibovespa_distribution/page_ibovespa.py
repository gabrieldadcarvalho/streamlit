import streamlit as st
import os


def display_html_work():
    # Título
    st.title("Análise Estatística dos Retornos Diários do Índice Ibovespa")
    st.subheader("Comparação entre Distribuições Normal e t de Student")

    # Carregando o arquivo HTML
    html_file_path = "ibovespa_distribution.html"  # Substitua com o caminho real do arquivo HTML

    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as file:
            html_content = file.read()

        # Exibe o conteúdo HTML no Streamlit
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.error("Arquivo HTML não encontrado.")
