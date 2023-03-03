side1 = float(input('Digite o 1° lado: '))
side2 = float(input('Digite o 2° lado: '))
side3 = float(input('Digite o 3° lado: '))
if side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2:
    print('Pode formar um triângulo', end=' ')
    if side1 == side2 == side3:
        print('Equilátero!')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Isóceles!')
    else:
        print('Escaleno!')
else:
    print('Não forma nada!')
