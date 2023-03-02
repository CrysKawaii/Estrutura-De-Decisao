print('Turnos')
print('''
[M] - Matutino
[V] - Vespertino
[N] - Noturno
''')
shift = str(input('Digite qual turno você estuda [M/V/N]: ')).upper()
if shift == 'M':
    print('Bom dia!')
elif shift == 'V':
    print('Boa Tarde!')
elif shift == 'N':
    print('Boa noite!')
else:
    print('Opção inválida!')
