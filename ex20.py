horas=float(input('Insira o número de horas trabalhadas:'))
valor=float(input('Insira o valor do salário mínimo:'))
valor_hora=(valor//2)
salario_bruto=horas*valor_hora
imposto=salario_bruto*3/100
salario_a_receber=salario_bruto-imposto
print('O salário a receber é:',salario_a_receber)