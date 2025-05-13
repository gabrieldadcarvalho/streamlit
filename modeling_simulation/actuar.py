import streamlit as st
from functions.displaypdf import downloadPDF

def actuar_pdf():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/Rlogo.png", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.title("Resumo do Artigo “actuar: An R Package for Actuarial Science”")

    st.markdown(
        """
  Este PDF apresenta um resumo dos primeiros tópicos do artigo **"actuar: An R Package for Actuarial Science"**, elaborado em **RMarkdown**. O pacote **actuar** é amplamente utilizado em ciências atuariais e oferece ferramentas especializadas para:

  * **Modelagem de distribuições de perdas**
  * **Teoria do risco**
  * **Simulação de modelos hierárquicos compostos**
  * **Teoria da credibilidade**

  Neste resumo, demonstro diversas funções do pacote **actuar**, comparando-as com implementações próprias desenvolvidas sem o uso do pacote. O objetivo é destacar as funcionalidades oferecidas e analisar sua eficiência na modelagem atuarial.
    """
    )

    pdf_url = "https://github.com/gabrieldadcarvalho/loss_of_variables/raw/main/abstract/actuar/abstract_actuar.pdf"

    # Exibir o PDF e botão de download
    downloadPDF(pdf_url, "abstract_actuar")
