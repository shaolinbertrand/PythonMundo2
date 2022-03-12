o = c50 = c20 = c10 = r = 0
while True:
    o = int(input('Quanto voce deseja sacar? '))
    r = o
    while r >= 50:
        c50 += 1
        r = r - 50
    while r >= 20:
        c20 += 1
        r = r - 20
    while r > 10:
        c10 += 1
        r = r - 10
    if r < 10:
        break
print(f'Para o valor de R$ {o}')
if c50 >0:
    print(f'Foram emitidas {c50} cedulas de R$ 50')
if c20>0:
    print(f'Foram emitidas {c20} cedulas de R$ 20')
if c10>0:
    print(f'Foram emitidas {c10} cedulas de R$ 10')
if r>0:
    print(f'Foram emitidas {r} cedulas de R$ 1')
    