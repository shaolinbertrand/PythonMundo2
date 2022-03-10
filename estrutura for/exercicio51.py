p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
for i in range(1,11):
    print("O termo {} é {}".format(i,p+(i-1)*r))