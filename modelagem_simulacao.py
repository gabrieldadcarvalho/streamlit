
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
