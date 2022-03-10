i = int(input('quantos numeros da sequencia fibonacci você deseja ver: '))
a = 0
b = 1
n=0
while n < i:
    print(' {} '.format(a), end='->')
    at = a
    a = a + b
    b = at
    n= n+1
print(' fim')