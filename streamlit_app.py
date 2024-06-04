import streamlit as st
import requests
import def_modelagem_simulacao


def pag_inicio():
    # URL do arquivo README.md no repositório do GitHub
    raw_url = (
        "https://raw.githubusercontent.com/gabrieldacarvalho/streamlit/main/README.md"
    )

    # Fazendo a requisição para obter o conteúdo do arquivo
    response = requests.get(raw_url)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pictures/me_picture.jpg", width=150)
    with col2:
        st.markdown(response.text)


def pag_modelagem_simulacao():
    opcao = st.sidebar.radio(
        "Problemas:",
        ("Andar do Bêbado", "Midsquare", "Congruentes Lineares"),
        format_func=lambda x: (
            "Andar do Bêbado"
            if x == "Andar do Bêbado"
            else ("Midsquare" if x == "Midsquare" else "Congruentes Lineares")
        ),
    )
    if opcao == "Andar do Bêbado":
        def_modelagem_simulacao.bebado()
    elif opcao == "Midsquare":
        def_modelagem_simulacao.midsquare()
    elif opcao == "Congruentes Lineares":
        def_modelagem_simulacao.congruencia()


def pagina_contato():
    st.title("Contato")
    st.write("Esta é a página de contato.")


def social_links():
    st.sidebar.title("Redes sociais")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button("GitHub", "https://github.com/gabrieldadcarvalho")
    with col2:
        st.sidebar.link_button(
            "LinkedIn", "https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/"
        )


def main():
    st.sidebar.image("pictures/logo_streamlit_gc.png", width=200)
    opcoes = st.sidebar.radio(
        "Selecione uma página",
        ("Sobre Mim", "Modelagem e Simulação"),
        format_func=lambda x: (
            "Sobre mim" if x == "Sobre Mim" else "Modelagem e Simulação"
        ),
    )
    if opcoes == "Modelagem e Simulação":
        pag_modelagem_simulacao()
    elif opcoes == "Sobre Mim":
        pag_inicio()
    social_links()


if __name__ == "__main__":
    main()
