import streamlit as st
from functions.displaypdf import downloadPDF


def ibovespa_distribution_pdf():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/ibov.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Análise Estatística dos Retornos Diários do Índice Ibovespa")
    st.markdown(
        """
    Este PDF apresenta uma análise detalhada dos retornos diários do Índice Bovespa (IBOV), com o objetivo de 
    determinar se a distribuição de probabilidade desses retornos pode ser adequadamente modelada por uma distribuição 
    **Normal** ou por uma distribuição **t de Student**. A conclusão deste estudo é fundamental para a realização de 
    simulações futuras, como o modelo de **Monte Carlo**, ou outras abordagens de simulação, pois a distribuição 
    de probabilidade dos retornos do índice foi identificada e compreendida. 
    
    Ao explorar o conteúdo deste estudo, você terá uma compreensão mais aprofundada da distribuição dos dados financeiros 
    do IBOV e seu comportamento estatístico.
    """
    )

    pdf_url = "https://github.com/gabrieldadcarvalho/modeling_simulatiton/raw/main/works/ibov_index/data_simulation.pdf"

    # Exibir o PDF
    downloadPDF(pdf_url, "ibovespa_distribution")
