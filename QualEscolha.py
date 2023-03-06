num = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('''
[1] SOMAR
[2] SUBTRAIR
[3] DIVIDIR
[4] MULTIPLICAR
''')
choice = int(input('Digite o número referente a operação que deseja fazer: '))
if choice == 1:
    addition = n1 + n2
    print(f'A soma desses números é {addition}')
    num = addition
elif choice == 2:
    subtraction = n1 - n2
    print(f'A subtração desses números é {subtraction}')
    num = subtraction
elif choice == 3:
    division = n1 / n2
    print(f'A divisão dos número é {division:.2f}')
    num = division
elif choice == 4:
    multiplication = n1 * n2
    print(f'A multiplicação desses números é {multiplication}')
    num = multiplication
if num % 2 == 0:
    print('Esse número é par!')
else:
    print('Esse número é impar!')
if num > 0:
    print('Esse número é positivo!')
else:
    print('Esse número é negativo!')
num = str(num)
if '.' in num:
    print('Esse número é decimal!')
elif ',' in num:
    print('Esse número é decimal!')
else:
    print('Esse número é inteiro!')
