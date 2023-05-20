numero=int(input('Digite um número entre 1 e 7:'))
while(numero<8)and(numero>0):
    if(numero==1):
        print('Segunda-feira')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==2):
        print('Terça-feira')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==3):
        print('Quarta-feira')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==4):
        print('Quinta-feira')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==5):
        print('Sexta-feira')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==6):
        print('Sábado')
        numero=int(input('Digite outro número entre 1 e 7:'))
    elif(numero==7):
        print('Domigo')
        numero=int(input('Digite outro número entre 1 e 7:'))
print('Número inválido')