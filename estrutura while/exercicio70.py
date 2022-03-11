NomeB = nome = ''
p = total = pM = 0
mb = 99999999

while True:
    nome = input('Digite o nome do produto: ').upper()
    p = float(input('Digite o valor do produto: '))
    total += p
    if p < mb:
        NomeB = nome
        mb = p
    if p > 1000:
        pM += 1
    print('~'*20)
    o = input('Deseja continuar [S/N]: ').upper()
    if o == 'N':
        break
print('~'*20)
print(f'Foram gasto R${total:.2f} \n {pM} produtos custam mais de R$ 1000\n O produto mais Barato é o {NomeB:*^5}')
print('~'*20)