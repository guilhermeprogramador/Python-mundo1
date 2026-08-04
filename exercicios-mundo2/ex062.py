#Resolução de exercicios 061 - Curso em Video
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

i = 0 

while i != 10:
    print(termo)
    termo += razao          
    i += 1

x = int(input('digite quantos termos a mais você quer: '))

while x != 0:
    j = 0
    while j != x:
        print(termo)
        termo += razao
        j += 1

    x = int(input('Digite quantos termos a mais você quer: '))
    
    

print('Fim programa')
