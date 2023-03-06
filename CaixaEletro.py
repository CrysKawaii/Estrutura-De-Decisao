withdrawal_amount = float(input('Digite o valor do saque (míninmo 10, máximo 600): '))
# aqui pega o valor da centena do número dividindo por cem
hundred = int(withdrawal_amount / 100)
# agora pega a parte do número fora a centena, ou seja, vai tirar o que foi removido na variável anterior
withdrawal_amount = (withdrawal_amount - hundred * 100)
# o processo se repete mas muda o número da cédula >>>
fifty = int(withdrawal_amount / 50)
withdrawal_amount = withdrawal_amount - (fifty * 50)
ten = int(withdrawal_amount / 10)
withdrawal_amount = withdrawal_amount - (ten * 10)
five = int(withdrawal_amount / 5)
withdrawal_amount = withdrawal_amount - (five * 5)
one = int(withdrawal_amount)
print(f'''
     CÉDULAS   |     QUANTIA
\tR$100,00           \t{hundred}
\tR$50,00            \t{fifty}
\tR$10,00            \t{ten}
\tR$5,00             \t{five}
\tR$1,00             \t{one}''')
