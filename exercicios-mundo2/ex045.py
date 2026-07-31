#Resolução do exercicio 045 - Curso em Video
import random 

jogador = int(input('PEDRA, DIGITE 1:\nTESOURA, DIGITE 2:\nPAPEL, DIGITE 3:\nESCOLHA SUA OPÇÃO: '))
maquina = random.randint(1, 3)

#print(maquina) e apenas para ver qual o valor escolhido pelo computador
print(maquina)

if jogador == 1 and maquina == 1:
    print('Deu empate, ambos jogadores escolheram pedra')
elif jogador == 2 and maquina == 2:
    print('Deu empate, ambos jogadores escolheram tesoura')
elif jogador == 3 and maquina == 3:
    print('Deu empate, ambos jogadores escolheram papel')
elif jogador == 1 and maquina == 2:
    print('Jogador venceu, jogou pedra e a maquina jogou tesoura')
elif jogador == 2 and maquina == 3:
    print('Jogador venceu, jogou tesoura e a maquina jogou papel')
elif jogador == 3 and maquina == 1:
    print('Jogador venceu, jogou papel e maquina jogou pedra')
elif maquina == 1 and jogador == 2:
    print('Maquina venceu, maquina jogou pedra e jogador jogou tesoura')
elif maquina == 2 and jogador == 3:
    print('Maquina vneceu, maquina jogou tesoura e jogador jogou papel')
elif maquina == 3 and jogador == 1:
    print('Maquina venceu, maquina jogou papel e jogador jogou pedra')


