from datetime import date
atual = date.today().year
ma = me = 0
for i in range(7):
    x = int(input("digite o ano de nascimento: "))
    if (atual-x > 20):
        ma = ma+1
    else:
        me = me+1
print('{} são maiores de idade e {} são menores de idade'.format(ma,me))