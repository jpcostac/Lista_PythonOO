class Bomba:
    def __init__(self, tipo, valor_litro, quantidade):
        self.tipo= tipo
        self.valor_litro= valor_litro
        self.quantidade= quantidade
        self.recebimentos_posto = 0
        self.total_abastecimentos = 0

    def abastecimento_Valor(self, valor_Cliente):
        self.valor_Cliente= valor_Cliente

        x= float(valor_Cliente/self.valor_litro)
        self.quantidade -= x
        print("Cliente abasteceu {} reais com um total de {:.2f} litros".format(valor_Cliente, x))
        self.recebimentos_posto += valor_Cliente
        self.total_abastecimentos +=1

    def abastecimento_Litro(self, valor_Cliente_Litros):
        self.valor_Cliente_Litros= valor_Cliente_Litros

        self.quantidade -= valor_Cliente_Litros
        preco = self.valor_litro*valor_Cliente_Litros

        print("O cliente solicitou abastecimento de {:.2f} litros e o valor final ficou em {:.2f} reais".format(valor_Cliente_Litros,preco))
        self.recebimentos_posto += preco
        self.total_abastecimentos += 1

    def alterar_Valor_litro(self,valor_litro):
        self.valor_litro = valor_litro
        print("Valor do litro de combustívl altrado para ",valor_litro)

    def alterara_Combustivel(self, tipo):
        self.tipo = tipo
        print("Combustível alterado para ",tipo)

    def operacoes (self):
        print("Resumo das operações: \nTotal de abastecimentos: {}\nTotal de dinheiro no caixa: R${:.2f}".format(self.total_abastecimentos,self.recebimentos_posto))
