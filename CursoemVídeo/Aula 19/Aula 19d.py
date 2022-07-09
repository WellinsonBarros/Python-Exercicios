'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato.'''
dic = {}
lista = []
listasoma = []
soma = 0
dic['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0, partidas):
    lista.append(int(input(f'{"Quantos":>10} gols na partida {c + 1}? ')))
    listasoma = lista[:]
    soma += listasoma[0]
    listasoma.clear()
dic['gols'] = lista
dic['total'] = soma
print('-=' * 25)
print(dic)
print('-=' * 25)
for k, w in dic.items():
    print(f'O campo {k} tem o valor {w}')
print('-=' * 25)
print(f'O jogador {dic["nome"]} jogou {partidas}.')
for x, y in enumerate(lista):
    print(f'{"=>":>5} Na partida {x + 1}, fez {y} gols.')
print(f'Foi um tolta de {soma} gols.')
