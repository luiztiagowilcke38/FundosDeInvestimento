import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class PlotVolatilidade:
    """
    Visualizações de Volatilidade.
    """
    @staticmethod
    def cone_volatilidade(retornos: pd.Series):
        """
        Plota um cone de volatilidade simples (desvio padrão móvel).
        """
        # Calcular vol realizada para diferentes janelas
        janelas = [21, 63, 126, 252] # 1 mês, 3 meses, 6 meses, 1 ano
        vols = {}
        for j in janelas:
            vols[f'{j}d'] = retornos.rolling(window=j).std() * np.sqrt(252)
        
        df_vols = pd.DataFrame(vols)
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_vols)
        plt.title("Cones de Volatilidade Realizada")
        plt.ylabel("Volatilidade Anualizada")
        plt.grid(True)
        return plt.gcf()

    @staticmethod
    def heatmap_correlacao(df_retornos: pd.DataFrame):
        corr = df_retornos.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("Matriz de Correlação")
        return plt.gcf()
