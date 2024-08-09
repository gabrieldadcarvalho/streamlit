import numpy as np
import streamlit as st
import plotly.graph_objects as go
from scipy.integrate import odeint
from scipy.optimize import fsolve

# Definição das funções diferenciais do modelo
def dX_dt(X, t, a, b, c, d):
    x, y = X
    dxdt = a * x - b * x * y
    dydt = c * x * y - d * y
    return [dxdt, dydt]

# Função para encontrar o ponto de equilíbrio
def equilibrium(X, a, b, c, d):
    x, y = X
    return [a * x - b * x * y, c * x * y - d * y]

# Interface Streamlit
st.title("Trajetórias e Campos Vetoriais com o Modelo Lotka-Volterra")

# Definir parâmetros
a = st.number_input("a", value=1.0, format="%.5f")
b = st.number_input("b", value=0.1, format="%.5f")
c = st.number_input("c", value=0.1, format="%.5f")
d = st.number_input("d", value=1.0, format="%.5f")
t0 = st.number_input("Tempo inicial", value=0.0, format="%.5f")
tn = st.number_input("Tempo final", value=30.0, format="%.5f")
nb_points = st.number_input("Número de pontos na grade", value=20, step=1)

# Parâmetros do sistema
t = np.linspace(t0, tn, 500)
X_f1 = np.array([10, 5])  # Ponto final (ajuste conforme necessário)

# Encontrar o ponto de equilíbrio
initial_guess = [1, 1]  # Chute inicial para o ponto de equilíbrio
equilibrium_point = fsolve(equilibrium, initial_guess, args=(a, b, c, d))

# Gráficos de trajetórias e campos vetoriais
fig = go.Figure()

# Trajetórias
values = np.linspace(0.3, 0.9, 5)
colors = ['rgba(255, 0, 0, 0.5)', 'rgba(255, 128, 0, 0.5)', 'rgba(255, 255, 0, 0.5)', 'rgba(128, 255, 0, 0.5)', 'rgba(0, 255, 255, 0.5)']  # Cores predefinidas para cada trajetória

for v, color in zip(values, colors):
    X0 = v * X_f1
    X = odeint(dX_dt, X0, t, args=(a, b, c, d))
    fig.add_trace(go.Scatter(x=X[:, 0], y=X[:, 1], mode='lines', line=dict(width=3.5*v, color=color), name=f'X0=({X0[0]:.1f}, {X0[1]:.1f})'))

# Grade de pontos e campos vetoriais
x = np.linspace(0, X_f1[0] * 1.2, nb_points)
y = np.linspace(0, X_f1[1] * 1.2, nb_points)
X1, Y1 = np.meshgrid(x, y)
DX1, DY1 = dX_dt([X1, Y1], t, a, b, c, d)
M = np.hypot(DX1, DY1)
M[M == 0] = 1.
DX1 /= M
DY1 /= M

# Ponto de Equilíbrio
equilibrium_x = c / d
equilibrium_y = a / b
fig.add_trace(go.Scatter(x=[equilibrium_x], y=[equilibrium_y], mode='markers', name='Ponto de Equilíbrio', marker=dict(color='red', size=10)))

# Layout
fig.update_layout(
    title='Trajetórias e Campos Vetoriais com Ponto de Equilíbrio',
    xaxis_title='Número de Coelhos',
    yaxis_title='Número de Raposas',
    legend_title='Legenda',
    showlegend=True
)

st.plotly_chart(fig)
