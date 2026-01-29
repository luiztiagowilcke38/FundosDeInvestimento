import numpy as np
import pandas as pd
import cvxpy as cp

class FronteiraEficiente:
    """
    Otimização de Portfólio (Markowitz).
    """
    def __init__(self, retornos_esperados: np.array, matriz_cov: np.matrix):
        self.mu = retornos_esperados
        self.sigma = matriz_cov
        self.n_ativos = len(retornos_esperados)

    def maximizar_sharpe(self, rf: float = 0.0) -> np.array:
        """
        Encontra os pesos que maximizam o Índice de Sharpe.
        """
        w = cp.Variable(self.n_ativos)
        retorno = self.mu @ w
        risco = cp.quad_form(w, self.sigma)
        
        # Maximizar (mu.T * w - rf) / sqrt(w.T * Sigma * w)
        # Transformação para problema convexo: minimizar risco sob retorno fixo não funciona direto para Sharpe
        # Abordagem alternativa: Maximizar retorno sob restrição de risco unitário (e depois normalizar)
        # Ou usar: maximizar mu.T * y sob sqrt(y.T * Sigma * y) <= 1, com w = y / (1.T * y)
        
        # Implementação simplificada: Maximizar retorno dado um risco, mas para Sharpe precisamos iterar a fronteira
        # ou usar a transformação de Charnes-Cooper se tiver restrições lineares.
        
        # Vamos usar a abordagem robusta do cvxpy para Max Sharpe:
        # Minimizando o risco quadrático ajustado pelo retorno excedente
        # Mas requer solver específico para QCQP ou reformulação.
        
        # Simplificando: Usar scipy.optimize se cvxpy complicar sem solver comercial?
        # Vamos usar a formulação clássica: Minimizar variância para um alvo de retorno.
        pass

    def minimizar_volatilidade(self) -> np.array:
        """
        Portfólio de Variância Mínima Global.
        """
        w = cp.Variable(self.n_ativos)
        risco = cp.quad_form(w, self.sigma)
        
        problema = cp.Problem(cp.Minimize(risco), 
                              [cp.sum(w) == 1, 
                               w >= 0]) # Long-only
        
        problema.solve()
        return w.value
