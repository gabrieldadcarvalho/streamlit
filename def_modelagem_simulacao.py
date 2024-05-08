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
    st.title("Método Mid-Square")
    st.markdown("O método Mid-Square é uma técnica de geração de números aleatórios. Neste método, o primeiro número (semente/seed) com **n** dígitos é elevado ao quadrado. \
                Em seguida, são utilizados os **n** dígitos centrais do resultado como o próximo número na sequência. No entanto, pode haver casos em que não conseguimos obter \
                os **n** dígitos centrais do quadrado. Para ajustar isso, devemos incluir zeros à esquerda se necessário.")
    st.warning("**Exemplo:**", icon="✏️")
    st.write("x¹ = 124\
             \n⮩ x¹ ** 2 = 1<u>**537**</u>6\
             \nx² = 537\
             \n⮩ x² ** 2 = 288369 ➟ 02<u>**883**</u>69 (correção)\
             \nx³ = 883",unsafe_allow_html=True)
    st.write('_'*3)
    lista_i_s = [str(st.number_input("Insira um número inicial de n dígitos:", 0, 99999, 0))]
    q = int(st.number_input("Quantos números aleatórios você deseja: ", 1, 1000, 1))
    if q != 0 and int(lista_i_s[0]) > 0:
        for x in range(q):
            i_2 = int(lista_i_s[x]) ** 2
            i_2_s = [int(d) for d in str(i_2)]
            if (
                len(i_2_s) % 2 != 0
                and len(lista_i_s[x]) % 2 == 0
                or len(i_2_s) % 2 == 0
                and int(lista_i_s[x]) % 2 != 0
                or lista_i_s[x][0] == "0"
            ):
                i_2_s = ["0"] * (len(i_2_s) - len(str(int(lista_i_s[x])))) + i_2_s
                media_i_1 = len(lista_i_s[x]) / 2
                media_i_2 = len(i_2_s) / 2
                sub = media_i_2 - media_i_1
                i_2_s = i_2_s[int(sub) : int(len(i_2_s) - sub)]
                lista_i_s.append("".join(str(d) for d in i_2_s))
            else:
                media_i_1 = len(lista_i_s[x]) / 2
                media_i_2 = len(i_2_s) / 2
                sub = media_i_2 - media_i_1
                i_2_s = i_2_s[int(sub) : int(len(i_2_s) - sub)]
                lista_i_s.append("".join(str(d) for d in i_2_s))
        df_i = pd.DataFrame(lista_i_s, columns=["Nº Gerados"])
        st.dataframe(df_i)