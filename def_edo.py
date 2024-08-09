import numpy as np
from scipy.integrate import odeint
import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio

# Título da aplicação
st.title("Modelo Corrupção-Fiscalização (Lotka-Volterra)")

# Entrada dos parâmetros do modelo
alpha_str = st.text_input("Alpha", value="1.0000")
try:
    alpha = float(alpha_str)
except ValueError:
    alpha = 1.0  # valor padrão ou algum tratamento de erro

Beta_str = st.text_input("Beta", value="1.0000")
try:
    beta = float(Beta_str)
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

T = st.number_input(
    "Tempo", 1, 999999, 1
) 
dt = 0.01
N = int(T/dt)

# Condições iniciais
C0 = st.number_input(
    "População inicial de corrupção (C0)", 1, 999999, 1
)  # População inicial de corrupção
F0 = st.number_input(
    "População inicial de fiscalização (F0)", 1, 999999, 1
)  # População inicial de fiscalização
X0 = [C0, F0]

C = np.zeros(N)
F = np.zeros(N)
C[0] = C0
F[0] = F0

# Exibindo os valores com a precisão desejada
st.write(f"Alpha selecionado: {alpha:.4f}")
st.write(f"Beta selecionado: {beta:.4f}")
st.write(f"P selecionado: {p:.4f}")
st.write(f"Q selecionado: {q:.4f}")
st.write(f"População inicial de corrupção (C0): {C0}")
st.write(f"População inicial de fiscalização (F0): {F0}")

for i in range(1, N):
    dC = alpha * C[i - 1] - beta * C[i - 1] * F[i - 1]
    dF = p * F[i - 1] + q * C[i - 1] * F[i - 1]
    C[i] = C[i - 1] + dC * dt
    F[i] = F[i - 1] + dF * dt


# Criação do gráfico com Plotly
fig = go.Figure()

# Adicionando a linha para C (Corruptos)
fig.add_trace(go.Scatter(
    x=np.linspace(0, T, N),
    y=C,
    mode='lines',
    name='Corruptos (C)',
    line=dict(color='blue')
))

# Adicionando a linha para F (Fiscalização)
fig.add_trace(go.Scatter(
    x=np.linspace(0, T, N),
    y=F,
    mode='lines',
    name='Fiscalização (F)',
    line=dict(color='red')
))

# Layout do gráfico
fig.update_layout(
    title='Modelo Presa-Predador (Lotka-Volterra)',
    xaxis_title='Tempo',
    yaxis_title='População',
    showlegend=True
)

# Exibir o gráfico
st.plotly_chart(fig)


"""
# Equações diferenciais do modelo corrupção-fiscalização
def lotka_volterra_corruption(X, t, alpha, beta, p, q):
    C, F = X
    dCdt = C * (alpha - beta * F)
    dFdt = F * (-p + q * C)
    return [dCdt, dFdt]


# Intervalo de tempo para a simulação
t = np.linspace(0, 200, 1000)

# Resolver as equações diferenciais
sol = odeint(lotka_volterra_corruption, X0, args=(alpha, beta, p, q))


# Criar o gráfico com Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=sol[:, 0], mode="lines", name="Corrupção (C)"))
fig.add_trace(go.Scatter(x=t, y=sol[:, 1], mode="lines", name="Fiscalização (F)"))

fig.update_layout(
    title="Modelo Corrupção-Fiscalização (Lotka-Volterra)",
    xaxis_title="Tempo",
    yaxis_title="Níveis",
    legend_title="Variáveis",
    template="plotly_white",
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)
"""
