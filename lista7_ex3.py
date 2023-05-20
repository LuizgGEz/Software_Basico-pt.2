import math
def volume(raio):
    return 4/3*math.pi*raio**3
medida=float(input('Insira o raio da circunferência:'))
v=volume(medida)
print(v)