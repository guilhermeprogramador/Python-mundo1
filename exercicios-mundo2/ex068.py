#Resolução exercicio 068 - Curso em Video
import random 

i = j = 0
par_impar = ''

while True: 
    jogador = int(input('Digite um valor: ')) 
    par_impar = input('Par ou Impar? [P/I]: ').upper()
    maquina = random.randint(1, 10)
    soma = maquina + jogador

    if soma % 2 == 0: #numero final deu par
        if par_impar == 'I':
            print(f'Você perdeu, você jogou {jogador} e o computador {maquina}. O total deu {soma}, que é Par')
            break
        elif par_impar == 'P':
            print(f'Você Ganhou, você jogou {jogador} e o computador {maquina}. O total deu {soma}, que é Par')
    else:
        if par_impar == 'I': #numero final deu impar
            print(f'Você ganhou, você jogou {jogador} e o computador {maquina}. O total deu {soma}, que é Impar')
        elif par_impar == 'P':
            print(f'Você perdeu, você jogou {jogador} e o computador {maquina}. O total deu {soma}, que é Impar')
            break
    j += 1

print(f'Game Over, você venceu {j} vezes')


