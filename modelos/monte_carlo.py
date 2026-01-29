import pandas as pd
import numpy as np

class MonteCarloEngine:
    """
    Motor genérico para executar simulações.
    """
    def __init__(self):
        pass

    @staticmethod
    def estatisticas_finais(caminhos: pd.DataFrame) -> dict:
        """
        Calcula estatísticas sobre os valores finais dos caminhos simulados.
        """
        finais = caminhos.iloc[-1]
        return {
            'media': finais.mean(),
            'mediana': finais.median(),
            'desvio_padrao': finais.std(),
            'min': finais.min(),
            'max': finais.max(),
            'p05': finais.quantile(0.05),
            'p95': finais.quantile(0.95),
            'p01': finais.quantile(0.01),
            'p99': finais.quantile(0.99)
        }
