n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
higher = smaller = n1
if n2 > n1 and n2 > n3:
    higher = n2
elif n3 > n2 and n3 > n1:
    higher = n3
if n2 < n3 and n2 < n1:
    smaller = n2
elif n3 < n2 and n3 < n1:
    smaller = n3
print(f'O maior é {higher}')
print(f'O menor é {smaller}')
