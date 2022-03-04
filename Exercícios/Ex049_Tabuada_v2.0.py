# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite um número para ver sua tabuada: '))
for contagem in range(0, 11):
    print(f'{numero} x {contagem:2} = {numero * contagem}')


