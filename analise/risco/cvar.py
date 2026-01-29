import numpy as np
import pandas as pd

class ConditionalVaR:
    """
    Cálculo do CVaR (Expected Shortfall).
    """
    
    @staticmethod
    def cvar_historico(retornos: pd.Series, confianca: float = 0.95) -> float:
        """
        Média dos retornos abaixo do VaR.
        """
        if isinstance(retornos, pd.DataFrame):
             retornos = retornos.iloc[:, 0]
        
        limite = np.percentile(retornos, 100 * (1 - confianca))
        return retornos[retornos <= limite].mean()
