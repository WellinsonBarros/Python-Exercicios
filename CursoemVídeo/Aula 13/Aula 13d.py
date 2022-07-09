'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''
t = int(input('Digite um número para obtenção da tabuada: '))
for x in range(0, 11):
    print(f'{t} x {x:2} = {t * x}')
