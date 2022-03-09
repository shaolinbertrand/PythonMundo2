nomemv = ''
media = m20 = mv = 0
for i in range(4):
    nome = input('Digite o nome da pessoa {}: '.format(i))
    idade = int(input('Digite a idade do(a) {}: '.format(nome)))
    sexo = input('Digite o sexo do(a) {}: '.format(nome))
    media = media + idade
    if(sexo=='f'):
        if(idade<20):
            m20 = m20+1
    else:
        if(idade > mv):
            nomemv=nome
            mv = idade
print(nomemv,' é o homem mais velho')
print('A media de idades do grupo é ',media/4)
print('Existem {} mulheres com menos de 20 anos'.format(m20))