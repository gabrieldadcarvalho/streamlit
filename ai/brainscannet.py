import streamlit as st
from functions.displaypdf import downloadPDF


def brainscannet():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/insurance.png", width=100
        )  # Substitua pelo caminho real da imagem

    with col2:
        st.title(
            "BrainScanNet: Diagnósticos Inteligentes Para Tumores Cerebrais Usando IA"
        )

    st.markdown(
        """
    # Classificação de Tumores Cerebrais com CNN

    Este relatório apresenta a implementação e avaliação de um modelo de **Redes Neurais Convolucionais (CNN)** para a **classificação de tumores cerebrais**. O modelo foi treinado para identificar três tipos de tumores:

    - **Glioma**  
    - **Meningioma**  
    - **Pituitário**  
    - **Cérebros sem tumores (controle)**  

    Para o treinamento, utilizamos o **Brain Tumor MRI Dataset**, disponível no [Kaggle](https://www.kaggle.com/), e a implementação foi realizada na linguagem **Python**. O estudo visa comparar diferentes abordagens e técnicas de regularização para otimizar o desempenho do modelo, avaliando métricas como:  

    1) **Perda**  
    2) **Acurácia**  
    3) **F1-Score**  

    ## Contexto Acadêmico  

    Este projeto foi desenvolvido no contexto da disciplina **IF867 - Introdução à Aprendizagem Profunda**, oferecida pelo **Centro de Informática da Universidade Federal de Pernambuco (CIn-UFPE)**.  

    O trabalho foi realizado em colaboração com:  

    - [**Leandro Freitas**](https://github.com/LeandroLuiz02)  
    - [**Lucas Sales**](https://github.com/LukasSales)  

    ## Código-Fonte e Pesos do Modelo  

    O código-fonte do projeto e os pesos da **RNN treinada** foram disponibilizados no **GitHub**, permitindo que qualquer pessoa possa aplicar o modelo em novos dados.  

    - **Repositório do Projeto:** [GitHub](https://github.com/gabrieldadcarvalho/BrainScanNet/tree/main)  
    """
    )

    pdf_url = "https://github.com/gabrieldadcarvalho/BrainScanNet/raw/main/relatorio_final_brainscannet.pdf"

    # Exibir o PDF
    downloadPDF(pdf_url, "nn_health_insurance")
