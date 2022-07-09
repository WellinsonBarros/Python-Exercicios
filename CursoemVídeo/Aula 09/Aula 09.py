'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo sem considerar os espaços.
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
divido = nome.split()
print(f'Seu primeiro nome tem {len(divido[0])}')
