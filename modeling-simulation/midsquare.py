import streamlit as st
import pandas as pd


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
