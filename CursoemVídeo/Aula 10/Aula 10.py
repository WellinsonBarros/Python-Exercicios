'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
n = int(input('Escolha um número entre 0 e 5: '))
r = random.randint(0, 5)
if n == r:
    print('Parabéns, você conseguiu me vencer!')
else:
    print(f'Eu ganhei, pensei no {r} e não no {n}')

