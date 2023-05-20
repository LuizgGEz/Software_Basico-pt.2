import math
def opcao (valor1,valor2):
    if (escolha=="a"):
        print(valor1+valor2)
    elif (escolha=="b"):
        print(valor1-valor2)
    elif (escolha=="c"):
        print(valor1*valor2)
    elif (escolha=="d"):
        print(valor1/valor2)
    elif (escolha=="e"):
        print(math.sqrt(valor1))
n1=int(input('Insira o primeiro número inteiro:'))
n2=int(input('Insira o segundo número inteiro:'))
print('\n a)Soma \n b)Subtrair \n c)Multiplicar \n d)Dividir \n e)Raiz quadrada do primeiro número. \n')
escolha=input('Insira a letra da opção desejada:')
opcao(n1,n2)