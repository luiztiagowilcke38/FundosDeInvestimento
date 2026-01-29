# Modelo Estocástico para Fundos de Investimento

Este repositório contém uma biblioteca Python modular para análise quantitativa  de fundos de investimento e ativos financeiros brasileiros. O sistema implementa modelos estocásticos, análise de séries temporais, métricas de risco sofisticadas e otimização de portfólio.

## Estrutura do Projeto

O projeto é organizado em pacotes temáticos:

*   **`dados`**: Coleta de Yahoo Finance e Banco Central (SGS), limpeza e cálculo de retornos.
*   **`modelos`**:
    *   **`estocasticos`**: GBM, Heston, Merton Jump Diffusion, Ornstein-Uhlenbeck.
    *   **`series`**: ARIMA, GARCH, Testes de Estacionariedade.
*   **`analise`**:
    *   **`risco`**: VaR (Histórico, Paramétrico, Monte Carlo), CVaR, Drawdown.
    *   **`performance`**: Sharpe, Sortino, Treynor, Jensen, Information Ratio.
*   **`otimizacao`**: Fronteira Eficiente, Black-Litterman, HRP.
*   **`visualizacao`**: Cones de volatilidade, Heatmaps, Cenários Monte Carlo, Distribuicões.

## Modelos Matemáticos Implementados

### 1. Movimento Browniano Geométrico (GBM)
Utilizado para modelar o preço de ativos que não assumem valores negativos. A equação diferencial estocástica (SDE) é dada por:

$$
\frac{dS_t}{S_t} = \mu dt + \sigma dW_t
$$

Onde:
*   $S_t$: Preço do ativo
*   $\mu$: Deriva (drift) percentual esperada
*   $\sigma$: Volatilidade percentual
*   $dW_t$: Incremento de Wiener (Movimento Browniano)

### 2. Modelo de Volatilidade Estocástica de Heston
Permite que a volatilidade varie aleatoriamente ao longo do tempo, correlacionada com o preço.

$$
dS_t = \mu S_t dt + \sqrt{\nu_t} S_t dW_t^S
$$
$$
d\nu_t = \kappa (\theta - \nu_t) dt + \xi \sqrt{\nu_t} dW_t^\nu
$$

Com correlação $d \langle W^S, W^\nu \rangle = \rho dt$.

### 3. Modelo de Difusão com Saltos de Merton
Adiciona um componente de saltos (Poisson) ao GBM para capturar eventos extremos de mercado.

$$
\frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (Y - 1)dN_t
$$

Onde $dN_t$ é um processo de Poisson com intensidade $\lambda$.

### 4. GARCH(1,1) para Séries Temporais
Modela a variância condicional $\sigma_t^2$ dependendo dos erros passados $\epsilon_{t-1}^2$ e da variância passada $\sigma_{t-1}^2$.

$$
\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2
$$

### 5. Análise de Risco: Value at Risk (VaR)
O VaR estima a perda máxima esperada para um dado nível de confiança ($1-\alpha$) em um horizonte de tempo.

$$
VaR_{\alpha} = \inf \{ l \in \mathbb{R} : P(L > l) \le 1-\alpha \}
$$

Para distribuição normal:
$$
VaR_{\alpha} = \mu - \sigma \Phi^{-1}(1-\alpha)
$$

## Como Executar

1.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

2.  Execute a análise principal:
    ```bash
    python main.py
    ```

3.  Visualize os gráficos gerados na pasta `saida/graficos`.

## Requisitos

*   Python 3.8+
*   Bibliotecas: `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `statsmodels`, `arch`, `yfinance`, `cvxpy`.

---
Desenvolvido como um framework robusto para análise quantitativa no mercado brasileiro.

**Autor:** Luiz Tiago Wilcke
