'''Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    x = date.today().year
    idade = x - ano
    if idade < 18:
        return f'Com {idade} anos: Voto NEGADO'
    elif 16 >= idade < 18 or idade > 70:
        return f'Com {idade} anos: Voto OPICIONAL!'
    else:
        return f'Com {idade} anos: Voto OBRIGATÓRIO!'


print('-' * 30)
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))
print('-' * 30)
