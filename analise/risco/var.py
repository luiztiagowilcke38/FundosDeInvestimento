import numpy as np
import pandas as pd
from scipy.stats import norm

class ValueAtRisk:
    """
    Cálculo de Value at Risk (VaR).
    """
    
    @staticmethod
    def var_historico(retornos: pd.Series, confianca: float = 0.95) -> float:
        """
        Calcula o VaR Histórico.
        """
        if isinstance(retornos, pd.DataFrame):
             retornos = retornos.iloc[:, 0]
        return np.percentile(retornos, 100 * (1 - confianca))

    @staticmethod
    def var_parametrico(retornos: pd.Series, confianca: float = 0.95) -> float:
        """
        Calcula o VaR Paramétrico (Normal).
        """
        mu = retornos.mean()
        sigma = retornos.std()
        return norm.ppf(1 - confianca, loc=mu, scale=sigma)

    @staticmethod
    def var_monte_carlo(simulacoes: pd.DataFrame, confianca: float = 0.95) -> float:
        """
        Calcula o VaR com base em simulações de Monte Carlo (retornos finais simulados).
        """
        # Assume que simulacoes contém os precos finais ou retornos finais
        # Se forem preços, calcula retorno em relação ao inicial
        # Aqui vamos assumir que recebemos uma série de retornos simulados
        valores_finais = simulacoes.iloc[-1]
        retornos_simulados = (valores_finais / simulacoes.iloc[0]) - 1
        return np.percentile(retornos_simulados, 100 * (1 - confianca))
