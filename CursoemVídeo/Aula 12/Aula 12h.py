'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
itens = ('wellinson', 'pedra', 'papel', 'tesoura')
computador = randint(1, 3)
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'Computador jogou: {itens[computador]}!')
print(f'Jogador jogou {itens[jogador]}!')
print('-=' * 11)
if computador == 1:
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence!')
    elif jogador == 3:
        print('Computador Vence')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Jogador vence!')
    else:
        print('Jogada inválida!')
elif computador == 3:
    if jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    elif jogador == 3:
        print('Empate')
    else:
        print('Jogada inválida!')
