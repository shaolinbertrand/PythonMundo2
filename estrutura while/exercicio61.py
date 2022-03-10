p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
i = 1
while i < 11:
    print("O {}º termo é {}".format(i,p+(i-1)*r))
    i = i+1