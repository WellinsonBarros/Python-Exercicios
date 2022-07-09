'''Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''
from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
escolha = randint(0, 10)
cont = 0
acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    cont += 1
    if palpite == escolha:
        acertou = True
    else:
        if palpite < escolha:
            print('Mais!')
        elif palpite > escolha:
            print('Menos!')

print(f'Eu havia escolhido {escolha}')
print(f'Parabéns, você adivinhou! Porém você errou {cont} vezes!')
