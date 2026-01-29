class TreynorRatio:
    """
    Índice de Treynor.
    (Rp - Rf) / Beta
    """
    @staticmethod
    def calcular(retorno_port: float, rf: float, beta: float) -> float:
        if beta == 0:
            return 0.0
        return (retorno_port - rf) / beta
