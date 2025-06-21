elemento = {
    'Z':3,
    'nome':'Lítio',
    'grupo':'Metais Alcalinos',
    'densidade':0.534
    #'densidade':0,534 #erro sintaxe separador de decimal é ponto.
}

# print(f'Elemento: {elemento['nome']}' ) #erro sintaxe confundo se fica tudo com aspas simples
# print(f'Elemento: '{elemento['nome']}' ) #erro sintaxe, dentro da fstring fica o valor com chave
print(f'Elemento: {elemento["nome"]}' )
print(f'Tamanho do dicionário: {len(elemento)} elementos.')

#atualizar uma entrada
elemento['grupo']='Alacalinos'
print(elemento)

#adicionar uma entrada
#    elemento[período]=1 #NameError: name 'período' is not defined
elemento['período']=1
print(elemento)

#exclusão de itens
##del elemento['período']
##print(elemento)
##elemento.clear()
##print(elemento)
##del elemento
# print(elemento)#NameError: name 'elemento' is not defined
# porque foi apagado o dicionario

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)


print(elemento.values())
for i in elemento.values():
    print(i)

for i,j in elemento.items():
    print(f'{i}: {j}')

