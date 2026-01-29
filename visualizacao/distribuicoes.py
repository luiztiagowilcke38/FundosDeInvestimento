import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

class PlotDistribuicoes:
    """
    Visualizações de Distribuições Estatísticas.
    """
    @staticmethod
    def histograma_retornos(serie: pd.Series, bins: int = 50):
        plt.figure(figsize=(10, 6))
        sns.histplot(serie, bins=bins, kde=True, stat="density", color='blue')
        
        # Plotar Normal teórica
        mu, std = stats.norm.fit(serie)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2, label='Normal Teórica')
        
        plt.title(f"Distribuição de Retornos (Mu={mu:.4f}, Sigma={std:.4f})")
        plt.legend()
        plt.grid(True)
        return plt.gcf()

    @staticmethod
    def qq_plot(serie: pd.Series):
        plt.figure(figsize=(8, 8))
        stats.probplot(serie, dist="norm", plot=plt)
        plt.title("QQ Plot vs Normal")
        plt.grid(True)
        return plt.gcf()
