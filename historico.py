from fila import Fila

class Historico:

    def __init__(self):
        self.trocas = Fila()

    def registrar_troca(self, figurinha1, figurinha2):

        descricao = (
            f"Troca: {figurinha1.numero} "
            f"<-> {figurinha2.numero}"
        )

        self.trocas.enqueue(descricao)

    def mostrar_historico(self):
        self.trocas.exibir()