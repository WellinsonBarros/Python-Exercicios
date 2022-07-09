'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''
import math
n1 = float(input('Digite um número: '))
print(f'O valor digitado foi {n1} e a sua porção inteira é {math.trunc(n1)}')
