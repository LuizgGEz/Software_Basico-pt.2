import math
lado_b=float(input('Digite um lado do triângulo retângulo:'))
lado_c=float(input('Digite o outro lado do triângulo retângulo:'))
lado_a=lado_b**2+lado_c**2
hipotenusa=math.sqrt(lado_a)
print('A hipotenusa é:',hipotenusa)