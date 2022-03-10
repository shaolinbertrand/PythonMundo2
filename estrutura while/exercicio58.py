from random import random


from random import *
n = randint(1,10)
p = int(input('Adivinhe o numero que estou pensando: '))
print(n)
while(n!=p):
    p = int(input('Errou tente novamente: '))
print('Acertou')