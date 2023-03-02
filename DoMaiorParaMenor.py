n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
first = second = third = n1
if n2 > n1 and n2 > n3:
    first = n2
elif n2 < n1 and n2 < n3:
    third = n2
else:
    second = n2
if n3 > n1 and n3 > n2:
    first = n3
elif n3 < n1 and n3 < n2:
    third = n3
else:
    second = n3
print(first, second, third)
