from arch import arch_model
import pandas as pd

class AnaliseGARCH:
    """
    Modelagem de Volatilidade Condicional (GARCH).
    """
    
    @staticmethod
    def ajustar_garch(retornos: pd.Series, p: int = 1, q: int = 1, dist: str = 'Normal') -> any:
        """
        Ajusta um modelo GARCH(p,q).
        
        Args:
            retornos (pd.Series): Série de retornos (idealmente * 100 para estabilidade numérica).
            p (int): Lag da variância (GARCH).
            q (int): Lag do erro (ARCH).
            dist (str): Distribuição ('Normal', 't', 'skewt').
        """
        # Escalar retornos é recomendável para otimização
        fator_escala = 100.0
        retornos_escalados = retornos * fator_escala
        
        modelo = arch_model(retornos_escalados, vol='Garch', p=p, q=q, dist=dist.lower())
        resultado = modelo.fit(disp='off')
        return resultado

    @staticmethod
    def prever_volatilidade(resultado_modelo, horizonte: int = 5):
        """Previsão de volatilidade futura."""
        previsao = resultado_modelo.forecast(horizon=horizonte)
        return previsao.variance.iloc[-1] # Retorna a variância prevista para os próximos passos
