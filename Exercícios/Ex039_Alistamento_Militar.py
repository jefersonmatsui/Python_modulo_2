#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#  do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('-='*10)
print('ALISTAMENTO MILITAR')
print('-='*10)

nome = str(input('Nome Completo: '))
sexo = str(input('M para masculino e F para feminino: ')).upper().strip()
if sexo == 'F':
    print('Você não precisa se alistar')
else:
    from datetime import date
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc

    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

    if idade < 18:
        n1 = 18 - idade
        if n1 == 1:
            print(f'Ainda faltam {n1} anos para o alistamento.')
        else:
            print(f'Ainda falta {n1} ano para o alistamento.')
        print(f'Seu alistamento será em {nasc + 18}')

    elif idade <= 18:
        n1 = idade - 18
        if n1 == 1:
            print(f'Você já deveria ter se alistado há {n1} ano.')
        else:
             print(f'Você já deveria ter se alistado há {n1} anos.')
        print(f'Seu alistamento foi em {nasc + 18}')
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
