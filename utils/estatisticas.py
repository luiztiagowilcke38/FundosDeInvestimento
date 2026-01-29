import pandas as pd

class EstatisticasDescritivas:
    """
    Gera estatísticas descritivas para séries financeiras.
    """
    @staticmethod
    def gerar_resumo(df: pd.DataFrame) -> pd.DataFrame:
        resumo = df.describe()
        resumo.loc['skewness'] = df.skew()
        resumo.loc['kurtosis'] = df.kurtosis()
        return resumo
