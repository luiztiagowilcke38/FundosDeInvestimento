import pandas as pd
import numpy as np

class Drawdown:
    """
    Cálculo de Drawdowns.
    """
    
    @staticmethod
    def calcular_drawdown(precos: pd.Series) -> pd.Series:
        """
        Retorna a série de drawdown (em percentual negativo).
        """
        pico_acumulado = precos.cummax()
        drawdown = (precos - pico_acumulado) / pico_acumulado
        return drawdown

    @staticmethod
    def max_drawdown(precos: pd.Series) -> float:
        """
        Retorna o pior drawdown do período.
        """
        return Drawdown.calcular_drawdown(precos).min()
