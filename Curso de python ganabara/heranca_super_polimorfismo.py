class mamifero(object):
    def __init__(self, cor, patas):
        self.cor = cor
        self.patas = patas

    def falar(self):
        print('sei falar')

    def andar(self):
        print(f'eu tenho {self.patas} patas')

    def amamentar(self):
        if self.pata < 4 :
            print('tenho poucas patas')


class Pessoa(mamifero):
    def __init__(self,cor, patas, cabelo):
        super(Pessoa, self).__init__(cor, patas)
        self.cabelo = 'loiro'

    def falar(self):
        print('sou pessoa')
