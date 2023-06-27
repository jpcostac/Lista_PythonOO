class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

        self.CalcularArea()
        self.CalcularPerimetro()

    def CalcularArea(self):
        self.area = self.ladoB * self.ladoA

    def CalcularPerimetro(self):
        self.perimetro = 2 * self.ladoA + 2 * self.ladoB

    def exibir_resultados(self):
        print("O valor da Área do reamgulo é {} e do perímetro é {}".format(self.area, self.perimetro))

ladoA = int(input("Digite o valor do lado A: "))
ladoB = int(input("Digite o valor do lado B: "))

meu_Retangulo = Retangulo(ladoA, ladoB)
meu_Retangulo.exibir_resultados()
