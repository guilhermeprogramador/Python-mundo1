#Resolução de exercicio 063 - Curso em Video

n = int(input('Digite quantos elementos da sequencia de fibonacci você quer: '))

i = 0

j = 0
p = 1

while i != n:
    seq = j + p
    j = p 
    p = seq
    print(seq)
    
    i += 1
