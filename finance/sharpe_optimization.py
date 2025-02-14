import streamlit as st
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import scipy.optimize as sco
import investpy as inv
import cvxpy as cp


def get_selic_rate():
    while True:
        try:
            data = inv.get_bond_historical_data(
                bond="Brazil 1Y",
                from_date=(date.today() - timedelta(days=1)).strftime("%d/%m/%Y"),
                to_date=date.today().strftime("%d/%m/%Y"),
            )["Close"]
            return float(data.loc[data.index[0]])
        except:
            continue


def get_eua_curve():
    alphavantage = st.secrets["api_keys"]["alphavantage"]
    url = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=weekly&maturity=1year&apikey={alphavantage}"
    response = requests.get(url)
    data = response.json()
    if "data" in data:
        yield_value = data["data"][0]["value"]
        return float(yield_value)
    else:
        print("Erro ao obter os dados.")
        return None


def get_ibov():
    url = "https://br.tradingview.com/symbols/BMFBOVESPA-IBOV/components/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all(
            "tr",
            {
                "class": "row-RdUXZpkv",
                "data-rowkey": lambda x: x and x.startswith("BMFBOVESPA"),
            },
        )
        return [row["data-rowkey"][11:] + ".SA" for row in rows]
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading asset list: {e}")
        return None


def get_ibxl():
    url = "https://br.tradingview.com/symbols/BMFBOVESPA-IBXL/components/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all(
            "tr",
            {
                "class": "row-RdUXZpkv",
                "data-rowkey": lambda x: x and x.startswith("BMFBOVESPA"),
            },
        )
        return [row["data-rowkey"][11:] + ".SA" for row in rows]
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading asset list: {e}")
        return None


def get_spx():
    url = "https://br.tradingview.com/symbols/SPX/components/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all(
            "tr",
            {
                "class": "row-RdUXZpkv",
                "data-rowkey": lambda x: x
                and x.startswith("NASDAQ")
                or x
                and x.startswith("NYSE"),
            },
        )
        assets = []
        for row in rows:
            data_rowkey = row["data-rowkey"]
            if data_rowkey.startswith("NASDAQ"):
                asset_name = data_rowkey[7:]
            elif data_rowkey.startswith("NYSE"):
                asset_name = data_rowkey[5:]
            assets.append(asset_name)

        return assets
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading asset list: {e}")
        return None


def get_asset_stats(data):
    return {
        "Media": data.mean(),
        "Variancia": data.var(),
        "Desvio_Padrao": data.std(),
        "Maximo": data.max(),
        "Minimo": data.min(),
    }


def function_returns(data):
    return data.pct_change().dropna()


def returns_portfolio(ret):
    weights = np.random.random(ret.shape[1])
    weights /= np.sum(weights)
    p_ret = np.dot(weights, ret.mean())
    return p_ret, weights


def vol_portfolio(ret, weights):
    return np.sqrt(np.dot(weights.T, np.dot(ret.cov(), weights)))


def sharpe(p_ret, p_vol, risk_free_rate):
    risk_free_rate = (risk_free_rate / 100 + 1) ** (1 / 252) - 1
    return (p_ret - risk_free_rate) / p_vol


def p_risk_min(weights, returns, risk_free_rate, selected_assets):
    def fun(weights, returns):
        return vol_portfolio(returns, weights)

    restri = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    bnds = tuple((0, 1) for _ in range(len(selected_assets)))
    optim_r = sco.minimize(
        fun,
        weights,
        args=(returns,),
        method="SLSQP",
        bounds=bnds,
        constraints=restri,
    )
    rm_weights = optim_r.x
    rm_return = np.dot(rm_weights, returns.mean())
    rm_vol = fun(rm_weights, returns)
    rm_sharpe = sharpe(rm_return, rm_vol, risk_free_rate)
    return rm_weights, rm_return, rm_vol, rm_sharpe


def p_sp_max(weights, returns, risk_free_rate, selected_assets):
    def fun(weights, returns, risk_free_rate):
        s_m_r = np.dot(weights, returns.mean())
        s_m_v = np.sqrt(np.dot(weights.T, np.dot(returns.cov(), weights)))
        risk_free_rate = (risk_free_rate / 100 + 1) ** (1 / 252) - 1
        return -((s_m_r - risk_free_rate) / s_m_v)

    restri = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    bnds = tuple((0, 1) for _ in range(len(selected_assets)))
    optim_s = sco.minimize(
        fun,
        weights,
        args=(returns, risk_free_rate),
        method="SLSQP",
        bounds=bnds,
        constraints=restri,
    )
    sp_weights = optim_s.x
    sp_vol = vol_portfolio(returns, sp_weights)
    sp_ret = np.dot(sp_weights, returns.mean())
    sp_sharpe = sharpe(sp_ret, sp_vol, risk_free_rate)
    return sp_weights, sp_ret, sp_vol, sp_sharpe


def scatter_plot(
    max_sharpe_portfolio=None, min_risk_portfolio=None, t_vol=None, trets=None
):
    fig = go.Figure()
    if max_sharpe_portfolio:
        fig.add_trace(
            go.Scatter(
                x=[max_sharpe_portfolio["Vol"]],
                y=[max_sharpe_portfolio["Return"]],
                mode="markers",
                name="Máximo Sharpe",
                marker=dict(color="red", size=10, symbol="star"),
            )
        )
    if min_risk_portfolio:
        fig.add_trace(
            go.Scatter(
                x=[min_risk_portfolio["Vol"]],
                y=[min_risk_portfolio["Return"]],
                mode="markers",
                name="Mínimo Risco",
                marker=dict(color="green", size=10, symbol="star"),
            )
        )
    if t_vol is not None and trets is not None:
        fig.add_trace(
            go.Scatter(
                x=t_vol,
                y=trets,
                mode="lines",
                name="Fronteira de Eficiência",
                line=dict(color="orange", width=2),
            )
        )
    fig.update_layout(
        title="Gráfico da Fronteira de Eficiência",
        xaxis_title="Risco (Volatilidade)",
        yaxis_title="Retorno",
        showlegend=True,
        legend=dict(x=1, y=1, xanchor="left", yanchor="top", bgcolor="rgba(0,0,0,0)"),
    )
    return fig


def load_data(selected_assets, window_date):
    """Carrega dados dos ativos e retorna um DataFrame com preços ajustados."""
    data = yf.download(
        selected_assets,
        start=(date.today() - timedelta(window_date)).strftime("%Y-%m-%d"),
        end=date.today().strftime("%Y-%m-%d"),
        progress=False,
    )

    # Verificar se a coluna 'Adj Close' está presente, caso contrário usar 'Close'
    if "Adj Close" in data.columns:
        data = data["Adj Close"]
    else:
        data = data["Close"]

    # Imprimir as primeiras linhas do DataFrame para verificar as colunas
    st.write(data.head())

    return data


def calculate_statistics(data):
    """Calcula e retorna as estatísticas dos ativos."""
    # Aqui você deve implementar sua função get_asset_stats
    return pd.DataFrame({asset: get_asset_stats(data[asset]) for asset in data.columns})


def optimize_portfolio(returns, rate, selected_assets):
    """Otimiza a carteira para maximizar o Sharpe ratio e minimizar o risco."""
    init_weights = np.ones(len(selected_assets)) / len(selected_assets)

    max_sharpe_weights, max_sharpe_ret, max_sharpe_vol, max_sharpe_ratio = p_sp_max(
        init_weights, returns, rate, selected_assets
    )
    max_sharpe_portfolio = {
        "Weights": max_sharpe_weights,
        "Return": max_sharpe_ret,
        "Vol": max_sharpe_vol,
        "Sharpe": max_sharpe_ratio,
    }

    min_risk_weights, min_risk_ret, min_risk_vol, min_risk_ratio = p_risk_min(
        init_weights, returns, rate, selected_assets
    )
    min_risk_portfolio = {
        "Weights": min_risk_weights,
        "Return": min_risk_ret,
        "Vol": min_risk_vol,
        "Sharpe": min_risk_ratio,
    }

    return max_sharpe_portfolio, min_risk_portfolio


def compute_volatility_curve(returns, selected_assets):
    """Calcula a volatilidade para diferentes retornos esperados."""
    trets = np.linspace(returns.mean().min(), returns.mean().max(), 100)
    tvols = []

    for t in trets:
        weights = cp.Variable(len(selected_assets))
        objective = cp.Minimize(cp.quad_form(weights, returns.cov()))
        constraints = [
            cp.sum(weights) == 1,
            cp.matmul(returns.mean().T, weights) == t,
            weights >= 0,
        ]
        problem = cp.Problem(objective, constraints)
        try:
            result = problem.solve(solver=cp.SCS, verbose=True)
            if result is not None:
                tvols.append(np.sqrt(result))
            else:
                tvols.append(np.nan)
        except cp.error.SolverError as e:
            st.error(f"SolverError: {e}")
            tvols.append(np.nan)

    return trets, tvols


def display_results(
    max_sharpe_portfolio, min_risk_portfolio, tvols, trets, selected_assets
):
    """Exibe os resultados das carteiras e a análise de volatilidade."""
    st.title("Análise de Carteiras")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Carteira Com o Menor Risco")
        subcol1, subcol2 = st.columns([1, 1.5])
        df_p_rm = pd.DataFrame(
            min_risk_portfolio["Weights"], index=selected_assets, columns=["Pesos"]
        )
        df_p_rm = df_p_rm[df_p_rm["Pesos"] >= 0.0001]
        df_e_rm = pd.DataFrame(
            [
                min_risk_portfolio["Vol"],
                min_risk_portfolio["Return"],
                min_risk_portfolio["Sharpe"],
            ],
            columns=[""],
            index=["Risco", "Retorno", "Sharpe"],
        )
        df_p_rm.index = df_p_rm.index.str.replace(".SA", "")
        with subcol1:
            st.dataframe(df_p_rm, width=700)
        with subcol2:
            st.dataframe(df_e_rm)

    with col2:
        st.subheader("Carteira Com o Maior Sharpe")
        subcol3, subcol4 = st.columns([1, 1.5])
        df_p_sp = pd.DataFrame(
            max_sharpe_portfolio["Weights"], index=selected_assets, columns=["Pesos"]
        )
        df_p_sp = df_p_sp[df_p_sp["Pesos"] >= 0.0001]
        df_e_sp = pd.DataFrame(
            [
                max_sharpe_portfolio["Vol"],
                max_sharpe_portfolio["Return"],
                max_sharpe_portfolio["Sharpe"],
            ],
            columns=[""],
            index=["Risco", "Retorno", "Sharpe"],
        )
        df_p_sp.index = df_p_sp.index.str.replace(".SA", "")
        with subcol3:
            st.dataframe(df_p_sp, width=700)
        with subcol4:
            st.dataframe(df_e_sp)

    fig = scatter_plot(
        max_sharpe_portfolio=max_sharpe_portfolio,
        min_risk_portfolio=min_risk_portfolio,
        t_vol=tvols,
        trets=trets,
    )
    st.plotly_chart(fig)


def sharpe_optimization():
    st.title("Calculadora de Maior Sharpe e Menor Risco")
    st.markdown(
        "Bem-vindo à calculadora de maior Sharpe e menor risco. O objetivo desta ferramenta é ajudá-lo a encontrar as melhores alocações de investimento com base no **maior índice de Sharpe** e no **menor risco**."
    )
    st.write("**Como Funciona:**")
    st.markdown(
        "1. **Seleção de Indices:** Escolha do índice para análise. Serão calculados os pesos de todos os ativos para criar duas carteiras: uma que maximize o índice de Sharpe e outra que minimize o risco.\
        \n2. **Escolha da Janela de Datas:** Seleção do tamanho da janela desejada para a análise dos ativos.\
        \n3. **Taxa Livre de Risco:** Ao selecionar um índice brasileiro, a taxa livre de risco será automaticamente configurada como a taxa SELIC, calculada com base em uma curva de 252 dias. Caso o índice escolhido seja dos Estados Unidos, a taxa livre de risco será ajustada para refletir o rendimento do Título de 1 ano dos EUA.\
        \n4. **Resultado:** Após inserir todas as informações necessárias, a calculadora fornecerá a alocação para a carteira com o **maior índice de Sharpe** e outra para **minimizar o risco**, considerando o período da janela especificada e a taxa livre de risco."
    )

    selected_assets = st.radio(
        "Selecione o índice de ativos a ser analisados:",
        ("IBOVESPA", "IBXL", "S&P 500"),
        format_func=lambda x: (
            "IBOVESPA" if x == "IBOVESPA" else "IBXL" if x == "IBXL" else "S&P 500"
        ),
    )

    window_date = st.slider("**Escolha o tamanho da janela de data:**", 0, 18250, 0)
    if window_date == 0:
        st.warning("Selecione um tamanho de janela de data.")
        return

    if selected_assets == "IBOVESPA":
        selected_assets = get_ibov()
        rate = get_selic_rate()
        st.success(
            f'**Taxa de Juros na curva 252 ({date.today().strftime("%d/%m/%Y")}): {rate}% a.a**'
        )
        if selected_assets is None:
            st.error("Falha ao carregar lista do IBOVESPA.")
            return
    elif selected_assets == "S&P 500":
        selected_assets = get_spx()
        rate = get_eua_curve()
        selected_assets = list(map(lambda x: x.replace(".", "-"), selected_assets))
        st.success(
            f'**Rendimento do Título de 1 ano dos EUA em ({date.today().strftime("%d/%m/%Y")}): {rate}% a.a**'
        )
        if selected_assets is None:
            st.error("Falha ao carregar lista do S&P 500.")
            return
    elif selected_assets == "IBXL":
        selected_assets = get_ibxl()
        rate = get_selic_rate()
        if selected_assets is None:
            st.error("Falha ao carregar lista do IBXL.")
            return
        st.success(
            f'**Taxa de Juros na curva 252 ({date.today().strftime("%d/%m/%Y")}): {rate}% a.a**'
        )
    if not selected_assets:
        st.warning("Nenhum índice selecionado.")
        return

    data = load_data(selected_assets, window_date)
    st.subheader("Últimos 5 dias de preços de cada ativo:")
    asset_stats = calculate_statistics(data)
    data.columns = data.columns.str.replace(".SA", "")
    st.dataframe(data.tail())
    st.subheader("Estatísticas de cada ativo:")
    asset_stats.columns = asset_stats.columns.str.replace(".SA", "")
    st.dataframe(asset_stats)

    returns = function_returns(data)

    max_sharpe_portfolio, min_risk_portfolio = optimize_portfolio(
        returns, rate, selected_assets
    )
    trets, tvols = compute_volatility_curve(returns, selected_assets)

    display_results(
        max_sharpe_portfolio, min_risk_portfolio, tvols, trets, selected_assets
    )
