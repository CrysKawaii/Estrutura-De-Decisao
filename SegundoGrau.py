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
    root1 = ((-b) + sqrt(delta)) / 2 * a
    print(root1)
elif delta > 0:
    print('Delta positivo, duas raizes:')
    root1 = ((-b) + sqrt(delta)) / 2 * a
    root2 = ((-b) - sqrt(delta)) / 2 * a
    print(root1)
    print(root2)
