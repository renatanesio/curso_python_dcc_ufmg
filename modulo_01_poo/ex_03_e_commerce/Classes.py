class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


class Livro(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.__desconto = 0.03
        self.__tipo = "Livro"

    @property
    def tipo(self):
        return self.__tipo

    @property
    def desconto(self):
        return self.__desconto


class Brinquedo(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.__desconto = 0.05
        self.__tipo = "Brinquedo"

    @property
    def desconto(self):
        return self.__desconto

    @property
    def tipo(self):
        return self.__tipo


class Eletronico(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.__desconto = 0.08
        self.__tipo = "Eletronico"

    @property
    def desconto(self):
        return self.__desconto

    @property
    def tipo(self):
        return self.__tipo


class CestaCompras:
    def __init__(self):
        self.itens = {}
        self.__valor_total_compra_desconto = 0

    def adicionar_item(self, item, qtde):
        self.itens[item] = qtde
        self.__valor_total_compra_desconto += item.valor * qtde * (1 - item.desconto)

    @property
    def valor_total_compra_desconto(self):
        return self.__valor_total_compra_desconto

    def relatorio_final(self):
        print("%.2f" % self.__valor_total_compra_desconto)
        for item, qtde in self.itens.items():
            print("%s, %s, %i, %.2f, %.2f, %.2f" % (
                item.tipo, item.nome, qtde, item.valor, item.valor * qtde, item.valor * qtde * (1 - item.desconto)))
