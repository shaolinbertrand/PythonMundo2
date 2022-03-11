from tkinter import E


idade = 0
sexo = ''
maior = 0
h = 0
m20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]:').upper()
    while sexo not in 'MF':
        print('Sexo invalido')
        sexo = input('Digite o sexo [M/F]:').upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        h += 1
    elif sexo == 'F':
        if idade < 20:
            m20 += 1
    print('Cadastro Realizado com Sucesso')
    print('*'*20)
    o = input('Deseja conrinuar [S/N]: ').upper()
    if o == 'N':
        break
print('*'*20)
print(f'Foram cadastrados {maior} pessoas maior de idade \n {h} homens\n {m20} mulheres com menos de 20 anos')
print('*'*20)