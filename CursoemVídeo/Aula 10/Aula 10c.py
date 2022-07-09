'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.'''
d = float(input('Qual foi a distância percorrida na viagem? '))
v = (d * 0.5)
v2 = (d * 0.45)
if v <= 100:
    print(f'O preço da passagem é de: {v}')
else:
    print(f'O preço da passagem é de: {v2}')
print('Boa Viagem')
