strawberry = float(input('Digite quantos Kgs de morango vai levar: '))
apple = float(input('Digite quantos Kgs de maçãs vai levar: '))

price_strawberry = 2.50
price_apple = 1.80

if apple > 5:
    price_apple = 1.50
elif strawberry > 5:
    price = 2.20

total = (price_apple * apple) + (price_strawberry * strawberry)

if (strawberry + apple) > 8 or total > 25:
    total -= (total * 10/100)

print(f'O valor a ser pago pela compra é R${total}')
