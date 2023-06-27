class Investimento:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.taxa_de_juros = 0.1

    def alterar_juros(self,taxa_de_juros):
        self.taxa_de_juros = taxa_de_juros
        print("Taxa de juros alterada para:",taxa_de_juros)

    def adicionar_juros(self):
        taxa = 1 + self.taxa_de_juros
        montante = taxa * self.valor_inicial
        self.valor_inicial = montante
        print("Montante no valor de",montante)

    def imprimir(self):
        print("Seu saldo é:",self.valor_inicial)