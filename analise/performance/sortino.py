import numpy as np
import pandas as pd

class SortinoRatio:
    """
    Índice de Sortino.
    Considera apenas volatilidade negativa (downside deviation).
    """
    @staticmethod
    def calcular(retornos: pd.Series, rf: float = 0.0, target: float = 0.0) -> float:
        """
        (Rp - Rf) / Downside_Deviation
        """
        # Retorno excedente médio
        retorno_medio = retornos.mean()
        
        # Desvio negativo (considerando retornos abaixo do target)
        retornos_negativos = retornos[retornos < target]
        downside_risk = np.sqrt(np.mean(retornos_negativos**2))
        
        if downside_risk == 0:
            return 0.0
            
        return (retorno_medio - rf) / downside_risk
