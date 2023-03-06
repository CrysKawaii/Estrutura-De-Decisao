num = int(input('Digite um número inteiro menor que 1000: '))

units = num % 10
hundreds = num // 100
dozens = ((num - units) / 10) % 10

if hundreds == 1:
    print(f'Esse número tem {hundreds} centena')
else:
    if hundreds != 0:
        print(f'Esse número tem {hundreds} centenas')

if dozens == 1:
    print(f'Esse número tem {dozens:.0f} dezena')
else:
    if dozens != 0:
        print(f'Esse número tem {dozens:.0f} dezenas')

if units == 1:
    print(f'Esse número tem {units} unidade')
else:
    if units != 0:
        print(f'Esse número tem {units} unidades')
