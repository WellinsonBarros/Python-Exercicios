'''Crie um programa que declare uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final, mostre
a matriz na tela, com a formatação correta.'''
'''l0 = [[],[],[]]
l1 = [[],[],[]]
l2 = [[],[],[]]
for c in range(0, 3):
    l0[c].append(int(input(f'Digite um valor para [0, {c}]: ')))
for d in range(0, 3):
    l1[d].append(int(input(f'Digite um valor para [1, {d}]: ')))
for e in range(0, 3):
    l2[e].append(int(input(f'Digite um valor para [2, {e}]: ')))
print('-=' * 25)
print('A matriz é:')
print(f'{l0[0]} {l0[1]} {l0[2]}')
print(f'{l1[0]} {l1[1]} {l1[2]}')
print(f'{l2[0]} {l2[1]} {l2[2]}')
print('-=' * 25)'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
