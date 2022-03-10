from random import random


from random import *
n = randint(0,10)
p = int(input('Adivinhe o numero que estou pensando: '))
i = 1
while(n!=p):
    if p<n:
        p = int(input('Errou tente novamente um pouco mais...: '))
    else:
        p = int(input('Errou tente novamente um pouco menos...: '))
    i +=1
print('Acertou depois de {} tentativas'.format(i))