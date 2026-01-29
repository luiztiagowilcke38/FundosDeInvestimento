import pandas as pd
import numpy as np

class LimpezaDados:
    """
    Utilitários para limpeza e pré-processamento de séries financeiras.
    """
    
    @staticmethod
    def remover_outliers_iqr(df: pd.DataFrame, coluna: str = None, fator: float = 1.5) -> pd.DataFrame:
        """
        Remove outliers usando o método do Intervalo Interquartil (IQR).
        Se coluna for None, aplica em todo o DataFrame (cuidado).
        """
        dados = df.copy()
        if coluna:
            Q1 = dados[coluna].quantile(0.25)
            Q3 = dados[coluna].quantile(0.75)
            IQR = Q3 - Q1
            filtro = (dados[coluna] >= Q1 - fator * IQR) & (dados[coluna] <= Q3 + fator * IQR)
            return dados.loc[filtro]
        else:
            # Aplica para cada coluna individualmente (pode desalinhar datas se não for cuidadoso)
            # Para séries temporais financeiras, geralmente tratamos retornos, não preços brutos dessa forma.
            for col in dados.columns:
                Q1 = dados[col].quantile(0.25)
                Q3 = dados[col].quantile(0.75)
                IQR = Q3 - Q1
                mask = (dados[col] >= Q1 - fator * IQR) & (dados[col] <= Q3 + fator * IQR)
                dados.loc[~mask, col] = np.nan # Substitui por NaN para manter alinhamento temporal
            
            return dados.dropna() # Ou ffill/bfill dependendo da estratégia

    @staticmethod
    def preencher_missing_values(df: pd.DataFrame, metodo: str = 'ffill') -> pd.DataFrame:
        """
        Preenche valores faltantes.
        metodo: 'ffill' (anterior), 'bfill' (próximo), 'linear' (interpolação).
        """
        if metodo == 'linear':
            return df.interpolate(method='linear')
        else:
            return df.fillna(method=metodo)

    @staticmethod
    def normalizar_min_max(serie: pd.Series) -> pd.Series:
        return (serie - serie.min()) / (serie.max() - serie.min())
    
    @staticmethod
    def alinhar_datas(df_lista: list[pd.DataFrame]) -> pd.DataFrame:
        """
        Recebe uma lista de DataFrames e retorna um único DataFrame com join nas datas (index).
        """
        if not df_lista:
            return pd.DataFrame()
        
        resultado = df_lista[0]
        for df in df_lista[1:]:
            resultado = resultado.join(df, how='inner')
        return resultado
