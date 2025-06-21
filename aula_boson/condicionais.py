#simples, composto, aninhado/encadeado

# media,n1,n2=0.0TypeError: cannot unpack non-iterable float object
media=n1=n2=0.0
n1=float(input('digite a primeira nota: '))
n2=float(input('digite a segunda nota: '))

media=(n1+n2)/2
if (media>=7):
    print('aprovado')
    print('ok')
print('sua média é {}'.format(media),'\n')
#-------------
if (media>=7):
    print('aprovado')
    print('ok')
else:
    print('reprovado')
print('sua média é {}'.format(media),'\n')
#-------------
if (media>=7):
    print('aprovado')
    print('ok')
elif (media>=5):
    print('recuperação')
    print('good luck')
else:
    print('reprovado')
    
print('sua média é {}'.format(media),'\n')

#proxima aula: 01:52:17
#https://youtu.be/-VeVq64Fgw0?t=6732
#https://www.youtube.com/watch?v=-VeVq64Fgw0
