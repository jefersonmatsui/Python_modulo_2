# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
resultado = 1
count = 1
numero = int(input('Digite um número para calcular seu fatorial: '))
while count <= numero:
    resultado *= count
    count += 1
print(f'Calculando {numero}! = {resultado}')
'''


'''
print('Solução Professor')
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')
'''

print('Solução Professor 2')
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
