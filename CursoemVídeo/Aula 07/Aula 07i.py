'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
x = float(input('Valor do produto: R$ '))
d = x * 0.95
print(f'Valor com desconto é de: R${d:.2f}')
