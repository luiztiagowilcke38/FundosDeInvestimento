import numpy as np
import pandas as pd

class GBM:
    """
    Movimento Browniano Geométrico (Geometric Brownian Motion).
    dS = mu * S * dt + sigma * S * dW
    """
    def __init__(self, s0: float, mu: float, sigma: float):
        self.s0 = s0
        self.mu = mu
        self.sigma = sigma

    def simular_caminhos(self, T: float, dt: float, n_caminhos: int) -> pd.DataFrame:
        """
        Simula N caminhos do ativo.
        
        Args:
            T (float): Tempo total em anos.
            dt (float): Passo de tempo (ex: 1/252 para diário).
            n_caminhos (int): Número de simulações.
            
        Returns:
            pd.DataFrame: DataFrame com os caminhos simulados.
        """
        n_passos = int(T / dt)
        caminhos = np.zeros((n_passos + 1, n_caminhos))
        caminhos[0] = self.s0
        
        for t in range(1, n_passos + 1):
            z = np.random.standard_normal(n_caminhos)
            # Solução exata da EDE: S(t) = S(0) * exp((mu - 0.5*sigma^2)*t + sigma*W(t))
            # Implementação incremental
            caminhos[t] = caminhos[t-1] * np.exp((self.mu - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * z)
            
        return pd.DataFrame(caminhos)
