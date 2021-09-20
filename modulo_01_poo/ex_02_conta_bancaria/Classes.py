class Conta:
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


class ContaCorrente(Conta):
    def __init__(self, numero, taxa):
        super().__init__(numero)
        self.__taxa = taxa

    def cobrar_taxa(self):
        self.sacar(self.__taxa)

    @property
    def saldo(self):
        return self._Conta__saldo


class ContaPoupanca(Conta):
    def __init__(self, numero, juros):
        super().__init__(numero)
        self.__juros = juros

    @property
    def saldo(self):
        return self._Conta__saldo

    def aplicar_juros(self):
        self.depositar(self._Conta__saldo * self.__juros)
