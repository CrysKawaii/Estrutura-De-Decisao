liters = float(input('Digite quantos litros você vai abastecer: '))
price = 0
print('''
A - Álcool
G - Gasolina''')
choice = str(input('Qual vai ser?[A/G] ')).lower()
if choice == 'a' and liters <= 20:
    price = liters * (1.90 - (1.90 * 3/100))
elif choice == 'a' and liters > 20:
    price = liters * (1.90 - (1.90 * 5/100))
elif choice == 'g' and liters <= 20:
    price = liters * (2.50 - (2.50 * 4/100))
elif choice == 'g' and liters > 20:
    price = liters * (2.50 - (2.50 * 6/100))

print(f'Preço final: R${price} para {liters} litros ')
