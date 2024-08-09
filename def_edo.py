import numpy as np
import streamlit as st
import plotly.graph_objects as go

def lotka_volterra(t0, tn, x0, y0, a, b, c, d):
    """ 
    Calcula e retorna as soluções do modelo Lotka-Volterra
    """
    # Definir o intervalo de tempo e passo
    n_points = 500 * int(tn)
    t = np.linspace(t0, tn, n_points + 1)
    h = (tn - t0) / n_points

    # Inicializar as populações
    x = np.zeros(n_points + 1)
    y = np.zeros(n_points + 1)
    x[0] = x0
    y[0] = y0

    # Funções diferenciais
    f1 = lambda t, x, y: a * x - b * y * x
    f2 = lambda t, x, y: -c * y + d * y * x

    # Resolver as equações diferenciais
    for i in range(1, n_points + 1):
        x[i] = x[i-1] + h * f1(t[i-1], x[i-1], y[i-1])
        y[i] = y[i-1] + h * f2(t[i-1], x[i-1], y[i-1])

    return t, x, y

def plot_lotka_volterra(t, x, y, a, b, c, d):
    """ 
    Cria e retorna o gráfico interativo do modelo Lotka-Volterra usando Plotly
    """
    fig = go.Figure()

    # Gráfico de População de Presas vs Predadores
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Trajetória', line=dict(color='black')))
    
    # Ponto de Equilíbrio
    equilibrium_x = c / d
    equilibrium_y = a / b
    fig.add_trace(go.Scatter(x=[equilibrium_x], y=[equilibrium_y], mode='markers', name='Ponto de Equilíbrio', marker=dict(color='black', size=10)))

    # Adicionar quiver (campo vetorial)
    u = np.linspace(0, max(x), 20)
    v = np.linspace(0, max(y), 20)
    U, V = np.meshgrid(u, v)
    Ux = U * (1 - (b/a) * V) / np.sqrt((U * (1 - (b/a) * V))**2 + (V * ((d/c) * U - 1))**2)
    Vy = V * ((d/c) * U - 1) / np.sqrt((U * (1 - (b/a) * V))**2 + (V * ((d/c) * U - 1))**2)
    
    fig.add_trace(go.Scatter(x=U.flatten(), y=V.flatten(), mode='markers', marker=dict(size=5, color='grey'), name='Quiver'))

    fig.update_layout(
        title='Modelo Lotka-Volterra: População de Presas vs Predadores',
        xaxis_title='População de Presas',
        yaxis_title='População de Predadores',
        legend_title='Legenda',
        showlegend=True
    )

    return fig

# Interface Streamlit
st.title("Modelo Lotka-Volterra")

# Entrada dos parâmetros do modelo
a = st.number_input("a", value=1.0)
b = st.number_input("b", value=1.0)
c = st.number_input("c", value=1.0)
d = st.number_input("d", value=1.0)
t0 = st.number_input("Tempo inicial", value=0.0)
tn = st.number_input("Tempo final", value=30.0)
x0 = st.number_input("População inicial de Presa", value=10)
y0 = st.number_input("População inicial de Predador", value=5)

# Cálculo do modelo
t, x, y = lotka_volterra(t0, tn, x0, y0, a, b, c, d)

# Plotar o gráfico de Presa vs Predador
fig = plot_lotka_volterra(t, x, y, a, b, c, d)
st.plotly_chart(fig)

# Gráfico da evolução temporal das populações
fig_time = go.Figure()
fig_time.add_trace(go.Scatter(x=t, y=x, mode='lines', name='Presa', line=dict(color='red')))
fig_time.add_trace(go.Scatter(x=t, y=y, mode='lines', name='Predador', line=dict(color='blue')))

fig_time.update_layout(
    title='Evolução Temporal das Populações',
    xaxis_title='Tempo',
    yaxis_title='População',
    legend_title='Legenda',
    showlegend=True
)

st.plotly_chart(fig_time)
