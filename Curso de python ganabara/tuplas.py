#tuplas não podem mudar 
lanche = ('hamburguer','suco','pizza','pudim')
#print(lanche[-2])#de trás para a frente
#print(len(lanche))
#pode deixar sem parênteses
#print(lanche[1])

#print(lanche[1:3])
#print(lanche[:2])

#for c in lanche:
#    print(f'eu vou comer {c}')

#for comida in range(0, len(lanche)):
#    print(comida)

for pos, comida in enumerate(lanche):
    print(f'vou comer {comida} na posicao {pos}')
