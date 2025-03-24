import streamlit as st
from functions.displayhtml import downloadHTML


def american_wallet_html():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/stock.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Análise de portfólio dos EUA")

    st.markdown(
        """
    Este relatório apresenta uma **análise de portfólio** de ativos financeiros nos Estados Unidos, fazendo a comparação entre a carteira com **preço ajustado** e **normal**. O estudo foi desenvolvido como parte da disciplina **EC437 - Mercado de Capitais**, oferecida pelo D**epartamento de Ciências Atuariais da Universidade Federal de Pernambuco (UFPE)**.

    O principal objetivo do projeto foi explorar a construção e avaliação de carteiras de investimento, com base em métricas financeiras fundamentais. Embora esta análise tenha sido focada nos preços dos ativos, futuras iterações podem incluir uma abordagem mais abrangente, incorporando **indicadores econômicos e financeiros** para um diagnóstico mais aprofundado do mercado.
    """
    )

    html_url = "https://github.com/gabrieldadcarvalho/capital_market/raw/main/1_activity/1_activity_capital_market.html"

    # Exibir o PDF e botão de download
    downloadHTML(html_url, "american_wallet")
