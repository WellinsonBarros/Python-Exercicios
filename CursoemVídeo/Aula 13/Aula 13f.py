'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 33)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:          '))
print('=' * 33)
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(f'{c}', end=' → ')
print('Fim')
