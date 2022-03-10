x = int(input('Digite um numero: '))
c = 0
for i in range(1,x):
    if(x%i==0):
         if(i!=1):
             if(i!=x):
                print('\033[31m'," não é primo")
                break
    c=i+1      
if c == x:
    print('\033[33m')
    print('É primo ')