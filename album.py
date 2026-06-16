from lista_encadeada import ListaEncadeada

class Album:

    TOTAL_FIGURINHAS = 670

    def __init__(self):
        self.figurinhas = ListaEncadeada()
        self.repetidas = ListaEncadeada()

    def inserir_figurinha(self, figurinha):

        if self.figurinhas.buscar_numero(figurinha.numero):
            self.repetidas.inserir(figurinha)
        else:
            self.figurinhas.inserir(figurinha)

    def remover_figurinha(self, numero):
        return self.figurinhas.remover(numero)

    def consultar_figurinha(self, numero):
        return self.figurinhas.buscar_numero(numero)

    def exibir_album(self):
        self.figurinhas.exibir()

    def percentual_concluido(self):
        return (
            self.figurinhas.tamanho()
            / self.TOTAL_FIGURINHAS
        ) * 100

    def exibir_repetidas(self):
        self.repetidas.exibir()

    def quantidade_repetidas(self):
        return self.repetidas.tamanho()

    def buscar_jogador(self, nome):

        atual = self.figurinhas.inicio

        while atual:

            if atual.dado.jogador.lower() == nome.lower():
                return atual.dado

            atual = atual.proximo

        return None

    def buscar_selecao(self, selecao):

        atual = self.figurinhas.inicio

        while atual:

            if atual.dado.selecao.lower() == selecao.lower():
                print(atual.dado)

            atual = atual.proximo