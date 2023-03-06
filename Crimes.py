positive = 0
print('Responda as perguntas com S ou N:')
question1 = str(input('Telefonou para a vítima? ')).lower()
if question1 == 's':
    positive += 1
question2 = str(input('Esteve no local do crime? ')).lower()
if question2 == 's':
    positive += 1
question3 = str(input('Mora perto da vítima? ')).lower()
if question3 == 's':
    positive += 1
question4 = str(input('Devia para a vítima? ')).lower()
if question4 == 's':
    positive += 1
question5 = str(input('Já trabalhou com a vítima? ')).lower()
if question5 == 's':
    positive += 1

if positive == 2:
    print('Você está classificada como suspeita!')
elif positive == 3 or positive == 4:
    print('Você está classificada como cúmplice!')
elif positive == 5:
    print('Você está classificada como assassino!')
else:
    print('Inocente!')
