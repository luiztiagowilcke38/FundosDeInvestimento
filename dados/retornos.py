import pandas as pd
import numpy as np

class CalculadoraRetornos:
    """
    Cálculo de retornos simples, log-retornos e acumulados.
    """
    
    @staticmethod
    def calcular_retorno_simples(precos: pd.DataFrame) -> pd.DataFrame:
        """Calcula retorno simples: (P_t / P_{t-1}) - 1"""
        return precos.pct_change().dropna()

    @staticmethod
    def calcular_log_retorno(precos: pd.DataFrame) -> pd.DataFrame:
        """Calcula log-retorno: ln(P_t / P_{t-1})"""
        return np.log(precos / precos.shift(1)).dropna()

    @staticmethod
    def calcular_retorno_acumulado(retornos: pd.DataFrame, log: bool = False) -> pd.DataFrame:
        """Calcula retorno acumulado a partir de uma série de retornos."""
        if log:
            return retornos.cumsum()
        else:
            return (1 + retornos).cumprod() - 1

    @staticmethod
    def anualizar_retorno(retorno_total: float, periodos: int, freq_anual: int = 252) -> float:
        """
        Anualiza um retorno total dado o número de períodos.
        """
        return (1 + retorno_total) ** (freq_anual / periodos) - 1

    @staticmethod
    def anualizar_volatilidade(std_dev: float, freq_anual: int = 252) -> float:
        """
        Anualiza a volatilidade (desvio padrão).
        """
        return std_dev * np.sqrt(freq_anual)
