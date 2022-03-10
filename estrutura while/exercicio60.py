n = y = x = int(input('digote um numero: '))
while x>1:
    n = n * (x-1)
    x = x-1
print('o fatorial de {} é {}'.format(y,n))