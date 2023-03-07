print('=============   MERCADO TABAJARA   =============')
print('''
                   Até 5 Kg              Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
''')
print('~~' * 52)
print('Devido a alta demanda, só é possível escolher UM tipo de carne! Contudo, não há limites de quantidade!')
print('Se o cliente escolher pagar pelo cartão Tabajara, receberá ainda um desconto de 5% no total!')
print('~~' * 52)
type_meat = str(input('''
 (A) Filé Duplo
 (B) Alcatra
 (C) Picanha
 
 Digite a opção referente ao tipo de carne qua vai levar: '''))
kgs = float(input('Digite quantos KGs vai comprar: '))
price_file = 4.90
price_alcatra = 5.90
price_picanha = 6.90
total = 0
discount = 0
if kgs > 5:
    price_file = 5.80
    price_alcatra = 6.80
    price_picanha = 7.80
if type_meat == 'a':
    total = price_file * kgs
    type_meat = 'Filé Duplo'
elif type_meat == 'b':
    total = price_alcatra * kgs
    type_meat = 'Alcatra'
elif type_meat == 'c':
    total = price_picanha * kgs
    type_meat = 'Picanha'
total_final = total
payment = str(input('Vai usar o cartão Tabajara?[S/N] '))
if payment == 's':
    payment = 'Cartão'
    discount = 5
    total_final -= (total * 5/100)
else:
    payment = 'Á vista'
print(f'''*************   CUPOM FISCAL   *************
TIPO                \t\t|   {type_meat}
QUANTIDADE          \t\t|   {kgs}Kgs
PREÇO TOTAL         \t\t| R${total:.2f}
TIPO DE PAGAMENTO   \t\t|   {payment}
VALOR DO DESCONTO   \t\t|   {discount}%
VALOR A PAGAR       \t\t| R${total_final:.2f}''')
