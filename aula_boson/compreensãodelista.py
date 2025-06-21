##numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##
##aoquadrado = list(map(lambda n: n**2,numeros))
##print(aoquadrado)

##numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##
##aoquadrado = [n**2 for n in numeros]
##print(aoquadrado)

###criar uma lista de numeros pares de 0 a 10
##pares=[num for num in range(11) if num%2==0]
##print(pares)

##frase = 'A inovação do Whisper reside em sua capacidade de lidar com uma ampla gama de sotaques, idiomas e ambientes acústicos variados, tornando-o uma ferramenta poderosa para a transcrição de áudio, treinado com 680 mil horas de dados rotulados.'
##vogais = ['a','e','i','o','u']
##
##lista_vogais=[v for v in frase if v in vogais]
##print(f'A frase possui {len(lista_vogais)} vogais:')
##print(lista_vogais)

#distributiva entre 2 listas
distributiva = [k*m for k in[2,3,5] for m in [10,20,30]]
print(distributiva)
