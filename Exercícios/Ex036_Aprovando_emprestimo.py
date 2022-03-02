# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Qual o salário do comprador: R$'))
fin = float(input('Quantos anos de financiamento: '))

mes = fin * 12
prest = casa / mes
exc = salario * 30/100

print(f'Para pagar uma casa de R${casa:.2f} em {fin:.0f} anos a pretação será de R${prest:.2f}')
if exc > prest:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
