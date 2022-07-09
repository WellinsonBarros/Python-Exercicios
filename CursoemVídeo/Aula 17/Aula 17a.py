'''Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas
respectivas posições na lista. '''
lista = []
mai = 0
men = 0
for ncont in range(0, 5):
    lista.append(int(input(f'Digete um valor para posição {ncont}: ')))
    if ncont == 0:
        mai = men = lista[ncont]
    else:
        if lista[ncont] > mai:
            mai = lista[ncont]
        if lista[ncont] < men:
            men = lista[ncont]
print('=-' * 25)
print(f'Você digitou os valores: {lista}')
#print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))}')
#print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista))}')
print(f'O maior valor digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()
print('=-' * 25)
