import json

class Persistencia:

    @staticmethod
    def salvar(album):

        dados = []

        atual = album.figurinhas.inicio

        while atual:

            dados.append({
                "numero": atual.dado.numero,
                "jogador": atual.dado.jogador,
                "selecao": atual.dado.selecao
            })

            atual = atual.proximo

        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)