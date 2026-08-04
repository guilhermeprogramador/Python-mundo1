#Resolução do exercicio 058 - Curso em Video
from random import randint

num = randint(0, 10)

i = None

while i != num:
    i = int(input('Digite um numero: '))
    
    if i == num:
        print('Você acertou!')
    else:
        print('Você errou')

print('fim do jogo')
