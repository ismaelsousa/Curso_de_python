class objetografico(object):
    def __init__(self, cor):
        self.cor = cor

    def area(self):
        pass #a classe que herdar tem q implemntar
    
    def perimetro(self):
        pass #abstratos
    
    def info(self):
        print(f' {self.area} metros serao preenchidos  com a cor {self.cor}')


class cachorro:
    #__ significa privado
    __nome = 'rex' #variaveis de class
    cor = 'marrom' #estatico
    def __init__(self, id, raca):
        self.id = id
        self.raca = raca
    def mudaNome(self, raca):
        cachorro.nome = raca#acessando os estaticos

    #metodo estatico n tem self

    def imprimi():
        print('sou estatico')

    def __metodoPrivado():
        print('sou')
        
        
    
    
