#sintaxe
##def nomefuncao ([argumentos]):
##    instrucões

##def mensagem():
##    print('Issao consultoria financeira')
##    print('outra linha')
##
##mensagem()

##def soma(a,b):
##    a=int(input('primeiro valor'))
##    b=int(input('segundo valor'))
##    print(f'soma = {a+b}')
##
##soma(1,2)


##def mult(a,b):
##    return a*b
##
##x=3
##y=5
##c=mult(x,y)
##print(c)


##def div(x,y):
##    if y !=0:
##        return x/y
##    else:
##        return 'não dá pra dividir por zero'
##
##if __name__ == '__main__':
##    
##    a=int(input('primeiro valor'))
##    b=int(input('segundo valor'))
##
##    r=div(a,b)
##    print(f'{a} dividido por {b} = {r}')

##def aoquadrado(val):
##    quadrados=[]
##    for x in val:
##        quadrados.append(x**2)
##    return quadrados
##
##if __name__ == '__main__':
##    valores=[2,3,4,5,6]
##    resultados = aoquadrado(valores)
##    print(resultados)
##    for i in resultados:
##        print(i)

def contar(num=11, caractere='='):
    for i in range(1, num+1):
        print(caractere)

if __name__ == '__main__':
    contar(caractere='&',num=3)
    contar(3,"x")
    contar(2,'A')
    a=4
    b='xx'
    contar(a,b)
    


