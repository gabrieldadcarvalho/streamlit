import streamlit as st
from functions.displayhtml import displayHTML


def m_linear_regression_journal():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/journals.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Análise de Regressão Múltipla para Dados de Jornais")

    st.markdown(
        """
    Este relatório tem como objetivo realizar uma **análise exploratória** dos dados contidos no arquivo journals.txt, seguida da proposição de um **modelo de regressão linear múltipla** para compreender melhor as relações entre as variáveis.

    O trabalho foi desenvolvido como parte da disciplina **ET661 - Modelos de Regressão para Atuária**, oferecida pelo **Departamento de Ciências Atuariais da UFPE**. Esta versão do relatório contém exclusivamente a parte da análise e modelagem realizada por mim no contexto do projeto acadêmico.
    """
    )

    pdf_url = "https://github.com/gabrieldadcarvalho/analise_regressao/raw/main/multiple_linear_regression/journals/regression_jornals.pdf"

    # Exibir o PDF e botão de download
    downloadPDF(pdf_url, "regression_jornals")
