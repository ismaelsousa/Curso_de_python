'''
#aqui coloca uma lista dentro da outra
teste = list()
teste.append('gustavo')
teste.append(30)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

'''

galera = [['joao',19],['ana',20]]
for pessoa in galera:
    print(pessoa)
