import streamlit as st
import requests
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def pagina_inicio():
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


import streamlit as st
import numpy as np


def bebado():
    st.title("Andar do Bêbado")
    st.write(
        "Bem-vindo à página do Andar do Bêbado. Neste exemplo, simularemos o comportamento de um bêbado que está caminhando aleatoriamente em uma grade. O objetivo é demonstrar como um agente pode se movimentar de forma aleatória do ponto (0,0) até o ponto (5,5) e visualizar sua trajetória."
    )

    direcao = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (norte, sul, leste, oeste)
    i = np.array([0, 0])
    f = np.array([5, 5])
    historico = [i.copy()]

    q = st.slider("Qual o limite de passos:", 0, 1000, 0)
    if q != 0:
        for passo in range(1, q + 1):
            direcao_escolhida = np.random.choice(range(len(direcao)))
            i += direcao[direcao_escolhida]
            historico.append(i.copy())
            if np.all(i == f):
                break

        st.write("Fim da simulação")
        fig = go.Figure(
            data=go.Scatter(
                x=[pos[0] for pos in historico],
                y=[pos[1] for pos in historico],
                mode="markers+text",
                text=[str(p) for p in range(len(historico))],
                textposition="bottom center",
            )
        )
        st.plotly_chart(fig)


def modelagem_simulacao():
    opcao = ["Andar do Bêbado", "Carteira Ibovespa"]

    escolha_m_s = st.sidebar.selectbox("Selecione uma opção", opcao)
    if escolha_m_s == "Andar do Bêbado":
        bebado()


def pagina_contato():
    st.title("Contato")
    st.write("Esta é a página de contato.")


def social_links():
    st.sidebar.title("Redes sociais")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button("GitHub", "https://github.com/gabrieldacarvalho")
    with col2:
        st.sidebar.link_button(
            "LinkedIn", "https://www.linkedin.com/in/gabriel-carvalho-ab38b7209/"
        )


def main():
    st.sidebar.title("Menu")
    opcoes = ["Página Inicial", "Modelagem e Simulação", "Contato"]
    escolha = st.sidebar.selectbox("Selecione uma página", opcoes)
    if escolha == "Página Inicial":
        pagina_inicio()
    elif escolha == "Modelagem e Simulação":
        modelagem_simulacao()
    elif escolha == "Contato":
        pagina_contato()
    social_links()


if __name__ == "__main__":
    main()
