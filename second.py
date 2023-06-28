class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado * self.lado
        return area

    def valor_lado(self):
        return self.lado
