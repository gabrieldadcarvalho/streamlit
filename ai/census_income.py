import streamlit as st
from functions.displayhtml import displayHTML


def ml_census_income():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("pictures/ml.png", width=100)  # Substitua pelo caminho real da imagem
    with col2:
        st.title(
            "Machine Learning para Classificação da Renda de Pessoas em Estados Unidos”"
        )

    st.markdown(
    """
      O presente estudo teve como foco uma **análise exploratória aprofundada** do conjunto de dados do **Censo dos EUA**, disponibilizado no repositório da UCI. O principal objetivo foi compreender as relações entre as variáveis e identificar padrões que permitissem a classificação da renda das pessoas em duas categorias: **≤50K e >50K**.

      Esse projeto foi desenvolvido no contexto da disciplina **IF699 - Aprendizagem de Máquina**, oferecida pelo **Centro de Informática da Universidade Federal de Pernambuco (CIn-UFPE)**, em colaboração com [**Arthur Bezerra Calado**](https://github.com/arthur-calado) e **Pedro Henrique Sarmento de Paula**, ambos alunos do CIn-UFPE.

      ### **Minhas contribuições**
      - **Análise exploratória dos dados**, investigando distribuições e correlações entre variáveis;  
      - **Pré-processamento e limpeza dos dados**, garantindo a qualidade e consistência do conjunto de dados;  
      - **Transformação e padronização de variáveis**, facilitando o aprendizado do modelo;  
      - **Implementação de Redes Neurais Artificiais (RNA)**, utilizadas para a classificação da renda.  

      O estudo não apenas evidenciou padrões interessantes nos dados, mas também demonstrou a aplicabilidade das **Redes Neurais** na modelagem de problemas de classificação no contexto socioeconômico.
    """
    )
    # URL do HTML convertido
    html_url = "https://raw.githubusercontent.com/gabrieldadcarvalho/AM-GRAD-2024-1/refs/heads/main/adult_uc_irvine/PJT-AM.html"

    # Chama a função para exibir
    downloadPDF(html_url, "PJT-AM")
