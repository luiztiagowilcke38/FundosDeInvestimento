import pandas as pd

class InformationRatio:
    """
    Information Ratio.
    (Rp - Rb) / Tracking Error
    """
    @staticmethod
    def calcular(retornos_port: pd.Series, retornos_bench: pd.Series) -> float:
        diferenca = retornos_port - retornos_bench
        retorno_ativo = diferenca.mean()
        tracking_error = diferenca.std()
        
        if tracking_error == 0:
            return 0.0
            
        return retorno_ativo / tracking_error
