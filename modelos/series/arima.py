import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

class AnaliseARIMA:
    """
    Modelagem ARIMA e testes de estacionariedade.
    """
    
    @staticmethod
    def teste_adf(serie: pd.Series) -> dict:
        """Teste Augmented Dickey-Fuller para estacionariedade."""
        resultado = adfuller(serie.dropna())
        return {
            'estatistica_teste': resultado[0],
            'p_valor': resultado[1],
            'lags_usados': resultado[2],
            'n_obs': resultado[3],
            'critico_1%': resultado[4]['1%'],
            'critico_5%': resultado[4]['5%'],
            'estacionaria': resultado[1] < 0.05
        }

    @staticmethod
    def ajustar_modelo(serie: pd.Series, ordem: tuple = (1, 1, 1)) -> any:
        """
        Ajusta um modelo ARIMA(p,d,q).
        """
        modelo = ARIMA(serie, order=ordem)
        resultado = modelo.fit()
        return resultado

    @staticmethod
    def auto_arima(serie: pd.Series):
        """
        Aqui poderíamos usar pmdarima se instalado, mas vamos manter statsmodels básico.
        Implementação simplificada ou placeholder para expansão futura.
        """
        # Exemplo simples de grid search poderia ser implementado aqui
        pass
