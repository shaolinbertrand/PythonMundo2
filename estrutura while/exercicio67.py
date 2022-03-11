x = i = 0
while True:
    x = int(input('digite um numero: '))
    if x<0:
        break
    print('~'*20)
    while i <=10:
        print(f'{x} x {i} = {x*i}')
        i += 1
    i = 0
    print('~'*20)
print(10*'~','FIM',10*'~')
