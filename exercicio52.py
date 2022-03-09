x = int(input('Digite um numero: '))
c = 0
for i in range(1,x):
    if(x%i==0):
         if(i!=1):
             if(i!=x):
                print("não é primo")
                break
    c=i+1      
if c == x:
    print('É primo')