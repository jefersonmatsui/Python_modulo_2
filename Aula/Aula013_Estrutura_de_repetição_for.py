# vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
# que é uma estrutura versátil e simples de entender. Por exemplo:
# for c in range(0, 4):
# print(c)
# print(‘Acabou’)
'''
# Aparece 5 'oi', o ultimo não conta
for c in range (1, 6):
    print('Oi')
print('FIM')

# Aparece 6 'oi', lembrando que a contagem começa no 0 e não no 1
for c in range (0, 6):
    print('Oi')
print('FIM')

# vai aparecer  Oi Fim 6 vezes, pq o a palavra fim está dentro do laço de repetição
for c in range (0, 6):
    print('Oi')
    print('FIM')

# contagem de números
for c in range (0, 6):
    print(c)
print('FIM')

# Ordem decrescente
#           começa, termina, passo
for c in range (6, 0, -1):
    print(c)
print('FIM')

for c in range (0, 7, 2):
    print(c)
print('FIM')


n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')


# Pede o comando 3 vezes
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')

'''

# Somatório
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
#   s = s + n
    s += n
print(f'O somatótio de todos os valores foi {s}')