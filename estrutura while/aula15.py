n = s = 0
'''while True:
    n=int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('a soma vale ',s)'''
print(f'A soma vale {s}')
nome = 'Jean'
idade = 28
salario = 1500
print(f'Testando a string {nome:~^20} tem {idade} anos e ganha R${salario:.2f}')