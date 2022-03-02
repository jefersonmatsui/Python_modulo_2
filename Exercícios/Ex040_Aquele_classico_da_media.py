# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
avg = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {avg:.2f}')
if avg > 7:
    print('O aluno está APROVADO! PARABÈNS!!!')
elif 5 <= avg < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print(('O aluno está REPROVADO!'))