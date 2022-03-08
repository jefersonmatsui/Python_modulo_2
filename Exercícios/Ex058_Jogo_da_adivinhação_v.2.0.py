# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.


from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi? 
''')
computador = randint(0, 10)
count = 0
palpite = int(input('Qual é o seu palpite? '))
while palpite != computador:
    if palpite < computador:
        palpite = int(input('Mais... Tente mais uma vez.\nQual é seu palpite? '))
        count += 1
    if palpite > computador:
        palpite = int(input('Menos... Tente mais uma vez.\nQual é seu palpite? '))
        count += 1
print(f'Acertou com {count} tentativas. Parabéns!')


'''
#RESPOSTA PROFESSOR

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')

'''