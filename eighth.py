class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self):
        if self.bucho >= 100:
            print("Seu macaco não está com fome")

        else:
            x = int(input("O que você gostaria de dar para o seu macaco? \n 1-)Banana \n 2-)Maça \n 3-)Outro Macaco\n"))
            if x == 1:
                self.bucho += 10

            elif x==2:
                self.bucho += 5

            elif x==3:
                self.bucho = 100

            else:
                print("Opção Inválida")

    def ver_bucho(self):
        print(self.bucho)

    def digerir(self):
        if self.bucho<=0:
            print("Seu macaco já está com fome")

        else:
            self.bucho -= 15
