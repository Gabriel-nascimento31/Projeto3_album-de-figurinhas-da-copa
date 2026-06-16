class Figurinha:
    def __init__(self, numero, jogador, selecao):
        self.numero = numero
        self.jogador = jogador
        self.selecao = selecao

    def __str__(self):
        return f"{self.numero} - {self.jogador} ({self.selecao})"