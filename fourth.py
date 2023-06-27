class Conta:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self,valor):
        if  self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insulficiente para efetuar o saque")

    def exibirSaldo(self):
        print("Saldo atual: R$", self.saldo)



