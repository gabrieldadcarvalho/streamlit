import streamlit as st
import requests
import streamlit.modeling_simulation.congruence as congruence
import streamlit.modeling_simulation.drunk_walk as drunk_walk
import streamlit.modeling_simulation.inverse_transformation as inverse_transformation
import streamlit.modeling_simulation.midsquare as midsquare


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
    opcao = st.sidebar.radio(
        "Problemas:",
        ("Drunk of Walk Simulation", "Midsquare Generator", "Linear Congruential Generator"),
        format_func=lambda x: (
            "Drunk of Walk"
            if x == "Drunk of Walk"
            else ("Midsquare" if x == "Midsquare" else "Linear Congruential Generator")
        ),
    )
    if opcao == "Drunk of Walk":
        drunk_walk()
    elif opcao == "Midsquare":
        midsquare()
    elif opcao == "":
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
    opcoes = st.sidebar.radio(
        "Select a page:",
        ("About Me", "Modeling and Simulation"),
        format_func=lambda x: (
            "About Me" if x == "About Me" else "Modeling and Simulation"
        ),
    )
    if opcoes == "Modeling and Simulation":
        modeling_simulation_page()
    elif opcoes == "About Me":
        about_page()
    social_links()


if __name__ == "__main__":
    main()
