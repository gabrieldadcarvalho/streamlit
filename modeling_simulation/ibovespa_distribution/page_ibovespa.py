import streamlit as st
import base64
import requests
import tempfile


def displayPDF(url):
    # Baixar o PDF da URL
    response = requests.get(url)
    if response.status_code == 200:
        # Criar um arquivo temporário para armazenar o PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
            tmp_pdf.write(response.content)
            pdf_path = tmp_pdf.name

        # Ler e converter para base64
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        # Gerar HTML para embutir o PDF
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

        # Mostrar o PDF no Streamlit
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error("Erro ao baixar o PDF. Verifique a URL.")


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

    # Exibir o PDF
    displayPDF(pdf_url)

