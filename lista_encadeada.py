from nodo_lista import NodoLista

class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def inserir(self, dado):
        novo = NodoLista(dado)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo

    def remover(self, numero):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.dado.numero == numero:

                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return True

            anterior = atual
            atual = atual.proximo

        return False

    def buscar_numero(self, numero):
        atual = self.inicio

        while atual:
            if atual.dado.numero == numero:
                return atual.dado

            atual = atual.proximo

        return None

    def exibir(self):
        atual = self.inicio

        while atual:
            print(atual.dado)
            atual = atual.proximo

    def tamanho(self):
        contador = 0
        atual = self.inicio

        while atual:
            contador += 1
            atual = atual.proximo

        return contador