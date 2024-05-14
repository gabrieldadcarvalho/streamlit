import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd


def bebado():
    def chega_5_5(i, f, direcao, historico):
        for _ in range(2000):
            i += direcao[np.random.choice(len(direcao))]
            historico.append(i.copy())
            if np.all(i == f):
                st.success("O BÊBADO CHEGOU NO PONTO (5,5)")
                return True
        st.error("O BÊBADO SE PERDEU DEPOIS DE 2000 PASOS")
        st.write("Se quiser recomeçar, aperte em aplicar novamente")
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
        'Os critérios de parada são: "Simular" e "Chegar no ponto (5,5)". Ao selecionar "Simular", você pode definir a\
            quantidade de passos que o bêbado dará a partir de 0 a 5000 passos, de acordo com a quantidade desejada.\
                Ao selecionar "Chegar no ponto (5,5)", o bêbado tentará mover-se para o ponto (5,5).\
                    Se não chegar em no máximo 2000 passos, o programa é encerrado.'
    )
    st.warning(
        "**GRANDES QUANTIDADES DE SIMULAÇÕES PODEM DEIXAR A PÁGINA MAIS LENTA** ",
        icon="⚠️",
    )

    criterio = st.radio(
        "Selecione uma opção",
        ("Simular", "Chegar no ponto (5,5)"),
        format_func=lambda x: "Simular" if x == "Simular" else "Chegar no ponto (5,5)",
    )
    direcao = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (norte, sul, leste, oeste)
    i = np.array([0, 0])
    f = np.array([5, 5])
    historico = [i.copy()]
    recomecar = False

    if criterio == "Simular":
        q = st.slider("Qual o limite de passos:", 0, 5000, 0)
        if st.button("Aplicar"):
            for passo in range(1, q + 1):
                i += direcao[np.random.choice(len(direcao))]
                historico.append(i.copy())
                if np.all(i == f):
                    st.success(
                        "O BÊBADO CHEGOU NO PONTO (5,5) depois de "
                        + str(len(historico) - 1)
                        + " pasos"
                    )
                    break
            else:
                if not np.all(i == f):
                    st.error("O BÊBADO SE PERDEU DEPOIS DE " + str(q) + " PASOS")
                    st.write("Se quiser recomeçar, aperte em aplicar novamente")
                    recomecar = True

    elif criterio == "Chegar no ponto (5,5)":
        if st.button("Aplicar"):
            recomecar = chega_5_5(i, f, direcao, historico)

    if len(historico) > 1 and not recomecar:
        st.write("Gráfico de passos: ")
        fig = go.Figure()

        # Otimizando a criação do gráfico
        x_coords, y_coords = zip(*historico)
        fig.add_trace(
            go.Scatter(
                x=x_coords,
                y=y_coords,
                mode="lines",
                line=dict(color="#ADD8E6", width=2),
                name="Passos",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[historico[0][0]],
                y=[historico[0][1]],
                mode="markers",
                marker=dict(color="green", size=10),
                name="Partida",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[historico[-1][0]],
                y=[historico[-1][1]],
                mode="markers",
                marker=dict(color="red", size=10),
                name="Chegada",
            )
        )

        st.plotly_chart(fig)


def midsquare():
    st.title("Método Mid-Square")
    st.markdown(
        "O método Mid-Square é uma técnica de geração de números aleatórios. Neste método, o primeiro número (semente/seed) com **n** dígitos é elevado ao quadrado. \
                Em seguida, são utilizados os **n** dígitos centrais do resultado como o próximo número na sequência. No entanto, pode haver casos em que não conseguimos obter \
                os **n** dígitos centrais do quadrado. Para ajustar isso, devemos incluir zeros à esquerda se necessário."
    )
    st.warning("**Exemplo:**", icon="✏️")
    st.write(
        "x¹ = 124\
             \n⮩ x¹ ** 2 = 1<u>**537**</u>6\
             \nx² = 537\
             \n⮩ x² ** 2 = 288369 ➟ 02<u>**883**</u>69 (correção)\
             \nx³ = 883",
        unsafe_allow_html=True,
    )
    st.write("_" * 3)

    # Usando st.session_state para armazenar os dados da sessão
    if "lista_n" not in st.session_state:
        st.session_state.lista_n = []

    st.session_state.lista_n.append(
        str(st.number_input("Insira um número inicial de n dígitos:", 0, 99999, 0))
    )
    q = int(st.number_input("Quantos números aleatórios você deseja: ", 1, 1000, 1))
    padronizar = st.radio(
        "Você quer padronizar os números gerados?",
        ("Sim", "Não"),
        format_func=lambda x: "Sim" if x == "Sim" else "Não",
    )

    if st.button("Gerar Números"):
        for x in range(q):
            x_2 = str(int(st.session_state.lista_n[x]) ** 2)
            if st.session_state.lista_n[x][0] == "0":
                x_2 = x_2.zfill(len(x_2) + 1)
            n = len(str(st.session_state.lista_n[x]))
            n2 = len(x_2)
            mid_x_2 = x_2[(n2 - n) // 2 : (n2 + n) // 2]
            st.session_state.lista_n.append(mid_x_2)
        st.session_state.df_n = pd.DataFrame(
            st.session_state.lista_n, columns=["Nº Gerados"]
        )

        # Criando colunas para a exibição dos dados
        col1, col2 = st.columns([1, 3])
        with col1:
            st.dataframe(st.session_state.df_n)
        with col2:
            if padronizar == "Sim":
                df_n_p_list = [
                    int(num) / 10 ** len(str(num))
                    for num in st.session_state.df_n["Nº Gerados"]
                ]
                st.session_state.df_n_p = pd.DataFrame(
                    df_n_p_list, columns=["Nº Padronizados"]
                )
                st.dataframe(st.session_state.df_n_p)
                with col1:
                    st.download_button(
                        label="Baixar Dados",
                        data=pd.concat(
                            [st.session_state.df_n, st.session_state.df_n_p], axis=1
                        ).to_csv(index=False),
                        file_name="mid_square.csv",
                        mime="text/csv",
                    )
            else:
                with col1:
                    st.download_button(
                        label="Baixar Dados",
                        data=st.session_state.df_n.to_csv(index=False),
                        file_name="mid_square.csv",
                        mime="text/csv",
                    )


def congruencia():
    st.title("Método de Congruência Linear - LCG")
    st.markdown(
        "O método de congruência é uma técnica de geração de números pseudo-aleatórios. Neste método, o termo n "
    )
    st.warning("**Exemplo:**", icon="✏️")
    st.write(
        "x¹ = 124\
             \n⮩ x¹ ** 2 = 1<u>**537**</u>6\
             \nx² = 537\
             \n⮩ x² ** 2 = 288369 ➟ 02<u>**883**</u>69 (correção)\
             \nx³ = 883",
        unsafe_allow_html=True,
    )

    st.write("_" * 3)

    if "lista_n" not in st.session_state:
        st.session_state.lista_n = []
    q = st.number_input("Quantos número você quer gerar? ", 1, 999999, 1)
    m = st.number_input("Insira o módulo 'm' (0 < m)", 1, 99999, 0)
    a = st.number_input("Insira o multiplicador 'a' (0 < a < m)", 1, (m - 1), 1)
    c = st.number_input("Insira o incrmento 'c' (0 <= c < m)", 0, (m - 1), 1)
    st.session_state.lista_n.append(
        st.number_input("Insira um número inicial de n dígitos:", 0, (m - 1), 0)
    )
    for i in range(q + 1):
        st.session_state.lista_n.append((a * st.session_state.lista_n[i] + c) % m)

    st.session_state.lista_n = pd.DataFrame(
        st.session_state.lista_n, columns=["Nº Gerados"]
    )
