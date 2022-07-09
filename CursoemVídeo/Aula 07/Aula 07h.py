''' Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
x = float(input('Altura da parede: '))
y = float(input('Largura da parede: '))
z = x*y
t = z/2
print(f'A parede possui uma área de: {z}m²\nSão necessários {t}Litros de tinta')
