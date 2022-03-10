x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
o = 0
while(o != 5):
    print('Escolha a opção desejada')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Numeros')
    print('[5] Sair do Programa')
    o = int(input("Opção: "))
    if (o==1):
        print('{} + {} = {}'.format(x,y,x+y))
    elif(o==2):
        print('{} x {} = {}'.format(x,y,x*y))
    elif(o==3):
        if x>y:
            print('{} > {}'.format(x,y))
        else:
            print('{} > {}'.format(y,x))
    elif(o==4):
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))
    print("=============================")
print('fim')
