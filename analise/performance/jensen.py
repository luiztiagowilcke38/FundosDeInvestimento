class JensenAlpha:
    """
    Alpha de Jensen.
    Alpha = Rp - [Rf + Beta * (Rm - Rf)]
    """
    @staticmethod
    def calcular(retorno_port: float, retorno_mercado: float, rf: float, beta: float) -> float:
        return retorno_port - (rf + beta * (retorno_mercado - rf))
