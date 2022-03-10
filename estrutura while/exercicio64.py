n = int(input('Digite um valor: '))
q = s = 0

while n!=999:
    q +=1
    s += n
    n = int(input('Digite um valor: '))
print('Foram digitados {} numeros e a soma entre eles é {}'.format(q,s))