n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
higher = n1
if n2 > n1 and n2 > n3:
    higher = n2
elif n3 > n2 and n3 > n1:
    higher = n3
print(f'O maior número entre eles é {higher}')
