##manipulador = open('Lorem Ipsum.txt','r', encoding='utf-8')
##print(f'Método read():\n')
##print(manipulador.read())

##print(f'Método readline():\n')
##print(manipulador.readline())
##print(manipulador.readline())

##print(f'Método readlines():\n')
##print(manipulador.readlines())

##try:
##    manipulador = open('Lorem Ipsum.txt','r', encoding='utf-8')
##    for linha in manipulador:
##        linha = linha.rstrip() #tira o caractere 'nova linha' no final
##        print(linha)
##except IOError:
##    print(f'Não foi possível abrir o arquivo')
##else:
##    manipulador.close()

##texto = input('qual o termo procurado? ')
##try:
##    manipulador = open('Lorem Ipsum.txt','r', encoding='utf-8')
##    for linha in manipulador:
##        linha = linha.rstrip() #tira o caractere 'nova linha' no final
##        if texto in linha:
##            print('achei')
##            print(linha)
##        else:
##            print('NÃO achei')
##except IOError:
##    print(f'Não foi possível abrir o arquivo')
##else:
##    manipulador.close()

#=======ESCREVER=========

##try:
##    manipulador = open('Lorem Ipsum.txt','w', encoding='utf-8')
##    manipulador.write('Issao, consultor\n')
##    manipulador.write('este metodo SUBSTITUI o texto no arquivo')
##    
##except IOError:
##    print(f'Não foi possível abrir o arquivo')
##else:
##    manipulador.close()

##texto = '\nTeste de adição de linha'
##try:
##    manipulador = open('Lorem Ipsum.txt','a', encoding='utf-8')
##    manipulador.write('Issao, consultor\n')
##    manipulador.write('este metodo SUBSTITUI o texto no arquivo\n')
##    manipulador.write(texto)
##except IOError:
##    print(f'Não foi possível abrir o arquivo')
##else:
##    manipulador.close()

frutas = ['morango\n','maçã\n','caju\n','amora\n', 'limão\n', 'groselha\n','tamarindo\n']
try:
    manipulador = open('frutas.dat','w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()
