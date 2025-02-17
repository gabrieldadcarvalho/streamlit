import streamlit as st
from functions.displaypdf import displayPDFile


def sulamericaPDF():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/sulamerica.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Business Case - SulAmérica Seguros")

    st.markdown(
        """
    O relatório a seguir foi elaborado e publicado publicamente durante minha atuação como **Analista Macroeconômico** na **Liga de Mercado Financeiro da UFPB**. Ele apresenta uma análise detalhada da **SulAmérica Seguros**, baseada em dados financeiros e econômicos disponíveis no mercado.

    O estudo inclui uma avaliação tanto do setor quanto da empresa, culminando na apresentação de um **valuation**, desenvolvido em conjunto por todos os integrantes do grupo.

    ### **Minha contribuição**
    Minha principal atuação no projeto foi na **análise setorial e no estudo da atuação da empresa no mercado**, fornecendo insights estratégicos para a avaliação do negócio.

    """
    )

    pdf = "streamlit/finance/pdf/sulamerica.pdf"

    # Exibir o PDF e botão de download
    displayPDFile(pdf, "sulamerica")
