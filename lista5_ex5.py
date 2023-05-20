lista=[]
for n in range(0,15):
    lista.append(float(input('Insira 15 temperaturas em graus Celsius:')))
for n in lista:
    x=((9*n)/5)+32
    print(x)