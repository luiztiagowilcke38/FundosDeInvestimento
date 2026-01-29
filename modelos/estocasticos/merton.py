import numpy as np
import pandas as pd

class MertonJumpDiffusion:
    """
    Modelo de Difusão com Saltos de Merton.
    Adiciona um componente de Poisson ao GBM.
    """
    def __init__(self, s0: float, mu: float, sigma: float, lambda_j: float, mu_j: float, sigma_j: float):
        self.s0 = s0
        self.mu = mu
        self.sigma = sigma
        self.lambda_j = lambda_j  # Intensidade do salto (saltos por ano)
        self.mu_j = mu_j          # Média do tamanho do salto (log)
        self.sigma_j = sigma_j    # Desvio padrão do tamanho do salto (log)

    def simular(self, T: float, dt: float, n_caminhos: int) -> pd.DataFrame:
        n_passos = int(T / dt)
        caminhos = np.zeros((n_passos + 1, n_caminhos))
        caminhos[0] = self.s0
        
        for t in range(1, n_passos + 1):
            z = np.random.standard_normal(n_caminhos)
            
            # Componente de Salto (Poisson composto)
            # Número de saltos neste intervalo (Poisson)
            n_saltos = np.random.poisson(self.lambda_j * dt, n_caminhos)
            fator_salto = np.zeros(n_caminhos)
            
            # Para simplificar vetorizado, assumimos que se n_saltos > 0, calculamos o efeito acumulado
            # Média do salto lognormal compensado: k = exp(mu_j + 0.5*sigma_j^2) - 1
            # Correção de drift para manter martingale risk-neutral não é aplicada diretamente aqui sem contexto,
            # usando a dinâmica física: dS/S = (mu - lambda*k)dt + sigma dW + (Y-1)dN
            
            # Gerando tamanho dos saltos para cada caminho
            # Simulação simples: soma de normais logarítmicas
            val_saltos = np.random.normal(self.mu_j, self.sigma_j, n_caminhos) * n_saltos
            # Se n_saltos é 0, val_saltos deve ser 0? Não, a multiplicação acima resolve se for 1 salto por vez,
            # mas poisson pode dar > 1. Aproximação para dt pequeno: max 1 salto.

            # Solução exata
            # S(t) = S(t-dt) * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z + soma(log_saltos))
            
            salto_total = np.zeros(n_caminhos)
            # Loop apenas onde houve saltos (otimização possível, mas loop for mais seguro)
            for i in range(n_caminhos):
                 if n_saltos[i] > 0:
                     salto_total[i] = np.sum(np.random.normal(self.mu_j, self.sigma_j, n_saltos[i]))

            caminhos[t] = caminhos[t-1] * np.exp((self.mu - 0.5 * self.sigma**2) * dt + \
                                                 self.sigma * np.sqrt(dt) * z + \
                                                 salto_total)
            
        return pd.DataFrame(caminhos)
