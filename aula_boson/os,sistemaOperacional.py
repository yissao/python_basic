##import os
##os.name
##os.getcwd() # get current work directory
##os.curdir
##os.listdir()
##os.listdir('c:\\')
##os.chdir('..\\')
##os.mkdir('teste')
##os.chdir('teste')
##
##pasta_nova='teste2'
##pasta_pai='..\\'
##caminho_completo=os.path.join(pasta_pai, pasta_nova)
##print(caminho_completo)
##os.mkdir(caminho_completo)
##
##os.rename('teste2', 'teste10')
##os.rmdir('teste10')
##
##os.path.basename(os.getcwd()) #retorna somente o diretorio atual sem caminho
##os.path.dirname(os.getcwd()) #retorna somente o diretorio pai sem caminho
##
##os.path.exists('c:\\users\\raziel\\documents\\projetos\\python')
##os.path.exists('c:\users\raziel\documents\projetos\python') #erro
##
##os.path.isdir('c:\\users\\raziel\\documents\\projetos\\python')
##os.path.isfile('c:\\users\\raziel\\documents\\projetos\\python\\sets1.py')
##
##manipulador = open('arq.txt','x')
##manipulador.close()
##arquivo=os.path.basename('c:\\users\\raziel\\documents\\projetos\\python\arq.txt')
##print(arquivo)
##os.path.splitext(arquivo)
##os.remove('arq.txt')

import os
os.chdir('c:\\users\\raziel\\documents\\projetos\\python\\teste')
print(f'Diretorio atual: {os.getcwd()}')

padrão_nome = input('Qual o padrão de nomes(sem extensão!')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrão_nome + ' ' + str(contador)

        nome_novo=f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)
        print(f'arquivo {arq} renomeado para {nome_novo}')
print(f'todos renomeados')

