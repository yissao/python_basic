def fatorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*fatorial(n-1)

if __name__ == '__main__':
    x = int(input('Digite um numero positivo: '))
    try:
        res = fatorial(x)
    except RecursionError:
        print(f'O número é grande demais ou negativo. ')
    else:
        print(f'O fatorial de {x} é {res}')
    finally:
        print('acabou')
    
            
