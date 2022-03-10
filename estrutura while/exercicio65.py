a = int(input('Digite um valor: '))
x = 1
soma = maior = menor = a
cmedia = 2
while x != 0:
    print('Quantos numeros você deseja continuar digitando')
    x = int(input('entre com o valor: '))
    i = 0
    while i<x:
        a = int(input('Digite mais um valor: '))
        i+=1
        cmedia +=1
        soma +=a
        if a > maior:
            maior = a
        elif a<menor:
            menor=a
print('a media entre todos os numeros digitados é %.2f'%(soma/cmedia))
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))