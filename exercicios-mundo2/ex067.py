#Resolução exercicio 067 - Curso em Video
i = num = 0

while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        break
    for i in range(0, 11):
        mult = i * num
        print(f'{num} x {i} = {mult}')

print(f'Programa encerrado, você digitou {num}')

