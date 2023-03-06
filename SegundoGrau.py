from math import *
print('ax2 + bx + c')
a = int(input('Digite o valor de A: '))
if a == 0:
    quit()
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = (b * b) - (4 * a * c)
print(delta)
if delta < 0:
    print('A equação não possui raizes pois delta é negativo!')
    quit()
elif delta == 0:
    print('Delta é 0, logo só possui uma raiz real:')
    raiz1 = ((-b) + sqrt(delta)) / 2 * a
    print(raiz1)
elif delta > 0:
    print('Delta positivo, duas raizes:')
    raiz1 = ((-b) + sqrt(delta)) / 2 * a
    raiz2 = ((-b) - sqrt(delta)) / 2 * a
    print(raiz1)
    print(raiz2)
