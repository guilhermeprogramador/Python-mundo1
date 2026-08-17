#Resolução do exercicio 077 - Curso em Video

palavras = ('bola', 'rua', ' comida', 'curso')
vogais = ('a', 'e', 'i', 'o', 'u')

for i in palavras:
    print(f'\nNa palavra {i} temos', end=' ')
    for c in i:
        if c in 'aeiou':
            print(f'{c}', end=' ')
