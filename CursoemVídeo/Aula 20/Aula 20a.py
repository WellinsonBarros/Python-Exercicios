''' Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''
def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


print('  Controle de Terrenos  ')
print('-' * 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
print('-' * 25)
