lista=[-5,-4,-3,-2,-1,1,2,3,4,5]
for n in lista:
    if (n %3==0 and n<0):
        print(n,"múltiplo de 3", 'negativo')
    elif (n %3==0 and n>0):
        print(n,"múltiplo de 3", 'positivo')
    elif (n %3>0 and n>0):
        print(n,"não é múltiplo de 3", 'positivo')
    else:
        print(n,'não é múltiplo de 3',"negativo")