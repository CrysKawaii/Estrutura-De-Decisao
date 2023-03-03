wage = float(input('Digite seu salário: R$'))
print(f'Seu salário atual é de R${wage:.2f}')
if wage <= 280:
    new_salary = wage + (wage * 20/100)
    print(f'Com o ajuste de 20% que equivale a R${wage * 20/100:.2f}')
    print(f'Seu novo salário fica {new_salary:.2f}')
elif wage <= 700:
    new_salary = wage + (wage * 15/100)
    print(f'Com o ajuste de 15% que equivale a R${wage * 15/100:.2f}')
    print(f'Seu novo salário é de {new_salary:.2f}')
elif wage <= 1500:
    new_salary = wage + (wage * 10/100)
    print(f'Com o ajuste de 10% que equivale a R${wage * 10/100:.2f}')
    print(f'Seu novo salário é de {new_salary:.2f}')
elif wage > 1500:
    new_salary = wage + (wage * 5/100)
    print(f'Com o ajuste de 5% que equivale a R${wage * 5/100:.2f}')
    print(f'Seu novo salário é de {new_salary:.2f}')
