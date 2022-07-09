''' Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho
adaptável.'''
def escreva(txt):
    t = len(txt) + 4
    print(t * '~')
    print(f'{txt:^{t + 4}}')
    print(t * '~')


n1 = str(input('Digite uma frase: '))
n2 = str(input('Digite outra frase: '))
n3 = str(input('Digite outra frase: '))
escreva(n1)
escreva(n2)
escreva(n3)
