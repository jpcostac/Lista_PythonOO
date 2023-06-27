class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def valores(self):
        print("Os pontos são {} e {}".format(self.x,self.y))

class Retangulo:
    def __init__(self, altura, comprimento):
        self.altura  = altura
        self.comprimento = comprimento

    def centro(self):
        centroa = self.altura/2
        centroc = self.comprimento /2

        print("O centro do retangulo é {} no eixo da altura e {} no eixo do comprimento".format(centroa,centroc))


