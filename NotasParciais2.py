n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
average = (n1 + n2) / 2
print(f'Sua notas foram {n1} e {n2}')
print(f'Sua média foi {average}')
if 9 < average <= 10:
    print('Conceito: A')
    print('Aprovado!')
elif 7.5 <= average < 9:
    print('Conceito: B')
    print('Aprovado!')
elif 6 <= average < 7.5:
    print('Conceito: C')
    print('Aprovado!')
elif 4 <= average < 6:
    print('Conceito: D')
    print('Reprovado!')
elif 0 <= average < 4:
    print('Conceito: E')
    print('Reprovado!')
