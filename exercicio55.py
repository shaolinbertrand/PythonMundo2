ma = 0
me = 9999
for i in range(5):
    x=int(input("digite o peso: "))
    if x > ma:
        ma = x
    if x<me:
        me = x
print('O maior peso digitado foi {} e o menor foi {}'.format(ma,me))