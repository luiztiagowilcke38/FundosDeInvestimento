import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class PlotSeries:
    """
    Visualizações de Séries Temporais.
    """
    @staticmethod
    def plotar_precos(df: pd.DataFrame, titulo: str = "Histórico de Preços"):
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df)
        plt.title(titulo)
        plt.xlabel("Data")
        plt.ylabel("Preço")
        plt.legend(df.columns)
        plt.grid(True)
        # plt.show() # Em ambiente não interativo, melhor salvar ou retornar fig
        return plt.gcf()

    @staticmethod
    def plotar_retornos(df: pd.DataFrame):
        plt.figure(figsize=(12, 6))
        df.plot(alpha=0.5)
        plt.title("Retornos Diários")
        plt.grid(True)
        return plt.gcf()
