salario=float(input('Insira seu salário;'))
valor=float(input('Insira o valor da prestação:'))
porcentagem=salario*(20/100)
if(valor>porcentagem):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
