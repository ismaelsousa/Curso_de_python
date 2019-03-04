num = [1,2,34,5]
num[2] = 23
num.append(3)
num.sort(reverse = True)
num.insert(2,2)
#print(num)

#---------
if 5 in num:
    num.remove(5)
else:
    print('não achei')

#-----------------------
#print(f'estas lista tem {len(num)} elementos')
#num.pop()
#num.remove(2) #remove somente a primera ocorrencia
#print(num)

valores = list()
valores.append(4)
valores.append(3)
valores.append(3)

for c,v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}')
print('final da lista')


#passa a referencia
a = [2,3,4]
b = a
b[2] = 100

print(f'lista a: {a}')
print(f'lista a: {b}')


#copia os valores, passa do inicio ao fim
c = a[:]
