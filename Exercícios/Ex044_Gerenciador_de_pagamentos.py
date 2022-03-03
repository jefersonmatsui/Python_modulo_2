# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('*'*30)
print('{:=^38}'.format("\033[33mPEPA'S STORE\033[m"))
print('*'*30)

price = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
option = int(input('Qual é a opção? '))

if option == 1:
    money = price - (price * 0.10)
elif option == 2:
    money = price - (price * 0.05)
elif option == 3:
    money = price
elif option == 4:
    quota = int(input('Quantas parcelas? '))
    money = price + (price * 0.20)
    print(f'Sua compra será parcelada em {quota}x de R${(money/quota):.2f} COM JUROS.')
else:
    money = price
    print('Opção INVÁLIDA de pagamento. Tente Novamente!')
print(f'Sua compra de R${price:.2f} vai custar R${money:.2f} no final.')
