#sintaxe: nome_lista = [valor1,valor2,valor3,...,valorn]
##l1 = [23,6,78]
##l2 = [20,4,74]
##valores = l1+l2
##print(f'concatenados: {valores}')
##print(len(valores))
##print(sorted(valores, reverse=True))
##print(valores)
##print(sum(valores))
##print(min(valores))
##print(max(valores))
##
##valores.append('xx')
##print(valores)
##valores.pop()
##print(valores)
##valores.pop(2)
##print(valores)
##valores.insert(2,100)
##print(valores)
##print('xx' in valores)
#=====================

##planetas=['Mercúrio','Vênus','Terra','Marte','Júpiter','Urano']
##for i in planetas:
##    print(i,end='')
#=====================

##bebidas=[]
##for i in range(5):
##    bebida = input('digite uma bebida: ')
##    bebidas.append(bebida)
##bebidas.sort()
##for j in bebidas:
##    print(j)

bebidas=[]
for i in range(5):
    # bebida = input('digite uma bebida: ')
    bebidas.append(input('digite uma bebida: '))
bebidas.sort()
for j in bebidas:
    print(j)
