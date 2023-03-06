print('Digite uma data no formato dd/mm/aaaa')
day = int(input('Digite o dia: '))
month = str(input('Digite o mês: '))
month = int(month)
year = int(input('Digite o ano: '))
if day > 31 or month > 12 or year < 0:
    print('Essa não é uma data válida!')
else:
    print('Essa é uma data válida!')
    print(f'{day}/0{month}/{year}')
