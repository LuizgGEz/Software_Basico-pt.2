n=int(input('Insira um número inteiro maior que 2:'))
while(n<=2):
    n=int(input('Insira outro número inteiro, que seja maior que 2:'))
x=2
while(x<n):
    print(x+x,x+x*x)
    x+=1