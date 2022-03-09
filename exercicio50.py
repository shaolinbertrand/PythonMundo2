soma =0
for i in range(6):
    x = int(input('Digite um numero: '))
    if x % 2 == 0:
        soma = soma + x
print("A soma dos numeros pares digitados é {}".format(soma))