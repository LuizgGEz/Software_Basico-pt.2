lista=[]
maior80=[]
menor10=[]
numero=int(input('Digite um número inteiro:'))
while(numero!=100):
    lista.append(numero)
    if(numero>80):
        maior80.append(numero)
        numero=int(input('Digite outro número inteiro:'))
    elif(numero<10):
        menor10.append(numero)
        numero=int(input('Digite outro número inteiro:'))
x=sum(lista)
y=len(lista)
z=x/y
print('Valores acima de 80:',maior80)
print('Valores menores que 10:',menor10)
print('A média é',z)