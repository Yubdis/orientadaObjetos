class Cardapio:
    def __init__(self):
        self.itens = list()
        self.preco = []

    def inserir_itens(self, item, preco):
        self.itens.append(item)
        self.preco.append(preco)

    def print_itens(self):
        print("\n"*30)
        print("="*30)
        print("Cardápio: ")
        for ind, item in enumerate(self.itens):
            print(f"  {str(item).ljust(45,'.')}...{self.preco[ind]}")

    def menu_itens(self):
        print("\n"*30)
        print("="*30)
        print("Cardápio: ")
        for ind, item in enumerate(self.itens):
            print(f"{ind+1}- {str(item).ljust(45,'.')}...{self.preco[ind]}")

        item_escolhido = int(input(f"Escolher opção [1-{len(self.itens)}]: ")) - 1
        return self.itens[item_escolhido], self.preco[item_escolhido]


class Pedido:
    def __init__(self):
        self.item = None
        self.quantidade = 0
        self.valor_pedido = 0

    def escolher_item(self, cardapio):
        # escolha = cardapio.menu_itens()
        item, preco = cardapio.menu_itens()
        # print(escolha)
        qt_item = int(input(f"  Quantidade: "))
        valor_pedido = qt_item * float(preco)
        print(f"""
        Confirmando:
           - {item} - {preco} Qt: {qt_item} = {valor_pedido} """)
        confirmado = input("Confirma s/n: ").upper()

        if confirmado == "S":
            self.item = item  # escolha[0]
            self.quantidade = qt_item
            self.valor_pedido = valor_pedido


#
# class Cartao:
#     def __init__(self):
#         self.numero = None
#         self.itens_consumo = list()
#         self.ativo = False
#
#
#     def ativar_cartao(self):
#         pass
#
#     def desativar_cartao(self):
#         pass
#
#     def adicionar_pedido(self, pedido):
#         self.itens_consumo.append(pedido)
#
#     def conferir_itens(self):
#         print("\nConsumo:")
#         soma = 0
#         for pedido in self.itens_consumo:
#             print(f"> {pedido.item} {pedido.quantidade} {pedido.valor_pedido}")
#             soma += pedido.valor_pedido
#
#
#         print(f">>> Total: {soma}")

""" """


# Atualização da Classe Cartão
class Cartao:
    numero_atual = 100

    def __init__(self):
        # self.numero = None
        self.numero = Cartao.numero_atual
        self.itens_consumo = list()
        self.ativo = False
        Cartao.numero_atual += 1

    def is_ativo(self):
        return self.ativo

    def ativar_cartao(self):
        self.ativo = True

    def desativar_cartao(self):
        self.ativo = False

    def adicionar_pedido(self, pedido):
        self.itens_consumo.append(pedido)

    def conferir_itens(self):
        print("\nConsumo:")
        soma = 0
        for item in self.itens_consumo:
            print(f"> {item.item} {item.quantidade} {item.valor_pedido}")
            soma += item.valor_pedido

        print(f">>> Total: {soma}")

"""
Crie uma classe chamada Pessoa com os seguintes atributos:
    -nome
    -telefone

    Os atributos são privados e do tipo string.

Utilizando o menu a baixo crie uma agenda e armazene
    os objetos de Pessoa em uma lista chamada agenda.
    agenda = []

MENU
================
1- Adicionar / Excluir
2- Visualizar agenda
 Escolha:


Descrição:
Na opção 1: Ler nome
                Caso nome não exista na agenda, ler telefone, Instanciar e
                adicionar em agenda.
            Caso o nome já exista, mostre os dados. Perguntar se quer
                adicionar outro telefone, ou se quer
                excluir o nome localizado, ou excluir um número.

Na opção 2: mostrar na tela o nome e os telefones das pessoas.

"""
class Cliente:
    agenda = []

    def __int__(self):
        self.nome = ""
        self.telefone = ""



