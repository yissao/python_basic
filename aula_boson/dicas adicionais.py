###trocar valores entre duas variáveis
##
##a=12
##b=34
##print(a,b)
##a,b=b,a
##print(a,b)

###operador condicional ternário
##a=12
##b=34
##menor=a if a<b else b
##print(f'Menor valor= {menor}')
##print(f'Menor valor= {(b,a)[a<b]}')

###Generators consome menos recurso da maquina
##valores=[1,3,5,7,9,11,13,15]
##quadrados = (item**2 for item in valores)
##print(quadrados)
##for i in quadrados:
##    print(i)

###função enumerate()
##bebidas = ['cafe','cha','suco','agua']
##for i, bebida in enumerate(bebidas):
##    print(f'Indice: {i}, bebida: {bebida}')
##
##temperaturas=[-1, 10, 5, -3, 8, 4, -2, -5, 7]
##total = 0
##for i, t in enumerate(temperaturas):
##    print(f'Indice: {i}, temperatura: {t}')
##    if t<0:
##        total +=1
##    print(total)

#Gerenciamento de contexto com with
with open('frutas.dat','r', encoding='utf-8') as a:
    for linha in a:
        print(linha.rstrip())
