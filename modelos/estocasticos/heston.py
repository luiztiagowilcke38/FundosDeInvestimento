import numpy as np
import pandas as pd

class Heston:
    """
    Modelo de Heston para Volatilidade Estocástica.
    dS = mu * S * dt + sqrt(V) * S * dW1
    dV = kappa * (theta - V) * dt + sigma_v * sqrt(V) * dW2
    dW1 e dW2 são correlacionados com rho.
    """
    def __init__(self, s0: float, v0: float, mu: float, kappa: float, theta: float, sigma_v: float, rho: float):
        self.s0 = s0
        self.v0 = v0
        self.mu = mu
        self.kappa = kappa
        self.theta = theta
        self.sigma_v = sigma_v
        self.rho = rho

    def simular(self, T: float, dt: float, n_caminhos: int) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Retorna (preços, volatilidades).
        """
        n_passos = int(T / dt)
        precos = np.zeros((n_passos + 1, n_caminhos))
        volatilidades = np.zeros((n_passos + 1, n_caminhos))
        
        precos[0] = self.s0
        volatilidades[0] = self.v0
        
        for t in range(1, n_passos + 1):
            # Gerando z1, z2 correlacionados
            z1 = np.random.standard_normal(n_caminhos)
            z2 = self.rho * z1 + np.sqrt(1 - self.rho**2) * np.random.standard_normal(n_caminhos)
            
            # Evolução da Volatilidade (Processo CIR para variância v) - Usando truncamento full truncation para positividade
            v_prev = volatilidades[t-1]
            v_pos = np.maximum(v_prev, 0) # Garante que raiz não seja num negativo nos passos intermerdiários
            
            # Euler-Maruyama discretization
            dv = self.kappa * (self.theta - v_pos) * dt + self.sigma_v * np.sqrt(v_pos) * np.sqrt(dt) * z2
            volatilidades[t] = np.maximum(v_prev + dv, 0) # Força positividade
            
            # Evolução do Preço
            s_prev = precos[t-1]
            ds = self.mu * s_prev * dt + np.sqrt(v_pos) * s_prev * np.sqrt(dt) * z1
            precos[t] = s_prev + ds
            
        return pd.DataFrame(precos), pd.DataFrame(volatilidades)
