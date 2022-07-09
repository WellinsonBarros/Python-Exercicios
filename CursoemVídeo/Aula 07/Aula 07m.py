'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
km = float(input('Digite a quantidade de km percorridos: '))
dias = float(input('Digite a quantidade de dias de aluguel: '))
d = dias * 60
k = km * 0.15
p = d + k
print(f'O preço pago pelo alguel do carro será de: R$ {p}')
