''' Crie uma tupla preenchida com os
20 primeiros colocados  da Tabela do
Campeonato Brasileiro de Futebol, na
ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Fluminense.'''
times = ('Palmeiras', 'Corinthians', 'São Paulo', 'Internacional',
         'Athletico-PR', 'Atlético-MG', 'Coritiba', 'Fluminense',
         'América-MG', 'Avaí', 'Santos', 'Bragantino', 'Ceará SC',
         'Goiás', 'Atlético-GO', 'Flamengo', 'Botafogo', 'Cuiabá',
         'Juventude', 'Fortaleza')
print('=-' * 50)
print(f'Lista de times: {times}')
print('=-' * 50)
print('Os 5 primeiros times: ', end='')
print(times[:5])
print('=-' * 50)
print('Os últimos 4 colocados: ', end='')
print(times[-4:])
print('=-' * 50)
print('Os times em ordem alfabética: ', end='')
print(sorted(times))
print('=-' * 50)
print('O Fluminense está na posição: ', end='')
print(times.index('Fluminense') + 1)
print('=-' * 50)
