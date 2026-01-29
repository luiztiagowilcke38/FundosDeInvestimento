import numpy as np

class SharpeRatio:
    """
    Índice de Sharpe.
    """
    @staticmethod
    def calcular(retorno_medio: float, vol: float, rf: float = 0.0) -> float:
        """
        (Rp - Rf) / Sigma_p
        """
        if vol == 0:
            return 0.0
        return (retorno_medio - rf) / vol
