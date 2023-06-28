class Tamagushi:
    def __init__(self, nome, fome, idade, saude):
        self.nome = nome
        self.fome = fome
        self.idade = idade
        self.saude = saude
        self.humor = 100

    def mudar_nome(self, novo_nome):
        self.nome = novo_nome
        print("Agora seu Tamagushi se chama:",self.nome)

    def mudar_fome(self, nova_fome):
        self.fome = nova_fome
        print("Agora seu Tamagushi está com {} de 100 de fome".format(self.fome))

    def mudar_idade(self, nova_idade):
        self.idade = nova_idade
        print("Agora seu Tamagushi esta com {} anos".format(self.idade))

    def mudar_saude(self, nova_saude):
        self.saude = nova_saude
        print("Agora seu Tamagushi está com {} de saúde".format(self.saude))

    def definir_humor(self):
        humor = (self.saude + self.fome)/2
        self.humor = humor
        print("O Humor do seu tamagushi está em: ",humor)
        return humor