lista=[]
numero=float(input('Digite um número:'))
while(numero!=0):
    lista.append(numero)
    numero=float(input('Digite outro número:'))
x=sum(lista)
y=len(lista)
z=x/y
print('A somatória dos valores inseridos é',x)
print('A média é',z)