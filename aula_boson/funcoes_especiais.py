#funcoes lambda (anônimas)
#sintaxe:
#lambda argumentos: expressão

##quadrado = lambda x: x**2
##for i in range(10):
##    print(quadrado(i))

##par = lambda x: x%2==0
##print(par(8))

##f2c = lambda f:(f-32)*5/9
##print(f2c(212))

#--------------------------

#função map()
#sintaxe:
#map(função, iterável)

##num = [1,2,3,4,5,6,7,8]
##dobro = list(map(lambda x: x*2, num))
##print(dobro)

##palavras = ['python', 'é', 'uma', 'linguagem', 'de', 'programação']
##maiusculas = list(map(str.upper, palavras))
##print (maiusculas)
##titulo=list(map(str.title, palavras))
##print (titulo)

#função filter()
#sintaxe:
#filter(função, sequencia)

##def pares(n):
##    return n % 2 == 0
##
##numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##num_pares=list(filter(pares,numeros))
##print (num_pares)

##numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##num_impares=list(filter(lambda x: x%2!=0,numeros))
##print(num_impares)

#--------------------------

#Função reduce()
#sintaxe
#reduce(função, sequencia, valor_inicial)

##from functools import reduce
##def mult(x,y):
##    return x*y
##
##numeros = [1,2,3,4,5,6]
##total=reduce(mult,numeros)
##print(total)

#soma cumulativa dos quadrados de valores, usando expressão lambda
from functools import reduce

numeros = [1,2,3,4]
total=reduce(lambda x,y:x**2+y**2,numeros)
print(total)
