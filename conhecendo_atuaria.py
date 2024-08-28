import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def oq_atuariais():
    st.title("O que é Ciências Atuariais?")
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("pictures/hourglass.png", width=100)
    with col2:
        st.markdown(
            "Ciências Atuariais é um campo que aplica métodos matemáticos, estatísticos e financeiros para avaliar e gerenciar **riscos**, especialmente em setores como seguros, previdência, saúde e finanças. Atuários, os profissionais dessa área, desempenham um papel essencial na estimativa e controle de incertezas financeiras, garantindo a viabilidade de planos e estratégias de longo prazo."
        )
    st.subheader("Matérias Estudadas:")
    st.markdown(
        "1. **Matemática Financeira**: Conceitos de valor presente, taxas de juros, amortização, entre outros.\n"
        "2. **Economia**: Fundamentos de macro e microeconomia, além de teorias econômicas básicas.\n"
        "3. **Probabilidade e Estatística**: Modelagem de eventos aleatórios, distribuições de probabilidades, e inferência estatística.\n"
        "4. **Teoria do Risco**: Análise de eventos incertos, modelagem de perdas e avaliação de riscos.\n"
        "5. **Matemática Atuarial**: Cálculo de prêmios, reservas técnicas, e avaliação de seguros de vida e não-vida.\n"
        "6. **Modelos de Sobrevivência**: Estudo de tempos de vida, tabelas de mortalidade, e cálculos atuariais para pensões e seguros de vida.\n"
        "7. **Gestão de Investimentos**: Avaliação de portfólios, aplicação da teoria moderna de finanças.\n"
        "8. **Contabilidade e Finanças**: Análise financeira e contabilidade aplicadas ao setor de seguros.\n"
        "9. **Legislação e Regulação**: Leis e normas que regem as atividades seguradoras e previdenciárias.\n"
        "10. **Programação**: Desenvolvimento de algoritmos para análise de dados e modelos atuariais."
    )

    st.subheader("Áreas de Atuação:")

    st.markdown(
        "1. **Seguros**: Desenvolvimento e precificação de produtos como seguros de vida, saúde, automóvel, entre outros.\n"
        "2. **Previdência**: Cálculo de contribuições e benefícios para planos de aposentadoria e pensões.\n"
        "3. **Consultoria Atuarial**: Assessoria a empresas na gestão de riscos, planejamento previdenciário e auditoria atuarial.\n"
        "4. **Gestão de Riscos**: Identificação, avaliação e mitigação de riscos financeiros em empresas e instituições financeiras.\n"
        "5. **Recursos Humanos**: Desenvolvimento de benefícios corporativos, incluindo planos de pensão e seguros de saúde.\n"
        "6. **Mercado Financeiro**: Análise de produtos financeiros, derivativos, avaliação de risco de crédito e criação de modelos quantitativos.\n"
        "7. **Saúde**: Planejamento de seguros de saúde, análise de custos e riscos relacionados à área da saúde.\n"
        "8. **Governança Corporativa**: Análise e gestão de riscos corporativos, além de garantir conformidade regulatória."
    )

    st.title("Para saber mais:")

    st.markdown(
        "Acesse o plano de ensino de Ciências Atuariais da UFPE para obter informações detalhadas sobre o curso."
    )
    st.link_button(
        "Plano Pedagógico",
        "https://www.ufpe.br/documents/39362/0/PPC+Ci%C3%AAncias+Atuariais+2019.pdf/76e18139-00af-438b-8eb4-b571220384d7",
    )


def roll_dice():
    st.title("Simulador de Lançamentos de Dados")
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("pictures/dice.png", width=100)
    with col2:
        st.markdown(
            "A simulação é uma ferramenta essencial na Ciência Atuarial, permitindo a análise de diversos cenários que podem ocorrer em um contexto específico. "
            "Esta página oferece uma maneira simples de simular múltiplos lançamentos de um dado justo de **6** lados, possibilitando a observação de padrões estatísticos."
        )

    num_rolls = st.number_input("Quantos lançamentos deseja simular?", 1, 100000)
    if st.button("Lançar"):
        roll = np.random.randint(1, 7, size=int(num_rolls))
        mean = np.mean(roll)
        var = np.var(roll)
        dp = np.std(roll)

        # Criando um DataFrame com as métricas como índice
        df_metrics = pd.DataFrame(
            {"Valor": [mean, var, dp]}, index=["Média", "Variância", "Desvio Padrão"]
        )

        st.subheader(f"Resultados da Simulação com {num_rolls} Lançamentos:")
        st.dataframe(df_metrics)

        # Contando a frequência dos valores
        value_counts = pd.Series(roll).value_counts().sort_index()

        # Criando um DataFrame com o lado do dado como índice
        df_counts = pd.DataFrame(
            {"Frequência": value_counts.values}, index=value_counts.index
        )

        df_counts.index.name = "Lado do Dado"

        st.subheader("Frequência de Cada Lado do Dado:")
        st.dataframe(df_counts)

        # Criando o gráfico dos lançamentos
        st.subheader("Gráfico dos Lançamentos:")
        fig, ax = plt.subplots()
        sns.barplot(
            x=df_counts.index,
            y="Frequência",
            data=df_counts.reset_index(),
            color="green",
            ax=ax,
        )
        ax.set_xlabel("Lado do Dado")
        ax.set_ylabel("Frequência")
        ax.set_title("Distribuição dos Lançamentos dos Dados")
        st.pyplot(fig)


def social_links():
    st.sidebar.title("Redes sociais")

    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.link_button(
            "UFPE", "https://www.ufpe.br/ciencias-atuariais-bacharelado-ccsa"
        )
    with col2:
        st.sidebar.link_button(
            "Instagram - Cordenação", "https://www.instagram.com/atuariaisufpe/"
        )
        st.sidebar.link_button(
            "Instagram - Diretorio Acadêmico", "https://www.instagram.com/dacat.ufpe/"
        )


def main():
    # st.sidebar.image("pictures/", width=200)
    opcoes = st.sidebar.radio(
        "Selecione uma página",
        ("O que é Ciências Atuarias?", "Simulador de Dado"),
        format_func=lambda x: (
            "O que é Ciências Atuarias?"
            if x == "O que é Ciências Atuarias?"
            else "Simulador de Dado"
        ),
    )
    if opcoes == "Simulador de Dado":
        roll_dice()
    elif opcoes == "O que é Ciências Atuarias?":
        oq_atuariais()
    social_links()


if __name__ == "__main__":
    main()
