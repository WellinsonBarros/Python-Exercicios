'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    elif valor % 1 == 0:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares são: {núm[0]}')
print(f'Os valores ímpares são: {núm[1]}')
print('-=' * 30)
