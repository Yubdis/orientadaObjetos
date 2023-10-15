from classes import *
from dados_iniciais import *
from lista_cartoes import *


def inicializa_cartoes():
    criar_cartoes(20)
    print("ok")


def entrada():
    """Instancia um Cliente e associa a um cartão.
    Armazena o cliente em uma lista enquanto estiver consumindo.
    """
    pass


def consumo():
    pass


def encerramento():
    pass


def popular_cardapio(cardapio, lista_itens, lista_precos):
    print(lista_itens, "\n",len(lista_itens))
    print(lista_precos, "\n",len(lista_precos))
    # input()
    for ind in range(len(lista_itens)):
        cardapio.inserir_itens(lista_itens[ind], lista_precos[ind])


def inicializa_menu():
    """Esta função utiliza o arquivo itens_menu.txt para
    criar o cardápio com os itens.
    A função lê o arquivo texto, instancia um cardápio, popula o cardápio e retorna um cardápio pronto.
    """
    arquivo = open("itens_menu.txt", "r")
    lista_itens = []
    lista_precos = []

    for linha in arquivo:
        item, preco = linha.split(";")
        lista_itens.append(item)
        lista_precos.append(preco[:-1])

    arquivo.close()
    cardapio = Cardapio()
    popular_cardapio(cardapio, lista_itens, lista_precos)
    return cardapio


menu = """
=========================================
    MENU - Principal
=========================================
    0- Exit
    1- Cadastrar Cliente
    2- Realizar um Pedido
    3- Finalizar a Comanda 
    4- Gerenciar Cardapio
    """


def menu_principal():
    # cardapio = inicializa_menu()
    cardapio = Cardapio()
    popular_cardapio(cardapio, list(aux_itens.replace("\n","").split(";")), list(aux_precos.split()))
    inicializa_cartoes()

    while True:
        print("\n"*20)
        escolha = input(menu + "Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            pass
            # criar cliente
            # associar cartao pelo cliente
        elif escolha == "2":
            pass
            # adicionar pedido para cartao do cliente
        elif escolha == "3":
            pass
            # pagar/limpar: cartao do cliente, nome do cliente
        elif escolha == "4":
            # addicionar, remover items/precos do menu
            pass

# cardapio = Cardapio()
# popular_cardapio(cardapio, list(aux_itens.replace("\n","").split(";")), list(aux_precos.split()))
# cardapio.menu_itens()


if __name__ == "__main__":
    menu_principal()
