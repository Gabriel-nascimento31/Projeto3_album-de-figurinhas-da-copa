from album import Album
from historico import Historico
from figurinha import Figurinha
from gerador_figurinhas import gerar_figurinha
from persistencia import Persistencia

album = Album()
historico = Historico()

while True:

    print("\n===== ÁLBUM DA COPA =====")
    print("1 - Inserir figurinha")
    print("2 - Remover figurinha")
    print("3 - Consultar figurinha por número")
    print("4 - Buscar jogador")
    print("5 - Buscar seleção")
    print("6 - Ver álbum completo")
    print("7 - Ver repetidas")
    print("8 - Quantidade de repetidas")
    print("9 - Ver porcentagem concluída")
    print("10 - Gerar 100 figurinhas aleatórias")
    print("11 - Gerar álbum completo")
    print("12 - Salvar álbum")
    print("13 - Registrar troca")
    print("14 - Ver histórico de trocas")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        
        numero = int(input("Número da figurinha: "))
        jogador = input("Nome do jogador: ")
        selecao = input("Seleção: ")

        figurinha = Figurinha(
            numero,
            jogador,
            selecao
        )

        album.inserir_figurinha(figurinha)

        print("Figurinha adicionada!")

        
        

    elif opcao == "2":

        
        numero = int(input("Número da figurinha: "))

        if album.remover_figurinha(numero):
            print("Figurinha removida!")
        else:
            print("Figurinha não encontrada.")

        
            

    elif opcao == "3":

        
        numero = int(input("Número da figurinha: "))

        resultado = album.consultar_figurinha(numero)

        if resultado:
            print(resultado)
        else:
            print("Figurinha não encontrada.")

        
            

    elif opcao == "4":

        jogador = input("Nome do jogador: ")

        resultado = album.buscar_jogador(jogador)

        if resultado:
            print(resultado)
        else:
            print("Jogador não encontrado.")

    elif opcao == "5":

        selecao = input("Seleção: ")
        album.buscar_selecao(selecao)

    elif opcao == "6":

        print("\n===== ÁLBUM =====")
        album.exibir_album()

    elif opcao == "7":

        print("\n===== REPETIDAS =====")
        album.exibir_repetidas()

    elif opcao == "8":

        print(
            f"Quantidade de repetidas: "
            f"{album.quantidade_repetidas()}"
        )

    elif opcao == "9":

        percentual = album.percentual_concluido()

        print(
            f"Álbum concluído: "
            f"{percentual:.2f}%"
        )

    elif opcao == "10":

        for numero in range(1, 101):

            album.inserir_figurinha(
                gerar_figurinha(numero)
            )

        print("100 figurinhas geradas!")

    elif opcao == "11":

        for numero in range(1, 671):

            album.inserir_figurinha(
                gerar_figurinha(numero)
            )

        print("Álbum completo gerado!")

    elif opcao == "12":

        Persistencia.salvar(album)

        print("Dados salvos com sucesso!")

    elif opcao == "13":

        

        num1 = int(
            input("Sua figurinha repetida: ")
        )

        num2 = int(
            input("Figurinha recebida: ")
        )

        fig1 = album.consultar_figurinha(num1)
        fig2 = album.consultar_figurinha(num2)

        if fig1 and fig2:

            historico.registrar_troca(
                fig1,
                fig2
            )

            print("Troca registrada!")

        else:
            print(
                "Uma ou ambas as figurinhas "
                "não existem."
            )

        
            

    elif opcao == "14":

        print("\n===== HISTÓRICO =====")
        historico.mostrar_historico()

    elif opcao == "0":

        print("Encerrando sistema...")
        break

    else:

        print("Opção inválida!")