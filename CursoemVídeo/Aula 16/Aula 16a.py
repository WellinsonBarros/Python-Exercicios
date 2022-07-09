'''Crie um programa que tenha uma tupla
totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número
pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''
n = int(input('Digite um número entre 0 e 20: '))
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    if n in range(0, 20):
        print(extenso[n])
        break
    else:
        int(input('Tente novamente. Digite um número entre 0 e 20: '))
