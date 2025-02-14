import streamlit as st
import requests
from modeling_simulation.congruence import congruence
from modeling_simulation.drunk_walk import drunk_walk
from modeling_simulation.inverse_transformation import inverse_transformation
from modeling_simulation.midsquare import midsquare


def about_page():
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


def modeling_simulation_page(option):
    """Executa a função correspondente com base na opção selecionada."""
    if option == "Drunk Walk Simulation":
        drunk_walk()
    elif option == "Midsquare Generator":
        midsquare()
    elif option == "Linear Congruential Generator":
        congruence()


def social_links():
    st.sidebar.title("Social Links")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button("GitHub", "https://github.com/gabrieldadcarvalho")
    with col2:
        st.sidebar.link_button(
            "LinkedIn", "https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/"
        )


import streamlit as st
import requests
from modeling_simulation.congruence import congruence
from modeling_simulation.drunk_walk import drunk_walk
from modeling_simulation.inverse_transformation import inverse_transformation
from modeling_simulation.midsquare import midsquare


def about_page():
    raw_url = (
        "https://raw.githubusercontent.com/gabrieldacarvalho/streamlit/main/README.md"
    )
    response = requests.get(raw_url)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pictures/me_picture.jpg", width=150)
    with col2:
        st.markdown(response.text)


def modeling_simulation_page(option):
    if option == "Drunk Walk Simulation":
        drunk_walk()
    elif option == "Midsquare Generator":
        midsquare()
    elif option == "Linear Congruential Generator":
        congruence()


def social_links():
    st.sidebar.title("Social Links")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button("GitHub", "https://github.com/gabrieldadcarvalho")
    with col2:
        st.sidebar.link_button(
            "LinkedIn", "https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/"
        )


def main():
    st.sidebar.image("pictures/logo_streamlit_gc.png", width=200)

    # Seção "About Me"
    st.sidebar.header("📌 About Me")
    option = st.sidebar.radio(
        "Select an option:",
        ["Resume"]
    )
    st.sidebar.markdown("Saiba mais sobre mim e meu trabalho.")

    st.sidebar.markdown("---")  # Separador

    # Seção de Estatística
    st.sidebar.header("📊 Statistics")
    option = st.sidebar.radio(
        "Choose a Model:",
        [
            "Drunk Walk Simulation",
            "Midsquare Generator",
            "Linear Congruential Generator",
        ],
        index=None,
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Finanças
    st.sidebar.header("💰 Finance")
    option = st.sidebar.radio(
        "Choose a Model:",
        ["Portfolio Optimization", "Risk Analysis"],
        index=None,
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Inteligência Artificial
    st.sidebar.header("🧠 Artificial Intelligence")
    option = st.sidebar.radio(
        "Choose a Model:",
        ["Neural Networks", "Predictive Models"],
        index=None,
    )

    social_links()  # Exibe os links sociais

    # Lógica de navegação
    if option:
        modeling_simulation_page(option)
    elif option:
        st.write(f"🔍 Selected Finance Model: {option}")
    elif option:
        st.write(f"🤖 Selected AI Model: {option}")
    else:
        about_page()  # Se nada for selecionado, exibe "About Me"


if __name__ == "__main__":
    main()
