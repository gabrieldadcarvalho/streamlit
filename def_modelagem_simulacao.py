import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd


def bebado():
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

    # if len(historico) > 1:
    #     # Adiciona o botão de download do arquivo CSV
    #     x_coords, y_coords = zip(*historico)
    #     historico_df = pd.DataFrame({"x": x_coords, "y": y_coords})
    #     csv = historico_df.to_csv(index=False)
    #     st.download_button(
    #         label="Baixar histórico como CSV",
    #         data=csv,
    #         file_name="historico_bebado.csv",
    #         mime="text/csv",
    #     )


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

    # Obter inputs do usuário
    numero_inicial = str(
        st.number_input("Insira um número inicial de n dígitos:", 0, 99999, 0)
    )
    quantidade_numeros = int(
        st.number_input("Quantos números aleatórios você deseja: ", 1, 1000, 1)
    )
    padronizar = st.radio(
        "Você quer padronizar os números gerados?",
        ("Sim", "Não"),
        format_func=lambda x: "Sim" if x == "Sim" else "Não",
    )

    # Inicializar a lista de números gerados
    lista_numeros = [numero_inicial]

    # Gerar números aleatórios usando o método Mid-Square
    if st.button("Gerar Números"):
        for i in range(quantidade_numeros):
            x_2 = str(int(lista_numeros[i]) ** 2)
            if lista_numeros[i][0] == "0":
                x_2 = x_2.zfill(len(x_2) + 1)
            n = len(lista_numeros[i])
            n2 = len(x_2)
            mid_x_2 = x_2[(n2 - n) // 2 : (n2 + n) // 2]
            lista_numeros.append(mid_x_2)

        # Criar DataFrames para exibir os resultados
        df_numeros = pd.DataFrame(lista_numeros, columns=["Nº Gerados"])
        col1, col2 = st.columns([1, 3])

        # Exibir resultados
        with col1:
            st.dataframe(df_numeros)

        if padronizar == "Sim":
            numeros_padronizados = [
                int(num) / 10 ** len(str(num)) for num in df_numeros["Nº Gerados"]
            ]
            df_numeros_padronizados = pd.DataFrame(
                numeros_padronizados, columns=["Nº Padronizados"]
            )
            with col2:
                st.dataframe(df_numeros_padronizados)
            with col1:
                st.download_button(
                    label="Baixar Dados",
                    data=pd.concat(
                        [df_numeros, df_numeros_padronizados], axis=1
                    ).to_csv(index=False),
                    file_name="mid_square.csv",
                    mime="text/csv",
                )
        else:
            with col1:
                st.download_button(
                    label="Baixar Dados",
                    data=df_numeros.to_csv(index=False),
                    file_name="mid_square.csv",
                    mime="text/csv",
                )


def congruencia():
    st.title("Método de Congruência Linear - LCG")
    st.markdown(
        "O método de congruência linear (LCG) é uma técnica de geração de números pseudo-aleatórios.  \
        Neste método, o próximo número na sequência é gerado usando a seguinte fórmula:\
        \n<div align='center'><span style='font-weight: bold; color: red;'>X_(n+1) = (a * X_n + c) mod m</span></div>\
        \n \
        \nOnde:  \
        \n* **X_n** é o número atual na sequência.  \
        \n* **a** é o multiplicador.  \
        \n* **c** é o incremento.  \
        \n* **m** é o módulo.  \
        \n \
        \nA escolha adequada dos parâmetros a, c e m é crucial para garantir a qualidade dos números pseudo-aleatórios gerados.",
        unsafe_allow_html=True,
    )
    st.warning("**Exemplo:**", icon="✏️")
    st.write(
        "Vamos considerar os seguintes parâmetros: a = 2, c = 1, m = 10.\
        \nSe o valor inicial (semente) for X_0 = 3, os próximos números da sequência seriam:\
        \n* X_1 = (2 * 3 + 1) mod 10 = 7  \
        \n* X_2 = (2 * 7 + 1) mod 10 = 5  \
        \n* X_3 = (2 * 5 + 1) mod 10 = 1  \
        \n* X_4 = (2 * 1 + 1) mod 10 = 3\
        \n \
        \nObserve que a sequência começa a se repetir após X_4. A qualidade do gerador LCG depende fortemente da escolha dos parâmetros."
    )
    st.write("_" * 3)
    # Obter parâmetros do usuário
    modulo = st.number_input("Insira o módulo (0 < m)", 1, 99999, 1)
    multiplicador = st.number_input(
        "Insira o multiplicador (0 < a < m):", 0, (modulo - 1), 0
    )
    incremento = st.number_input(
        "Insira o incremento (0 \u2264 c < m):", 0, (modulo - 1), 0
    )
    numero_inicial = st.number_input(
        "Insira um número inicial (0 \u2264 x0 < m):", 0, (modulo - 1), 0
    )
    quantidade_numeros = st.number_input(
        "Quantos números você quer gerar? ", 1, 999999, 1
    )
    padronizar = st.radio("Você quer padronizar os números gerados?", ("Sim", "Não"))
    if st.button("Gerar Números"):
        # Validação de entradas (adicione mais validações se necessário)
        if modulo <= 0:
            st.error("O módulo deve ser maior que 0.")
        elif not (0 < multiplicador < modulo):
            st.error("O multiplicador deve estar entre 0 e m.")
        elif not (0 <= incremento < modulo):
            st.error("O incremento deve estar entre 0 e m (inclusive).")
        elif not (0 <= numero_inicial < modulo):
            st.error("O número inicial deve estar entre 0 e m-1.")
        elif quantidade_numeros <= 0:
            st.error(
                "A quantidade de números a serem gerados deve ser um valor positivo."
            )
        else:
            # Gerar números pseudo-aleatórios usando o LCG
            numeros_gerados = np.zeros(quantidade_numeros + 1, dtype=int)
            numeros_gerados[0] = numero_inicial

            for i in range(quantidade_numeros):
                numeros_gerados[i + 1] = (
                    multiplicador * numeros_gerados[i] + incremento
                ) % modulo

            # Exibir resultados
            dataframe_numeros_gerados = pd.DataFrame(
                numeros_gerados, columns=["Números Gerados"]
            )
            col1, col2 = st.columns([1, 3])
            with col1:
                st.dataframe(dataframe_numeros_gerados)

            if padronizar == "Sim":
                numeros_padronizados = [
                    int(num) / int(modulo)
                    for num in dataframe_numeros_gerados["Números Gerados"]
                ]
                dataframe_numeros_padronizados = pd.DataFrame(
                    numeros_padronizados, columns=["Números Padronizados"]
                )
                with col2:
                    st.dataframe(dataframe_numeros_padronizados)
                with col1:
                    st.download_button(
                        label="Baixar Dados",
                        data=pd.concat(
                            [
                                dataframe_numeros_gerados,
                                dataframe_numeros_padronizados,
                            ],
                            axis=1,
                        ).to_csv(index=False),
                        file_name="congruentes_lineares.csv",
                        mime="text/csv",
                    )
            else:
                with col1:
                    st.download_button(
                        label="Baixar Dados",
                        data=dataframe_numeros_gerados.to_csv(index=False),
                        file_name="congruentes_lineares.csv",
                        mime="text/csv",
                    )
