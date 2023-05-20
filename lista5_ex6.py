lista=[]
for n in range(0,10):
    lista.append(int(input('Insira 10 números inteiros:')))
for n in lista:
    
    if(n%3==0):
        print('múltiplo de 3:',n)
    elif(n<45):
        print('menor que 45:',n)
    elif(n>55):
        print("maior que 55:",n)