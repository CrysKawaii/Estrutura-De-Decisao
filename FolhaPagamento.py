ear_hour = float(input('Digite quanto você ganha por hora: R$'))
hour_month = float(input('Digite quantas horas trabalha por mês: '))
wage = ear_hour * hour_month
ir = inss = fgts = 0
if wage <= 900:
    inss = wage * 10/100
    fgts = wage * 11/100
elif wage <= 1500:
    ir = wage * 5/100
    inss = wage * 10 / 100
    fgts = wage * 11 / 100
elif wage <= 2500:
    ir = wage * 10/100
    inss = wage * 10 / 100
    fgts = wage * 11 / 100
elif wage > 2500:
    ir = wage * 20/100
    inss = wage * 10 / 100
    fgts = wage * 11 / 100

print(f'''
Salário Bruto   ({ear_hour} * {hour_month})                :  R${wage:.2f}
(-) IR                   ({ir})              :  R${ir:.2f}
(-) INSS                 (10%)               :  R${inss:.2f}
FGTS                     (11%)               :  R${fgts:.2f}
Total de descontos                           :  R${ir + inss:.2f}
Salário líquido                              :  R${wage - ir - inss:.2f}'''.replace('.', ','))
