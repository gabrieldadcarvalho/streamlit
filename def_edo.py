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


def derivative(X, t, alpha, beta, p, q):
    C, F = X
    dotx = C * (alpha - beta * C)
    doty = F * (-p + q * F)
    return np.array([dotx, doty])


Nt = 1000
tmax = 30.
t = np.linspace(0.,tmax, Nt)
res = integrate.odeint(derivative, X0, t, args = (alpha, beta, p, q))
x, y = res.T

plt.figure()
IC = np.linspace(1.0, 6.0, 21) # initial conditions for deer population (prey)
for deer in IC:
    X0 = [deer, 1.0]
    Xs = integrate.odeint(derivative, X0, t, args = (alpha, beta, p, q))
    plt.plot(Xs[:,0], Xs[:,1], "-", label = "$x_0 =$"+str(X0[0]))
plt.xlabel("Deer")
plt.ylabel("Wolves")
plt.legend()
plt.title("Deer vs Wolves");
st.plotly_chart(plt.show())
