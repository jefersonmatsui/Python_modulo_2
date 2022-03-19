# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


valor = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    for contagem in range (0, 11):
        print(f'{valor} x {contagem:2} = {valor * contagem}')
    print('-'*20)
print('Programa encerrado...')

