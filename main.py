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

    # Divisão do sidebar
    st.sidebar.header("📌 Navigation")
    page = st.sidebar.radio(
        "Choose a section:",
        ["About Me", "Statistics", "Finance", "Artificial Intelligence"],
    )

    st.sidebar.markdown("---")  # Separador visual

    if page == "Statistics":
        st.sidebar.header("📊 Statistics Models")
        stats_option = st.sidebar.radio(
            "Choose a Model:",
            [
                "Drunk Walk Simulation",
                "Midsquare Generator",
                "Linear Congruential Generator",
            ],
            index=None,
        )
    else:
        stats_option = None

    if page == "Finance":
        st.sidebar.header("💰 Finance Models")
        finance_option = st.sidebar.radio(
            "Choose a Model:",
            ["Portfolio Optimization", "Risk Analysis"],
            index=None,
        )
    else:
        finance_option = None

    if page == "Artificial Intelligence":
        st.sidebar.header("🧠 AI Models")
        ai_option = st.sidebar.radio(
            "Choose a Model:",
            ["Neural Networks", "Predictive Models"],
            index=None,
        )
    else:
        ai_option = None

    social_links()  # Exibir os links sociais no sidebar

    # Renderizar a página selecionada
    if page == "About Me":
        about_page()
    elif stats_option:
        modeling_simulation_page(stats_option)
    elif finance_option:
        st.write(f"🔍 Selected Finance Model: {finance_option}")
    elif ai_option:
        st.write(f"🤖 Selected AI Model: {ai_option}")


if __name__ == "__main__":
    main()
