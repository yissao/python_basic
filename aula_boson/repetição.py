#while 
##num=0
##while(num<=10):
##    print(num)
##    num+=1
##print(f'fim {num}')

##nome=None
##while(1): #só encerra quando achar um break
##    print('nome ou x para parar: ')
##    nome = input()
##    if nome == 'x' or nome == 'X':
##        break
##    print(f'Bem-vindo, {nome}')
##print('fim')
#-----------------------

#Sintaxe
#for item in sequencia:
    #instruções
    #executadas para
    #cada item da sequencia

##lista = [1,2,3,4,5,6,7,8,9,10]
##for item in lista:
##    print(item)
##
##palavra = 'executada'
##for item in palavra:
##    print(item)
##
##for numero in range(1,11):
##    print(numero)
##
##for numero in range(10):
##    print(numero,end='')
##    print(' issao')
##
##for numero in range(10,0,-2):
##    print(numero,end='')
##    print(' issao')
#-----------------------

pedras = ('rubi','quartzo','diamante','esmeralda','safira','turmalina')
for pedra in pedras:
    if pedra == 'quartzo':
        continue #pula execução do laço mas não sai que nem o break
    print(pedra)

# https://youtu.be/-VeVq64Fgw0?t=9582
# 2:39:42
