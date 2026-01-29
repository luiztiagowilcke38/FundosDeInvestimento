"""
Projeto: Modelo Estocástico para Fundos de Investimento
Autor: Luiz Tiago Wilcke
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dados import ColetorYahoo, LimpezaDados, CalculadoraRetornos
from dados import ColetorYahoo, LimpezaDados, CalculadoraRetornos
from modelos import GBM, Heston, MonteCarloEngine, AnaliseGARCH, AnaliseARIMA
from analise.risco import ValueAtRisk, Drawdown
from analise.performance import SharpeRatio
from visualizacao import PlotSeries, PlotDistribuicoes, PlotVolatilidade, PlotCenarios

def main():
    print("=== Iniciando Análise Avançada de Fundos de Investimento ===\n")
    
    # 1. Coleta de Dados
    coletor = ColetorYahoo()
    tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', '^BVSP']
    print(f"Coletando dados para {tickers}...")
    dados = coletor.baixar_dados(tickers, "2020-01-01", "2023-12-31")
    
    if dados.empty:
        print("Falha na coleta de dados. Encerrando.")
        return

    # 2. Processamento
    retornos = CalculadoraRetornos.calcular_log_retorno(dados)
    print("Retornos calculados.\n")

    # Criar pasta de saida
    os.makedirs("saida/graficos", exist_ok=True)

    # 3. Visualização Inicial
    print("Gerando gráficos iniciais...")
    plt_precos = PlotSeries.plotar_precos(dados)
    plt_precos.savefig("saida/graficos/01_precos_historicos.png")
    
    plt_retornos = PlotSeries.plotar_retornos(retornos)
    plt_retornos.savefig("saida/graficos/02_retornos.png")
    
    plt_corr = PlotVolatilidade.heatmap_correlacao(retornos)
    plt_corr.savefig("saida/graficos/03_correlacao.png")
    plt.close('all')

    # 4. Análise de Risco (PETR4)
    ativo = 'PETR4.SA'
    ret_ativo = retornos[ativo]
    
    var_95 = ValueAtRisk.var_historico(ret_ativo, 0.95)
    print(f"VaR 95% Histórico para {ativo}: {var_95:.4f}")
    
    dd_max = Drawdown.max_drawdown(dados[ativo])
    print(f"Max Drawdown para {ativo}: {dd_max:.4f}\n")
    
    plt_cone = PlotVolatilidade.cone_volatilidade(ret_ativo)
    plt_cone.savefig(f"saida/graficos/04_cone_volatilidade_{ativo}.png")
    plt.close('all')

    # 5. Modelagem Estocástica (GBM)
    print("Executando Simulação de Monte Carlo (GBM)...")
    s0 = dados[ativo].iloc[-1]
    mu = ret_ativo.mean() * 252
    sigma = ret_ativo.std() * np.sqrt(252)
    
    gbm = GBM(s0, mu, sigma)
    caminhos = gbm.simular_caminhos(T=1.0, dt=1/252, n_caminhos=1000)
    
    plt_mc = PlotCenarios.plotar_caminhos(caminhos, n_mostrar=100)
    plt_mc.savefig("saida/graficos/05_monte_carlo_gbm.png")
    plt.close('all')

    # 6. Modelagem de Volatilidade (GARCH)
    print("Ajustando modelo GARCH(1,1)...")
    res_garch = AnaliseGARCH.ajustar_garch(ret_ativo)
    print(res_garch.summary())
    
    # 7. Distribuição
    plt_dist = PlotDistribuicoes.histograma_retornos(ret_ativo)
    plt_dist.savefig(f"saida/graficos/06_distribuicao_{ativo}.png")
    plt.close('all')

    print("\n=== Análise Concluída com Sucesso! ===")
    print("Verifique a pasta 'saida/graficos' para os resultados.")

if __name__ == "__main__":
    main()
