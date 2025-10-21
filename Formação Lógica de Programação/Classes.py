class Heroi:
    def __init__(self, nome, idade, tipo, ataque):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ataque = ataque
    def atacar(self):
        print(f"O {self.tipo} atacou usando {self.ataque}")
heroi1 = Heroi("Eric", "20", "Mago", "usando magia")
heroi2 = Heroi("Felipe", "21", "Guerreiro", "usando espada")
herois = [heroi1, heroi2]
for heroi in herois:
    heroi.atacar()