#Resolução do exercicio 028 - Curso em Vídeo

from random import randint

pc = randint(0, 5)
num = None

while (num != pc):
    num = int(input('Digite um numero de 0 a 5: '))
    if num == pc:
        print('Você acertou, parabéns!')
    else:
        print('Você errou!')


