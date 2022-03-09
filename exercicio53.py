x = input("digite uma frase qualquer: ")
x = x.replace(' ','')
tam = len(x)
metade = int(tam/2)
for i in range(metade,1,-1):
    for j in range(1,metade,1):
        if(x[i] != x[j]):
            print('não é palindromo')
            break
print('É palindromo')
