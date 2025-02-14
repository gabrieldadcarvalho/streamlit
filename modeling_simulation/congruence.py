import streamlit as st
import numpy as np
import pandas as pd


def congruence():
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
        \n **mod** é a abreviação de módulo, que é o resto de um divisão.\
        \n* **m** é o módulo.  \
        \n \
        \nA escolha adequada dos parâmetros a, c e m é crucial para garantir a qualidade dos números pseudo-aleatórios gerados.",
        unsafe_allow_html=True,
    )
    st.warning("**Exemplo:**", icon="✏️")
    st.write(
        "Vamos considerar os seguintes parâmetros: a = 2, c = 1, m = 10.\
        \nSe o valor inicial (semente) for X_0 = 3, os próximos números da sequência seriam: \
        \n* X_1 = (2 * 3 + 1) mod 10 = 7  \
        \n* X_2 = (2 * 7 + 1) mod 10 = 5  \
        \n* X_3 = (2 * 5 + 1) mod 10 = 1  \
        \n* X_4 = (2 * 1 + 1) mod 10 = 3  \
        \n* X_5 = (2 * 3 + 1) mod 10 = 7  \
        \n* X_6 = (2 * 7 + 1) mod 10 = 5  \
        \n* X_7 = (2 * 5 + 1) mod 10 = 1  \
        \n* X_8 = (2 * 1 + 1) mod 10 = 3  \
        \n*... \
        \n \
        \nObserve que a sequência começa a se repetir após X_4. A qualidade do gerador LCG depende fortemente da escolha dos parâmetros."
    )
    st.write("_" * 3)
    # Obter parâmetros do usuário
    modulo = st.number_input("Insira o módulo (0 < m)", 1, 99999, 1, format="%d")
    multiplicador = st.number_input(
        "Insira o multiplicador (0 < a < m):",
        0.00000001,
        float(modulo - 0.00000001),
        0.00000001,
    )
    incremento = st.number_input(
        "Insira o incremento (0 \u2264 c < m):", 0.0, float(modulo - 0.00000001), 0.0
    )
    numero_inicial = st.number_input(
        "Insira um número inicial (0 \u2264 x0 < m):",
        0.0,
        float(modulo - 0.00000001),
        0.0,
    )
    quantidade_numeros = st.number_input(
        "Quantos números você quer gerar?", 1, 999999, 1, format="%d"
    )
    padronizar = st.radio("Você quer padronizar os números gerados?", ("Sim", "Não"))
    if st.button("Gerar Números"):
        # Validação de entradas (adicione mais validações se necessário)
        if modulo <= 0:
            st.error("O módulo deve ser maior que 0.")
        elif not (0 < multiplicador < modulo):
            st.error("O multiplicador deve estar entre (0,m).")
        elif not (0 <= incremento < modulo):
            st.error("O incremento deve estar entre [0,m).")
        elif not (0 <= numero_inicial < modulo):
            st.error("O número inicial deve estar entre [0,m).")
        elif quantidade_numeros <= 0:
            st.error("A quantidade de números a serem gerados deve ser [1,999999].")
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
                    num / modulo for num in dataframe_numeros_gerados["Números Gerados"]
                ]
                transformacao_inversa(numeros_padronizados)
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
