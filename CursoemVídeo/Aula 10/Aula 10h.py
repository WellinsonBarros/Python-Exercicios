'''Rascunho'''
'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
escolha = int(input('\033[1;31;107mTente adivinhar um número que escolhi entre zero e cinco: \033[m'))
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
nlista = [n0, n1, n2, n3, n4, n5]
computador = random.choice(nlista)
print(f'\033[4;32;44mEu escolhei: {computador}\033[m')
if escolha == computador:
    print('Parabéns! Você adivinhou o número que eu escolhi!')
else:
    print('Não foi dessa vez!')
