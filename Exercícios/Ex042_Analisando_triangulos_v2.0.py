# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-*'*15)
print('ANALISADOR DE TRIÂNGULOS V2.0')
print('*-'*15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmnto: '))
c = float(input('Terceiro segmento: '))
if a + b >= c and b + c >= a and a + c >= b:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a == b != c or a == c != b or b == c != a:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulos \033[34m{tipo}')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triãngulo')