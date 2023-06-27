class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornar_valores(self):
        print("Funcionário {}\nSalário R${:.2f}".format(self.nome,self.salario))

    def aumento(self,porcentagem):
        self.porcentagem = porcentagem
        novo = self.salario*(1+porcentagem)
        self.salario = novo

        print("Aumento de {} no salário, resultando no total de {:.2f}".format(porcentagem,self.salario))

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = 0
        self.perimetro = 0

    def calculo_area(self):
        x = float(self.raio * self.raio * 3.1415)
        self.area = x
        print("{:.2f}".format(self.area))

    def calculo_perimetro(self):
        y = float(2* 3.1415 * self.raio)
        self.perimetro = y
        print("{:.2f}".format(self.perimetro))

class Carro:
    def __init__(self,modelo, preco):
        self.modelo = modelo
        self.preco = preco
