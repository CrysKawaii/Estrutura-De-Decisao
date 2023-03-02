n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
average = (n1 + n2) / 2
print(f'Sua média é {average}')
if average == 10:
    print('Aprovado com Distinção!')
elif average >= 7:
    print('Aprovado!')
elif average < 7:
    print('Reprovado!')
