'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:
    print('=-=' * 15)
    print('''Lista de opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Escolhar a sua opção: '))
    if escolha == 1:
        print(f'A soma entre {v1} e {v2} é {v1 + v2}.')
    elif escolha == 2:
        print(f'A multiplicação entre {v1} e {v2} é {v1 * v2}.')
    elif escolha == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}!')
        elif v1 < v2:
            print(f'{v1} é menor que {v2}!')
        else:
            print('Os valores são iguais')
    elif escolha == 4:
        v1 = int(input('Digite novamente o primeiro valor: '))
        v2 = int(input('Digite novamente o segundo valor: '))
    elif escolha == 5:
        sair = True
    else:
        print('Opção inválida, tente novamente!')
from time import sleep
print('Finalizando...')
print('=-=' * 15)
sleep(2)
print('Fim do programa! Volte sempre!')
