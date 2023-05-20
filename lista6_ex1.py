celsius=float(input('Insira a temperatura em celsius:'))
while(celsius>=-5):
    print('A temperatura em Fahrenheit é',(celsius*9/5)+32)
    print("A temperatura em Kelvin é",celsius+273,15)
    celsius=float(input('Insira outra temperatura em celsius:'))
print('Operação finalizada.')