#resolução do exercicio 026 - Curso em video
frase = input('digite a sua frase: ').upper()

cont = frase.count('A')

print(f'A letra A aparece {cont} vezes')
print(f'A primeiro letra A aparece na posição: {frase.find('A')}')
print(f'A ultima letra A aparece na posição: {frase.rfind('A')}')

