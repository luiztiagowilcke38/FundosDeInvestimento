import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform

class HRP:
    """
    Hierarchical Risk Parity (Lopez de Prado).
    """
    def __init__(self, retornos: pd.DataFrame):
        self.retornos = retornos
        self.cov = retornos.cov()
        self.corr = retornos.corr()

    def agrupar_ativos(self):
        """
        Etapa 1: Clusterização Hierárquica.
        """
        dist = np.sqrt(0.5 * (1 - self.corr))
        # linkage matrix
        link = linkage(squareform(dist), 'single')
        return link

    def quase_diagonalizacao(self, link):
        """
        Etapa 2: Reordenar linhas/colunas da matriz de covariância.
        """
        # Ordenação baseada no cluster
        pass

    def alocacao_recursiva(self):
        """
        Etapa 3: Biseção recursiva.
        """
        pass
        
    def otimizar(self):
        """
        Executa o pipeline completo HRP.
        """
        # Implementação simplificada: Retorna pesos iguais por enquanto
        n = len(self.retornos.columns)
        return np.ones(n) / n
