from re import split
import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import pandas as pd


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


def bebado():
    def chega_5_5(i, f, direcao, historico):
        cont = 0
        while not np.all(i == f):
            direcao_escolhida = np.random.choice(range(len(direcao)))
            i += direcao[direcao_escolhida]
            historico.append(i.copy())
            cont += 1
            if cont == 5000:
                st.error("O BÊBADO SE PERDEU DEPOIS DE 5000 PASOS")
                st.write("Se quiser recomeçar, aperte em aplicar novamente")
                return True
        st.success("O BÊBADO CHEGOU NO PONTO (5,5)")
        return False

    st.title("Andar do Bêbado")
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("pictures/bebado.jpg", width=100)
    with col2:
        st.write(
            "Bem-vindo à página do Andar do Bêbado. Neste exemplo, simularemos o comportamento de um bêbado que está caminhando aleatoriamente em uma grade. O objetivo é demonstrar como um agente pode se movimentar de forma aleatória do ponto (0,0) até o ponto (5,5) e visualizar sua trajetória."
        )
    st.write(
        'Os critérios de parada são: "Simular" e "Chegar no ponto (5,5)". Ao selecionar "Simular", o bêbado dará uma sequência de 0 a 1000 passos, de acordo com a quantidade desejada. Ao selecionar "Chegar no ponto (5,5)", o bêbado tentará mover-se para o ponto (5,5). Se não chegar em no máximo 5000 passos, o programa é encerrado.'
    )

    criterio = st.selectbox(
        "Selecione uma opção", ["Simular", "Chegar no ponto (5,5)"], index=None
    )
    direcao = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (norte, sul, leste, oeste)
    i = np.array([0, 0])
    f = np.array([5, 5])
    historico = [i.copy()]
    recomecar = False

    if criterio == "Simular":
        q = st.slider("Qual o limite de passos:", 0, 1000, 0)
        if st.button("Aplicar"):
            if q != 0:
                for passo in range(1, q + 1):
                    direcao_escolhida = np.random.choice(range(len(direcao)))
                    i += direcao[direcao_escolhida]
                    historico.append(i.copy())
                    if np.all(i == f):
                        st.success(
                            "O BÊBADO CHEGOU NO PONTO (5,5) depois de "
                            + str(len(historico) - 1)
                            + " pasos"
                        )
                        break
                    elif passo == q and not np.all(i == f):
                        st.error("O BÊBADO SE PERDEU DEPOIS DE " + str(q) + " PASOS")
                        st.write("Se quiser recomeçar, aperte em aplicar novamente")
                        recomecar = True

    elif criterio == "Chegar no ponto (5,5)":
        if st.button("Aplicar"):
            recomecar = chega_5_5(i, f, direcao, historico)

    if len(historico) > 1 and not recomecar:
        st.write("Histórico de passos: ")
        st.dataframe(historico)
        st.write("Gráfico de passos: ")
        fig = go.Figure(
            data=go.Scatter(
                x=[pos[0] for pos in historico],
                y=[pos[1] for pos in historico],
                text=[
                    "Passo " + str(q) if q == len(historico) - 1 else ""
                    for q in range(len(historico))
                ],
                marker=dict(
                    color=[
                        "red" if q == len(historico) - 1 else "lightblue"
                        for q in range(len(historico))
                    ]
                ),
                textposition="bottom center",
                mode="markers+text",
            )
        )
        st.plotly_chart(fig)


def midsquare():
    lista_i = [st.number_input("Insira um número inicial de n dígitos:", 0, 9999, 0)]
    q = int(st.number_input("Quantos números aleatórios você deseja: ", 1, 1000, 1))
    if q != 0 and lista_i[0] > 1:
        for x in range(q):
            i_2 = lista_i[x] ** 2
            if (
                i_2 % 2 != 0
                and lista_i[x] % 2 == 0
                or i_2 % 2 == 0
                and lista_i[x] % 2 != 0
            ):
                i_2 = [int(d) for d in str(i_2)]
                i_2 = ["0"] * (int(len(i_2) - len(str(lista_i[x])))) + i_2
                st.write(i_2)
                media_i_1 = len(str(lista_i[x])) / 2
                media_i_2 = len(i_2) / 2
                sub = media_i_2 - media_i_1
                i_2 = i_2[int(sub) : int(len(i_2) - sub)]
                lista_i.append(int("".join(str(d) for d in i_2)))
            else:
                i_2 = [int(d) for d in str(i_2)]
                media_i_1 = len(str(lista_i[x])) / 2
                media_i_2 = len(i_2) / 2
                sub = media_i_2 - media_i_1
                i_2 = i_2[int(sub) : int(len(i_2) - sub)]
                lista_i.append(int("".join(str(d) for d in i_2)))
        df_i = pd.DataFrame(lista_i, columns=["Nº Gerados"])
        st.dataframe(df_i)


def modelagem_simulacao():
    opcao = ["Andar do Bêbado", "Midsquare"]

    escolha_m_s = st.sidebar.selectbox("Selecione uma opção", opcao)
    if escolha_m_s == "Andar do Bêbado":
        bebado()
    elif escolha_m_s == "Midsquare":
        midsquare()


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
    opcoes = ["Apresentação", "Modelagem e Simulação"]
    escolha = st.sidebar.selectbox("Selecione uma página", opcoes)
    if escolha == "Modelagem e Simulação":
        modelagem_simulacao()
    elif escolha == "Apresentação":
        pagina_inicio()
    social_links()


if __name__ == "__main__":
    main()
