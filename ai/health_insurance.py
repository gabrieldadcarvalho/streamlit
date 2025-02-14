import streamlit as st
from functions.displaypdf import displayPDF


def nn_insurence():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/insurance.png", width=100
        )  # Substitua pelo caminho real da imagem

    with col2:
        st.title(
            "Modelagem de Redes Neurais para Previsão de Custos em Seguros de Saúde"
        )

    st.markdown(
        """
    Este PDF apresenta um estudo detalhado sobre a aplicação de **redes neurais** na previsão de custos em seguros de saúde. O trabalho foi desenvolvido durante a disciplina **ET645 - REDES NEURAIS**, oferecida pelo Departamento de Estatística da Universidade Federal de Pernambuco.

    O foco principal do estudo foi a **análise exploratória dos dados**, utilizando abordagens estatísticas para compreender melhor os padrões e relações entre as variáveis. Foram aplicados:

    * **Normalização de dados** para melhorar o desempenho dos modelos.
    * **Preparação e limpeza de dados** para garantir a qualidade e consistência dos dados.
    * **Teste t de Student** para avaliar a diferença entre variáveis binárias e numéricas;
    * **Análise de correlação** para identificar relações entre variáveis;
    * **Teste ANOVA** para examinar associações entre variáveis categóricas multiníveis e variáveis numéricas.

    Esse estudo fornece uma base sólida para a construção de modelos preditivos mais robustos e eficientes no contexto de seguros de saúde.
    """
    )

    pdf_url = "https://github.com/gabrieldadcarvalho/neural_network/raw/main/projeto/Neural_Network_Projetc.pdf"

    # Exibir o PDF
    displayPDF(pdf_url, "nn_health_insurance")
