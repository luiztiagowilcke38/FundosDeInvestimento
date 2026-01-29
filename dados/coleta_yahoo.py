import yfinance as yf
import pandas as pd
from typing import List, Union, Optional

class ColetorYahoo:
    """
    Classe responsável por coletar dados financeiros do Yahoo Finance.
    """
    def __init__(self):
        pass

    def baixar_dados(self, tickers: List[str], inicio: str, fim: str, intervalo: str = "1d") -> pd.DataFrame:
        """
        Baixa dados históricos ajustados de fechamento para uma lista de tickers.

        Args:
            tickers (List[str]): Lista de símbolos dos ativos (ex: ['PETR4.SA', 'VALE3.SA']).
            inicio (str): Data de início no formato 'YYYY-MM-DD'.
            fim (str): Data de fim no formato 'YYYY-MM-DD'.
            intervalo (str): Intervalo dos dados (ex: '1d', '1wk', '1mo').

        Returns:
            pd.DataFrame: DataFrame contendo os preços ajustados de fechamento.
        """
        print(f"Baixando dados para: {tickers} de {inicio} a {fim}...")
        try:
            dados_brutos = yf.download(tickers, start=inicio, end=fim, interval=intervalo, progress=False)
            
            if dados_brutos.empty:
                print("ERRO: Nenhum dado retornado. Verifique os tickers e as datas.")
                return pd.DataFrame()

            # Tenta acessar Adj Close, se não, tenta Close, se não, erro
            if 'Adj Close' in dados_brutos:
                dados = dados_brutos['Adj Close']
            elif 'Close' in dados_brutos:
                print("AVISO: 'Adj Close' não encontrado. Usando 'Close'.")
                dados = dados_brutos['Close']
            else:
                 print(f"ERRO: Colunas esperadas não encontradas. Colunas disponíveis: {dados_brutos.columns}")
                 return pd.DataFrame()
            
            # Se for apenas um ticker, o yfinance pode retornar Series
            if isinstance(dados, pd.Series):
                dados = dados.to_frame()
                dados.columns = tickers if len(tickers) == 1 else ['Preco']
            
            return dados
        except Exception as e:
            print(f"ERRO ao baixar dados do Yahoo Finance: {e}")
            return pd.DataFrame()

    def baixar_ativo_detalhado(self, ticker: str, inicio: str, fim: str) -> pd.DataFrame:
        """
        Baixa todos os dados OHLCV para um único ativo.
        """
        try:
            return yf.download(ticker, start=inicio, end=fim, progress=False)
        except Exception as e:
            print(f"ERRO ao baixar detalhes para {ticker}: {e}")
            return pd.DataFrame()
