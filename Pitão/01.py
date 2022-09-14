#Considere um programa que deve classificar um número como par ou ímpar e, além disso, classificar ele como menor do que
# 100 ou maior ou igual a 100. Escreva um programa que faça essa classificação corretamente.

number = float(input('Escolha um número :'))
if number % 2 == 1:
    print(f'O número {number} é IMPAR,')
else:
    print(f'O número {number} é PAR,')
if number > 100:
    print('e maior que 100')
else:
    print('e menor que 100')