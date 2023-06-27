class Consumo:
    def __init__(self, modelo, consumo_litros):
        self.modelo = modelo
        self.consumo_litros = consumo_litros
        self.tanque = 0
        self.odometro = 0

    def abastecer(self,litros):
        self.litros = litros
        self.tanque += litros
        trip = float(self.tanque*self.consumo_litros)
        print("Abatecimento completo, você consegue dirigir {:.2f} KMs com esse combustível.".format(trip))

    def andar(self, distancia):
        self.distancia = distancia
        combustivel_consumido = float(distancia/self.consumo_litros)
        self.tanque -= combustivel_consumido
        self.odometro += distancia

    def kilometragem(self):
        print("Seu carro tem {} KMs rodados".format(self.odometro))
