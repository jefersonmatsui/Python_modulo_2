# vamos aprender como utilizar a instrução break e os loopings
# infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Python, já que em
# alguns casos precisamos interromper um laço no meio do caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
'''
# Conta até 10
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

# Conta infinitamente
cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

'''

# utilizando flag
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

