# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[031m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

