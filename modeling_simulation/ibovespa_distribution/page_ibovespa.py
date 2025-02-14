import streamlit as st

def show_data_simulation_pdf():
    st.title("Análise Estatística dos Retornos Diários do Índice Ibovespa")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/ibov.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
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

    pdf_url = "https://nbviewer.org/github/gabrieldadcarvalho/modeling_simulatiton/blob/main/works/ibov_index/data_simulation.pdf"

    pdf_viewer = f"""
        <embed src="{pdf_url}" width="800" height="600" type="application/pdf">
    """
    st.markdown(pdf_viewer, unsafe_allow_html=True)
    #st.components.v1.html(pdf_viewer, height=700)
