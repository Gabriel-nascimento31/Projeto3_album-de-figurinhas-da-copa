from nodo_fila import NodoFila

class Fila:

    def __init__(self):
        self.frente = None
        self.fim = None

    def enqueue(self, dado):
        novo = NodoFila(dado)

        if self.fim is None:
            self.frente = novo
            self.fim = novo
            return

        self.fim.proximo = novo
        self.fim = novo

    def dequeue(self):

        if self.frente is None:
            return None

        removido = self.frente.dado
        self.frente = self.frente.proximo

        if self.frente is None:
            self.fim = None

        return removido

    def vazia(self):
        return self.frente is None

    def exibir(self):
        atual = self.frente

        while atual:
            print(atual.dado)
            atual = atual.proximo