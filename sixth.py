class Televisao:
    def __init__(self):
        self.volume = 50
        self.canal = 1

    def mudar_canal(self, novo_canal):
        if 1<=  novo_canal <= 100:
            self.canal = novo_canal
            print("Canal alterado para: ",self.canal)
        else:
            print("Canal inválido!")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido")

    def diminuir_volume(self):
        if 0 < self.volume:
            self.volume -= 1
        else:
            print("Volume mínimo atingido")


    #def __repr__(self):
        #return f"Televisao(volume={self.volume}, canal={self.canal})"