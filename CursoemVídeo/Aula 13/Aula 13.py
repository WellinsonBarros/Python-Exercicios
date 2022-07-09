cont = 0
soma = 0
mult = 1
for c in range(1, 6):
    print(f'{c}', end=' ')
    cont = cont + 1
    soma = soma + c
    mult = mult * c
print(f'\nO número de elementos é: {cont}, sua soma é: {soma} e sua multiplicação é de: {mult}')
