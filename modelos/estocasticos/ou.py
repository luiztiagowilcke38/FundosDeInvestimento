import numpy as np
import pandas as pd

class OrnsteinUhlenbeck:
    """
    Processo de Reversão à Média (Ornstein-Uhlenbeck).
    dx = theta * (mu - x) * dt + sigma * dW
    """
    def __init__(self, x0: float, mu: float, theta: float, sigma: float):
        self.x0 = x0
        self.mu = mu        # Nível de média de longo prazo
        self.theta = theta  # Velocidade de reversão
        self.sigma = sigma  # Volatilidade

    def simular(self, T: float, dt: float, n_caminhos: int) -> pd.DataFrame:
        n_passos = int(T / dt)
        caminhos = np.zeros((n_passos + 1, n_caminhos))
        caminhos[0] = self.x0
        
        for t in range(1, n_passos + 1):
            z = np.random.standard_normal(n_caminhos)
            # Discretização exata
            # x(t) = x(t-1)*exp(-theta*dt) + mu*(1-exp(-theta*dt)) + sigma*sqrt((1-exp(-2*theta*dt))/(2*theta))*Z
            
            exp_theta_dt = np.exp(-self.theta * dt)
            term_det = caminhos[t-1] * exp_theta_dt + self.mu * (1 - exp_theta_dt)
            variance = (self.sigma**2) * (1 - np.exp(-2 * self.theta * dt)) / (2 * self.theta)
            term_stoch = np.sqrt(variance) * z
            
            caminhos[t] = term_det + term_stoch
            
        return pd.DataFrame(caminhos)
