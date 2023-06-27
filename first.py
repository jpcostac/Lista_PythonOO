class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    #def trocaCor(self, nova_cor):
    #    self.cor = nova_cor

    #def mostraCor(self):
    #    return self.cor














class Ball:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self.circ = circ
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)


te = Ball("azul", 12, "plastico")
