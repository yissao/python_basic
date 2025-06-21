##com este arquivo chamando string.py, causa erro de inicialização
##Delete all newely created .py files in the directory with Python. for example random.py, end.py - that was my problem that caused the same notification window. Reason in filename conflicts.

frase = 'Vamos aprender Python hoje.'
##palavras = frase.split()
##print(palavras)
##print(palavras[2])
##
##for palavra in palavras:
##    print(palavra)
##print (frase[7:19])

##email = input('digite email: ')
##arroba = email.find('@')
##print(arroba)
##usuário=email[0:arroba]
##dominio=email[arroba+1:]
##
####print(usuário.upper)
####print(dominio.lower)
######<built-in method upper of str object at 0x01D60520>
######<built-in method lower of str object at 0x041CBE80>
##
##print(usuário.upper())
##print(dominio.lower())

frase= '   teste   de espços    demais.   '
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())
print(frase)

fruta='maçã'
print (fruta)
print (fruta.rjust(20))
print (fruta.center(20))
print (fruta.ljust(20,'0'))
print (fruta.center(20,'0'))
print (fruta.rjust(20,'0'))

print(fruta.startswith('Maç'))
print(fruta.endswith('ça'))

#DOCSTRINGS
''' TEXTO
GRANDE
'''
""" PODE SER
COM ASPAS
DUPLAS
    RESPEITA
    INDENTAÇÃO
        AAA
        AAA
    TAMBÉM PODE SER USADO COMO STRING
"""

docstring1=""" PODE SER
COM ASPAS
DUPLAS
    RESPEITA
    INDENTAÇÃO
        AAA
        AAA
    TAMBÉM PODE SER USADO COMO STRING
"""
print(docstring1)
