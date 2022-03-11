n = s = q = 0
while True:
    n=int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'foram digitados {q} numeros a soma vale {s}')