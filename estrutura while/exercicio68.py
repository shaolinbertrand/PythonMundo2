from random import *
v = j = c = 0
o = ''
while True:
    j = int(input('escolha um numero: '))
    c = randint(1,10)
    o = input('Par ou Impar [P/I]: ').upper()
    while o not in 'PI':
            o = input('Opção invalida por favor digite [P/I]').upper()
    if o == 'P':
        if (j + c) % 2 == 0:
            print('Você Venceu !!!')
            print(f'você escolheu {j} e eu escolhi {c} e {j+c} é PAR')
            v +=1
        else:
            print('Perdeu seu pato huehuehe')
            print(f'você escolheu {j} e eu escolhi {c} e {j+c} é IMPAR')
            break
    elif o== 'I':
        if (j + c) % 2 == 1:
            print('Você Venceu !!!')
            print(f'você escolheu {j} e eu escolhi {c} e {j+c} é IMPAR')
            v +=1
        else:
            print('Perdeu seu pato huehuehe')
            print(f'você escolheu {j} e eu escolhi {c} {j+c} é PAR')
            break
print(f'Você obteve {v} vitorias consecutivas')