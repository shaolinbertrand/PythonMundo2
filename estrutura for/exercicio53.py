x = input("digite uma frase qualquer: ").strip().upper()
palavras = x.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo')