'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa'''
from math import hypot
catetooposto = float(input('Valor do cateto oposto: '))
catetoadjacente = float(input('Valor do cateto adjacente: '))
hipotenusa = hypot(catetooposto, catetoadjacente)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
