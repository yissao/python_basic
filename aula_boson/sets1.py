##planeta_anão = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
##print(planeta_anão)
##print(len(planeta_anão))
##print('Marte' not in planeta_anão)
##
astros = ['lua', 'venus', 'venus', 'terra', 'sirius', 'lua']
print(astros)
astros_set=set(astros)
print(astros_set)

#astros2 = ['lua', 'venus', 'venus', 'terra', 'sirius', 'lua', 'halley']
#TypeError: unsupported operand type(s) for |: 'list' and 'list'

astros1 = {'lua', 'venus', 'venus', 'terra', 'sirius', 'lua','io'}
astros2 = {'lua', 'venus', 'venus', 'terra', 'sirius', 'lua', 'halley'}
print(astros1 == astros2)
print(astros1|astros2)
print(astros1.union(astros2))

print(astros1&astros2)
print(astros1.intersection(astros2))

print(astros1^astros2)
print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
#astros1.add('sol','jupiter')#TypeError: add() takes exactly one argument (2 given)
astros1.add('sol')
print(astros1)
#astros1.remove('plutao') #KeyError: 'plutao'
astros1.remove('lua')
print(astros1)
astros1.discard('plutao') #Não dá erro
astros1.discard('sol')
astros1.pop() #remove aleatoriamente, executar varias vezes para conferir
print(astros1)
astros1.clear()
print(astros1)



