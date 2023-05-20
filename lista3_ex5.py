from ssl import HAS_NEVER_CHECK_COMMON_NAME


altura=float(input('Insira a sua altura:'))
sexo=input('Digite o seu sexo:')
peso_1=(72.7*altura)-58
peso_2=(62.1*altura)-44.7
if(sexo =='homem'):
    print(peso_1)
elif(sexo == 'mulher'):
    print(peso_2)
else:
    print('Sexo inválido')
