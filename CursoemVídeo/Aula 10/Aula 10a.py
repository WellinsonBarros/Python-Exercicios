'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
v = float(input('Informe a velocidade do veículo: '))
if v > 80:
    print('Multado! Você excedeu o limite de velocidade de 80km')
    multa = (v - 80) * 7
    print(f'Você deve pagar uma multa de {multa} reais')
print('Dirija com segurança!')
