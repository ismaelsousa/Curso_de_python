'''
pessoa = {'nome': 'ismael','sexo':'m','idade':22}
#print(f' o {pessoa["nome"]} tem {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

for k,v in pessoa.items():
    print(f' o {k} é {v}')

#dicionario dentro da lista
estado1 = {'uf':'rio','sigla':'rj'}
estado2 = {'uf':'sao paulo','sigla':'sp'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''

#copia de dic
estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('und federal'))
    estado['sigla'] = str(input('sigla federal'))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'o campo {k} tem valor {v}')
