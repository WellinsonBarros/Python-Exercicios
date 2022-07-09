'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Digite o seu sexo: ')).strip().lower()
while sexo not in ['f', 'm', 'masculino', 'feminino']:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().lower()[0]
if sexo == 'f':
    print('O seu sexo feminino foi registrado com sucesso!')
elif sexo == 'm':
    print('O seu sexo masculino foi registrado com sucesso!')
else:
    print(f'O seu sexo {sexo} foi registrado com sucesso!')
