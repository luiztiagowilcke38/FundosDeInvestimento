from bcb import sgs
import pandas as pd
from typing import Optional

class ColetorBCB:
    """
    Classe para coleta de dados do Banco Central do Brasil (SGS).
    Foco em taxas de juros (SELIC, CDI) e índices econômicos.
    """
    
    CODIGOS_SGS = {
        'SELIC': 11,        # Taxa de juros - Selic
        'CDI': 12,          # Taxa de juros - CDI
        'IPCA': 433,        # Índice nacional de preços ao consumidor-amplo (IPCA)
        'IGPM': 189,        # IGP-M
        'DOLAR': 1          # Taxa de câmbio - Livre - Dólar (venda)
    }

    def __init__(self):
        pass

    def obter_taxa_livre_risco(self, inicio: str, fim: str, codigo: int = 11) -> pd.Series:
        """
        Obtém a taxa livre de risco (padrão SELIC diária).
        
        Args:
            inicio (str): Data início 'YYYY-MM-DD'.
            fim (str): Data fim 'YYYY-MM-DD'.
            codigo (int): Código SGS da série (11 para Selic diária).
            
        Returns:
            pd.Series: Série temporal com as taxas.
        """
        try:
            print(f"Buscando série SGS {codigo} (Taxa Livre de Risco) de {inicio} a {fim}...")
            # A biblioteca python-bcb aceita strings de data
            serie = sgs.get({f'SGS_{codigo}': codigo}, start=inicio, end=fim)
            return serie[f'SGS_{codigo}']
        except Exception as e:
            print(f"ERRO ao buscar dados do BCB: {e}")
            return pd.Series(dtype='float64')

    def obter_serie_historica(self, codigo: int, inicio: str, fim: str, nome: str = 'Serie') -> pd.DataFrame:
        """
        Busca uma série genérica do SGS.
        """
        try:
            df = sgs.get({nome: codigo}, start=inicio, end=fim)
            return df
        except Exception as e:
            print(f"ERRO ao obter série {codigo}: {e}")
            return pd.DataFrame()
