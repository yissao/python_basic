#sintaxe
#print(objetos, argumentos)

##mensagem = 'função print'
##print(mensagem)
##print('teste')
##print("teste")
##
##nome='Issao Yamazaki'
##print('testes do ',nome)
##
##nome = input('digite seu nome: ')
##print('Olá '+nome+ '! Bem vindo')
##
##print('teste')
##print("teste",end='')
##print('teste',end='')
##print("teste",end='')
##print('teste',end='')
##print("teste")
##print('nova linha')

nome = 'Adriana'
idade = 51
msg_formatada = 'O nome dela é {0} e ela tem {1} anos. {0}{1}{1}'.format(nome, idade)
print(msg_formatada)
print('O nome dela é {0} e ela tem {1} anos. {0}{1}{1}'.format(nome, idade))

msgf=f'Olá, meu nome é {nome} e tenho {idade} anos.'
print(msgf)

a=10
b=5
res=f'A soma de {a} com {b} é {a+b}'
print(res)

valor=123.579637
print(f'O valor é {valor:010.2f}')
print(f'O valor é \n\t\'{valor:.2f}\'')
