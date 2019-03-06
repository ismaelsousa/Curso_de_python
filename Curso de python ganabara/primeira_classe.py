class meu_objeto:
    def __init__(self, nome, i):
        self.nome = nome
        self.idade = i
        print('construtor')

    def imprime(self):
        print(f'ola {self.nome}')

    
class pessoa:
    def __init__(self, nome,cao, peso = 60):
        self.nome = nome
        self.peso = peso
        self.cao = cao#precisa da class

    def treinar(self):
        self.cao.daPata()
        self.cao.latir()

class cao:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def daPata(self):
        print('deu a pata')

    def latir(self):
        print(latiuu)

        
