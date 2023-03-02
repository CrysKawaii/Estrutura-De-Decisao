price1 = float(input('Qual o preço do 1° produto? R$'))
price2 = float(input('Qual o preço do 2° produto? R$'))
price3 = float(input('Qual o preço do 2° produto? R$'))
cheaper = price1
if price2 < price1 and price2 < price3:
    cheaper = price2
elif price3 < price2 and price3 < price1:
    cheaper = price3
print(f'Você deve comprar o de R${cheaper}')
