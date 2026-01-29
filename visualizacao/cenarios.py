import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class PlotCenarios:
    """
    Visualização de simulações de Monte Carlo.
    """
    @staticmethod
    def plotar_caminhos(caminhos: pd.DataFrame, n_mostrar: int = 100):
        """
        Plota os primeiros N caminhos da simulação.
        """
        plt.figure(figsize=(12, 6))
        # Se houver muitos caminhos, plota apenas os primeiros n_mostrar
        subset = caminhos.iloc[:, :n_mostrar]
        plt.plot(subset, alpha=0.3, linewidth=1)
        
        # Média
        media = caminhos.mean(axis=1)
        plt.plot(media, color='black', linewidth=2, linestyle='--', label='Média')
        
        plt.title(f"Simulação de Monte Carlo ({caminhos.shape[1]} cenários)")
        plt.xlabel("Passos de Tempo")
        plt.ylabel("Preço")
        plt.legend()
        plt.grid(True)
        return plt.gcf()

    @staticmethod
    def plotar_distribuicao_final(caminhos: pd.DataFrame):
        finais = caminhos.iloc[-1]
        plt.figure(figsize=(10, 6))
        plt.hist(finais, bins=50, alpha=0.7, color='purple', density=True)
        plt.title("Distribuição dos Preços Finais Simulados")
        plt.grid(True)
        return plt.gcf()
