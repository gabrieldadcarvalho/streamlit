import streamlit as st
from functions.displayhtml import downloadHTML


def wine_html():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/wine.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Machine Learning para Classificação da Qualidade de Vinhos")

    st.markdown(
        """
    O presente estudo teve como foco uma **análise exploratória detalhada** do conjunto de dados **Wine Quality**, disponibilizado no repositório da UCI. O principal objetivo foi desenvolver **modelos de machine learning** para prever a qualidade do vinho com base em suas características físico-químicas.

    Este projeto foi desenvolvido no contexto da disciplina **IF699 - Aprendizagem de Máquina**, oferecida pelo **Centro de Informática da Universidade Federal de Pernambuco (CIn-UFPE)**, em colaboração com [**Arthur Bezerra Calado**](https://github.com/arthur-calado) e **Pedro Henrique Sarmento de Paula**, ambos alunos do CIn-UFPE.

    ### **Minhas contribuições**
    - **Análise exploratória dos dados**, investigando distribuições, padrões e correlações entre variáveis;
    - **Pré-processamento e limpeza dos dados**, garantindo a consistência e integridade do conjunto de dados;
    - **Transformação e padronização de variáveis**, otimizando o desempenho dos modelos de aprendizado de máquina.

    Os modelos de machine learning foram desenvolvidos por **Arthur Bezerra Calado** e **Pedro Henrique Sarmento de Paula**, enquanto minha principal atuação foi na **análise exploratória e no pré-processamento dos dados**, etapas fundamentais para garantir a qualidade do treinamento dos modelos.
    """
    )
    # URL do HTML convertido
    html_url = "https://raw.githubusercontent.com/gabrieldadcarvalho/AM-GRAD-2024-1/refs/heads/main/wine_quality/analitic_wine.html"

    # Chama a função para exibir
    downloadPDF(html_url, "wine_quality")
