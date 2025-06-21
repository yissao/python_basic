x=y=z=0
x=7
y=9

z=x+y

print('A soma dos dois valores é: ',z)

x=int(input('valor de x: '))
y=int(input('valor de y: '))

print('A soma dos dois valores é: ',x+y)
print('O resto da divisão x/y é: ',x%y)
print('O resto da divisão y/x é: ',y%x)
print('\n')
print('O modulo da divisão x/y é: ',x//y)# floor division discards the fractional part
print('O modulo da divisão y/x é: ',y//x)

x=4
y=2

print('x e y agora valem: %x,%y',x,y)# corrigir, queria que substituice na string %x, %y
print('x e y agora valem: ',x,', ',y)# corrigido
print('A divisão sempre retorna float: ',x/y)
