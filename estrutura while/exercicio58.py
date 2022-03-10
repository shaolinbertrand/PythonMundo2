from random import random


from random import *
n = randint(0,10)
p = int(input('Adivinhe o numero que estou pensando: '))
while(n!=p):
    p = int(input('Errou tente novamente: '))
print('Acertou')