# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
''')
player = int(input('Qual é a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.3)
print('-='*13)
print(f'Jogador jogou {itens[player]}')
print(f'Computador jogou {itens[computer]}')
print('-='*13)

if computer == 0:
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('JOGADOR VENCE!')
    elif player == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')
elif computer == 1:
    if player == 0:
        print('COMPUTADOR VENCE!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA')
elif computer == 2:
    if player == 0:
        print('JOGADOR VENCE!')
    elif player == 1:
        print('COMPUTADOR VENCE!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('Opção inválida. Tente novamente.')