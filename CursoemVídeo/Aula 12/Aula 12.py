'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('-' * 52)
print('Bem-vindo a fundação de empréstimos para residências')
print('-' * 52)
vc = float(input('Informe o valor da casa: '))
s = float(input('Informe o seu salário: '))
anos = float(input('Em quantos anos você deseja pagar o empréstimo: '))
parcela = (s * 1.3 - s) * 12
if vc >= parcela * anos:
    print('Parabéns, aprovamos o seu empréstimo!')
else:
    print('Infelizmente o seu empréstimo foi negado!')
print('Tenha um bom dia!')
