import streamlit as st
import requests
from modeling_simulation.congruence import congruence
from modeling_simulation.drunk_walk import drunk_walk
from modeling_simulation.midsquare import midsquare
from modeling_simulation.ibovespa_distribution.page_ibovespa import (
    show_data_simulation_pdf,
)
from finance.sharpe_optimization import sharpe_optimization  # Importando a função p_sp_max
from ai.health_insurance import nn_insurence  
from modeling_simulation.actuar import actuar_pdf

def about_page():
    raw_url = (
        "https://raw.githubusercontent.com/gabrieldacarvalho/streamlit/main/README.md"
    )
    response = requests.get(raw_url)

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("pictures/me_picture.jpg", width=150)
    with col2:
        st.title("Bem-vindo ao meu site Streamlit!")
    
    st.markdown(response.text)


def modeling_simulation_page(option):
    if option == "Drunk Walk Simulation":
        drunk_walk()
    elif option == "Midsquare Generator":
        midsquare()
    elif option == "Linear Congruential Generator":
        congruence()
    elif option == "Ibovespa Distribution":
        show_data_simulation_pdf()
    elif option == "Actuarial Modeling with the Actuar Package":
        actuar_pdf()


def finance_page(option):
    if option == "Portfolio Optimization":
        sharpe_optimization()

def ai_page(option):
    if option == "Neural Networks in Health Insurance":
        nn_insurence()

def social_links():
    st.sidebar.title("Social Links")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button("GitHub", "https://github.com/gabrieldadcarvalho")
    with col2:
        st.sidebar.link_button(
            "LinkedIn", "https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/"
        )


def reset_selection(except_key):
    """Reseta todas as opções do session_state, exceto a que foi selecionada."""
    keys = ["about_option", "stats_option", "finance_option", "ai_option"]
    for key in keys:
        if key != except_key:
            st.session_state[key] = None  # Reseta todas, exceto a escolhida


def main():
    st.sidebar.image("pictures/logo_streamlit_gc.png", width=200)

    # Inicializa os estados se não existirem
    if "about_option" not in st.session_state:
        st.session_state["about_option"] = None
    if "stats_option" not in st.session_state:
        st.session_state["stats_option"] = None
    if "finance_option" not in st.session_state:
        st.session_state["finance_option"] = None
    if "ai_option" not in st.session_state:
        st.session_state["ai_option"] = None

    # Seção "About Me"
    st.sidebar.header("📌 About Me")
    about_option = st.sidebar.radio(
        "Select an option:",
        ["Resume"],
        key="about_option",
        on_change=reset_selection,
        args=("about_option",),
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Estatística
    st.sidebar.header("📊 Statistics")
    stats_option = st.sidebar.radio(
        "Choose a Model:",
        [
            "Drunk Walk Simulation",
            "Midsquare Generator",
            "Linear Congruential Generator",
            "Actuarial Modeling with the Actuar Package",
            "Ibovespa Distribution",
        ],
        key="stats_option",
        on_change=reset_selection,
        args=("stats_option",),
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Finanças
    st.sidebar.header("💰 Finance")
    finance_option = st.sidebar.radio(
        "Choose a Model:",
        ["Portfolio Optimization", "Risk Analysis"],
        key="finance_option",
        on_change=reset_selection,
        args=("finance_option",),
    )

    st.sidebar.markdown("---")  # Separador

    # Seção de Inteligência Artificial
    st.sidebar.header("🧠 Artificial Intelligence")
    ai_option = st.sidebar.radio(
        "Choose a Model:",
        ["Neural Networks in Health Insurance"],
        key="ai_option",
        on_change=reset_selection,
        args=("ai_option",),
    )

    social_links()  # Exibe os links sociais

    # Lógica de navegação
    if stats_option:
        modeling_simulation_page(stats_option)
    elif finance_option:
        finance_page(finance_option)  # Passa a opção para a função finance_page
    elif ai_option:
        ai_page(ai_option)
    else:
        about_page()  # Se nada for selecionado, exibe "About Me"


if __name__ == "__main__":
    main()
