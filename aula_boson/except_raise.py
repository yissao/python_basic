##from math import sqrt
##
##if __name__=='__main__':
##    try:
##        num=int(input('digite um número positivo: '))
##        if num<0:
##            raise ArithmeticError
##    except ArithmeticError:
##        print(f'Foi forncido um número negativo.')
##
##    else:
##        print(f'a raiz quadrada de {num} é {sqrt(num)}')
##
##    finally:
##        print(f'fim')
#-----------------------

from math import sqrt

class NumeroNegativoIssaoError(Exception):
    def __init__(self):
        pass #não faz nada, pass adiante
    
if __name__=='__main__':
    try:
        num=int(input('digite um número positivo: '))
        if num<0:
            raise NumeroNegativoIssaoError
    except NumeroNegativoIssaoError:
        print(f'Foi fornecido um número negativo.')

    else:
        print(f'a raiz quadrada de {num} é {sqrt(num)}')

    finally:
        print(f'fim')
#-----------------------
