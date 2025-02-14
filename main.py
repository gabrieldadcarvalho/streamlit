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


def modeling_simulation_page():
    option = st.sidebar.radio(
        "Select a Method:",
        (
            "Drunk Walk Simulation",
            "Midsquare Generator",
            "Linear Congruential Generator",
        ),
    )

    if option == "Drunk Walk Simulation":
        drunk_walk()
    elif option == "Midsquare Generator":
        midsquare()
    elif option == "Linear Congruential Generator":
        congruence()


def contact_page():
    st.title("Contact")
    st.write("This is the contact page.")


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
    page = st.sidebar.radio("Navigation", ["About Me"])

    st.sidebar.markdown("---")  # Separador

    # Seção de Modelagem e Simulação
    st.sidebar.header("📊 Statistics")
    stats_options = st.sidebar.radio(
        "Choose a Model:",
        [
            "Drunk Walk Simulation",
            "Midsquare Generator",
            "Linear Congruential Generator",
        ],
        index=None,
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Finanças (Placeholder)
    st.sidebar.header("💰 Finance")
    finance_options = st.sidebar.radio(
        "Choose a Model:",
        ["Portfolio Optimization", "Risk Analysis"],
        index=None,
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Inteligência Artificial (Placeholder)
    st.sidebar.header("🧠 Artificial Intelligence")
    ai_options = st.sidebar.radio(
        "Choose a Model:",
        ["Neural Networks", "Predictive Models"],
        index=None,
    )

    social_links()  # Exibe os links sociais

    # Lógica para exibição das páginas
    if page == "About Me":
        about_page()
    elif stats_options:
        modeling_simulation_page()
    elif finance_options:
        st.write(f"🔍 Selected Finance Model: {finance_options}")
    elif ai_options:
        st.write(f"🤖 Selected AI Model: {ai_options}")


if __name__ == "__main__":
    main()
