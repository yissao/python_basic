import random
##valor= random.randint(1,2)
##print(valor)
##
##for i in range(5):
##    print(random.randint(1,20))
##    
##for i in range(5):
##    print(random.random())
##
##for i in range(5):
##    print(random.random()*10)
##
##for i in range(5):
##    print(round(random.random()*10,2))
##
##for i in range(5):
##    print(random.uniform(2,5))

lista=['fulano','beltrano','ciclano','jon_doe','jane_doe','zé_ninguém']
nlista=[1,2,3,4,5,6,7]
#print(random.choice(lista))

#print(random.sample(lista,3))

#print(random.shuffle(lista))
n=random.shuffle(nlista)
print(n)
print(nlista)
