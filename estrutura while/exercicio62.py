p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
v = f = int(input('Digite quantos termos você deseja ver: '))
i = 1

while v!=0:
    print("O {}º termo é {}".format(i,p+(i-1)*r))
    i = i+1
    if(i>f):
        print('quantos termos a mais você deseja ver?')
        v = int(input('digite o valor: '))
        f += v
