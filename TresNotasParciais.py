n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
n3 = float(input('Digite a 3° nota: '))
average = (n1 + n2 + n3) / 3
if average == 10:
    print('Aprovado com Distinção! Tirou a média 10!')
elif average >= 7:
    print(f'Aprovado com a média {average:.1f}!')
else:
    print(f'Reprovado com a média {average:.1f}!')
