year = int(input('Digite um ano: '))
if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Não é bissexto!')
