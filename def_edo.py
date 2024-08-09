import numpy as np
from scipy.integrate import odeint
import streamlit as st
import plotly.graph_objects as go

# Título da aplicação
st.title("Modelo Corrupção-Fiscalização (Lotka-Volterra)")

# Entrada dos parâmetros do modelo
alpha_str = st.text_input("Alpha", value="1.0000")
try:
    alpha = float(alpha_str)
except ValueError:
    alpha = 1.0  # valor padrão ou algum tratamento de erro

beta_str = st.text_input("Beta", value="1.0000")
try:
    beta = float(beta_str)
except ValueError:
    beta = 1.0  # valor padrão ou algum tratamento de erro

p_str = st.text_input("p", value="1.0000")
try:
    p = float(p_str)
except ValueError:
    p = 1.0  # valor padrão ou algum tratamento de erro

q_str = st.text_input("q", value="1.0000")
try:
    q = float(q_str)
except ValueError:
    q = 1.0  # valor padrão ou algum tratamento de erro

T = st.number_input("Tempo", min_value=1, max_value=999999, value=30)
dt = 0.01
N = int(T/dt)

# Condições iniciais
C0 = st.number_input("População inicial de corrupção (C0)", min_value=1, max_value=999999, value=10)
F0 = st.number_input("População inicial de fiscalização (F0)", min_value=1, max_value=999999, value=10)
X0 = [C0, F0]

# Exibindo os valores com a precisão desejada
st.write(f"Alpha selecionado: {alpha:.4f}")
st.write(f"Beta selecionado: {beta:.4f}")
st.write(f"P selecionado: {p:.4f}")
st.write(f"Q selecionado: {q:.4f}")
st.write(f"População inicial de corrupção (C0): {C0}")
st.write(f"População inicial de fiscalização (F0): {F0}")

def derivative(X, t, alpha, beta, p, q):
    C, F = X
    dotx = C * (alpha - beta * C)
    doty = F * (-p + q * F)
    return np.array([dotx, doty])

# Definindo o tempo
Nt = 1000
tmax = T
t = np.linspace(0., tmax, Nt)

# Resolvendo o sistema
res = odeint(derivative, X0, t, args=(alpha, beta, p, q))
x, y = res.T

# Criando o gráfico usando Plotly
fig = go.Figure()

# Adicionando curvas para diferentes condições iniciais
fig.add_trace(go.Scatter(x=t, y=x, mode='lines', name='C'))
fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name='F'))

fig.update_layout(
    title="População de Corrupção vs Fiscalização",
    xaxis_title="População de Corrupção",
    yaxis_title="População de Fiscalização",
    legend_title="População Inicial"
)

st.plotly_chart(fig)
