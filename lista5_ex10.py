lista=[]
for n in range(0,5):
    lista.append(float(input('Insira 5 números:')))
for n in lista:
    if(n<0):
        n=0
        print(n)
    else:
        print(n)