# Escopo Global e Local

##var_global = 'Issao Yamazaki'
##
##def escreva():
##    var_local = 'Consultor Financeiro'
##    print(f'Variavel Global: {var_global}')
##    print(f'Variavel Local: {var_local}')
##
##if __name__ == '__main__':
##    print(f'executar a função escreva()')
##    escreva()
##    print(f'Variavel Global: {var_global}')
##    #print(f'Variavel Local: {var_local}') #NameError: name 'var_local' is not defined

##var_global = 'Issao Yamazaki'
##
##def escreva():
##    var_global= 'issao.pro@gmail.com' #cria outra variável. Não altera a global
##    var_local = 'Consultor Financeiro'
##    print(f'Variavel Global: {var_global}')
##    print(f'Variavel Local: {var_local}')
##
##if __name__ == '__main__':
##    print(f'executar a função escreva()')
##    escreva()
##    print(f'Variavel Global: {var_global}')
##    #print(f'Variavel Local: {var_local}') #NameError: name 'var_local' is not defined

var_global = 'Issao Yamazaki'

def escreva():
    global var_global #='issao.pro@gmail.com' #não pode atribuir na mesma linha
    var_global= 'issao.pro@gmail.com' # altera a global, mas tem q ser nesta linha
    var_local = 'Consultor Financeiro'
    print(f'Variavel Global: {var_global}')
    print(f'Variavel Local: {var_local}')

if __name__ == '__main__':
    print(f'executar a função escreva()')
    escreva()
    print(f'Variavel Global: {var_global}')
    #print(f'Variavel Local: {var_local}') #NameError: name 'var_local' is not defined
    
