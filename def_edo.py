import numpy as np
import streamlit as st
import plotly.graph_objects as go
from scipy.integrate import odeint

# Definição das funções diferenciais do modelo (substitua dX_dt pelo seu modelo específico)
def dX_dt(X, t):
    x, y = X
    a, b, c, d = 1.0, 0.1, 0.1, 1.0  # Defina os parâmetros aqui
    dxdt = a * x - b * x * y
    dydt = c * x * y - d * y
    return [dxdt, dydt]

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

# Gráficos de trajetórias e campos vetoriais
fig = go.Figure()

# Trajetórias
values = np.linspace(0.3, 0.9, 5)
colors = [go.colors.rgb_to_rgb(f"rgba({int(c[0]*255)}, {int(c[1]*255)}, {int(c[2]*255)}, 1)") for c in plt.cm.autumn(np.linspace(0.3, 1., len(values)))[:, :3]]  # Cores para cada trajetória

for v, color in zip(values, colors):
    X0 = v * X_f1
    X = odeint(dX_dt, X0, t)
    fig.add_trace(go.Scatter(x=X[:, 0], y=X[:, 1], mode='lines', line=dict(width=3.5*v, color=color), name=f'X0=({X0[0]:.1f}, {X0[1]:.1f})'))

# Grade de pontos e campos vetoriais
x = np.linspace(0, X_f1[0] * 1.2, nb_points)
y = np.linspace(0, X_f1[1] * 1.2, nb_points)
X1, Y1 = np.meshgrid(x, y)
DX1, DY1 = dX_dt([X1, Y1])
M = np.hypot(DX1, DY1)
M[M == 0] = 1.
DX1 /= M
DY1 /= M

fig.add_trace(go.Quiver(x=X1.flatten(), y=Y1.flatten(), u=DX1.flatten(), v=DY1.flatten(), scale=0.1, color=M.flatten(), colorscale='Jet', showscale=True, name='Campo Vetorial'))

# Layout
fig.update_layout(
    title='Trajetórias e Campos Vetoriais',
    xaxis_title='Número de Coelhos',
    yaxis_title='Número de Raposas',
    legend_title='Legenda',
    showlegend=True
)

st.plotly_chart(fig)
