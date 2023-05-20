nome=input('Insira seu nome:')
rg=input('Insira seu RG:')
telefone=input('Insira o seu número de telefone:')
salario_bruto=float(2500)
descontos=(float(300))
salario_liquido=salario_bruto-descontos
print('Prezado {}, de telefone {}, seu salário líquido é de {}'.format(nome,telefone,salario_liquido))