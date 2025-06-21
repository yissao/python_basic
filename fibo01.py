a = 0
b = 1
c = 0

##for i in range(8):
##    #print(a)
##    print(a+b)
##    c=a+b
##    a=b
##    b=c

# for i in range(8):
#     print(a+b)
#     c=a+b
#     a=b
#     b=c

###trocar valores entre duas variáveis
##
##a=12
##b=34
##print(a,b)
##a,b=b,a
##print(a,b)

# passos=input("quantos? ")
# print(a)
# print(b)
# for i in range (int(passos)):
#     c=a+b
#     print(c)
#     a=b
#     b=c

def fibo(n):
    fibonacci =[]
    a,b=0,1
    while b<=n:
        fibonacci.append(b)
        a,b=b,a+b
    return fibonacci

limite=int(input("fibonacci: "))
print(fibo(limite))
