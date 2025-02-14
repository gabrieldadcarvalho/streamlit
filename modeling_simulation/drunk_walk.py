import streamlit as st
import numpy as np
import plotly.graph_objects as go


def drunk_walk():
    st.title("Andar do Bêbado")

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image(
            "pictures/bebado.jpg", width=100
        )  # Substitua pelo caminho real da imagem
    with col2:
        st.write(
            "Bem-vindo à página do Andar do Bêbado. Neste exemplo, simularemos o comportamento de um bêbado que está "
            "caminhando aleatoriamente em uma grade. O objetivo é demonstrar como um agente pode se movimentar de "
            "forma aleatória do ponto (0,0) até o ponto (5,5) e visualizar sua trajetória."
        )

    st.write(
        "Você pode simular o andar do bêbado por um número específico de passos ou até que ele chegue ao ponto (5,5). "
        "Se o bêbado não alcançar o ponto (5,5) em 2000 passos, a simulação será interrompida."
    )

    st.warning(
        "Simulações com grande número de passos podem deixar a página mais lenta.",
        icon="⚠️",
    )

    criterio = st.radio(
        "Selecione uma opção:",
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
                        f"O BÊBADO CHEGOU NO PONTO (5,5) depois de {len(historico) - 1} passos"
                    )
                    break
            else:  # Executa se o loop não for interrompido pelo 'break'
                st.error(f"O BÊBADO SE PERDEU DEPOIS DE {q} PASSOS")
                st.write("Se quiser recomeçar, aperte em aplicar novamente")
                recomecar = True

    elif criterio == "Chegar no ponto (5,5)":
        if st.button("Aplicar"):
            for _ in range(2000):
                i += direcao[np.random.choice(len(direcao))]
                historico.append(i.copy())
                if np.all(i == f):
                    st.success("O BÊBADO CHEGOU NO PONTO (5,5)")
                    break
            else:
                st.error("O BÊBADO SE PERDEU DEPOIS DE 2000 PASOS")
                st.write("Se quiser recomeçar, aperte em aplicar novamente")
                recomecar = True

    if len(historico) > 1 and not recomecar:
        st.write("Gráfico de passos: ")
        fig = go.Figure()
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
