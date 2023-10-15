class Cardapio:
    def __init__(self):
        self.itens = list()
        self.preco = []

    def inserir_itens(self, item, preco):
        self.itens.append(item)
        self.preco.append(preco)

    def retirar_itens(self, item, preco):
        self.itens.remove(item)
        self.preco.remove(preco)

    def print_itens(self):
        print("\n" * 30)
        print("=" * 30)
        print("Cardápio: ")
        for ind, item in enumerate(self.itens):
            print(f"  {str(item).ljust(45,'.')}...{self.preco[ind]}")

    def menu_itens(self):
        print("\n" * 30)
        print("=" * 30)
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
        print(
            f"""
        Confirmando:
           - {item} - {preco} Qt: {qt_item} = {valor_pedido} """
        )
        confirmado = input("Confirma s/n: ").upper()

        if confirmado == "S":
            self.item = item
            self.quantidade = qt_item
            self.valor_pedido = valor_pedido


# Atualização da Classe Cartão
class Cartao:
    numero_atual = 100

    def __init__(self):
        # self.numero = None
        self.numero = Cartao.numero_atual
        self.itens_consumo = list()
        self.ativo = False
        Cartao.numero_atual += 1

    def get_cartao(self):
        return self.numero

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


class Convidado:
    def __init__(self, nome, telefone, cartao_cli):
        self.nome = nome
        self.telefone = telefone
        self.cartao_de_consumo = cartao_cli

    def finalizar_consumo(self):
        # clear total, deactivate card,
        liberar_cartao(cartao)

    def realizar_pedido(self):
        # add card to convidado
        cartao = Cartao
        cartao.ativar_cartao
        # add order to convidado(card)
