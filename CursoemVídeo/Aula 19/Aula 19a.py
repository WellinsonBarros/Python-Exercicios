'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-=' * 30)
if aluno['Média'] >= 7:
    aluno['Resultado'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Resultado'] = 'Recuperação'
else:
    aluno['Resultado'] = 'Reprovado'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
