'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
núm = int(input('Digite um número: '))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[34m', end=' ')
    else:
        print('\33[m', end=' ')
    print(f'{c}', end=' ')
