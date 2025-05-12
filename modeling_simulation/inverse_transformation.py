import streamlit as st
import numpy as np
import pandas as pd

def inverse_transformation(n_padronizado):
    dist = st.radio(
        "Transformar os números em que tipo de distribuição:", ("Discreta", "Contínua")
    )
    if dist == "Continua":
        tipo = st.radio(
            "Você quer transformar os números em qual distribuição?",
            ("Exponencial", "Normal", "Gama", "Lognormal"),
        )
    else:
        tipo = st.radio(
            "Você quer transformar os números em qual distribuição?",
            ("Geométrica", "Binomial", "Hipergeométrica", "Poison"),
        )
    n_trans = []
    if tipo == "Exponencial":
        parametro = st.number_input("Qual valor de lambda? ", 1, 999999, 1)
        for i in range(len(n_padronizado)):
            n_trans.append((-1 / parametro) * np.log(1 - n_padronizado[i]))

    return n_trans
