##n1 = int(input('Digite um número: '))
##n2 = int(input('Digite outro: '))
##
##try:
##    r=round(n1/n2,2)
##
##except ZeroDivisionError:
##    print(f'não é possível dividir por zero')
##else:
##    print(f'Resultado: {r}')
##
##print('continuando>>>')

#-----------------------
def div(k,j):
    return round(k/j,2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro: '))
            break
        except ValueError:
            print(f'Erro ao ler o valor. Tente novamente. ')
    try:
        r=div(n1, n2)
    except ZeroDivisionError:
        print(f'não é possível dividir por zero')
    except:
        print('erro não previsto')
    else:
        print(f'Resultado: {r}')
    finally:
        print('acabou...')
