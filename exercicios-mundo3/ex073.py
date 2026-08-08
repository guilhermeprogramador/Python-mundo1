#Resolução de exercicios 073 - Curso em Video

brasileirao = ('palmeiras', 'flamengo', 'atletico-pr', 'fluminense', 'bahia', 'bragantino', 'cruzeiro', 'botafogo','atletico-mg', 'corinthians', 'coritiba', 'são paulo','vitoria', 'grêmio','mirassol', 'santos', 'internacional', 'remo', 'vasco', 'chapecoense')

print(f'Os cinco primeiros colocados são {brasileirao[0:5]}\n')

print(f'Os 4 ultimos são {brasileirao[-4::]}\n')

ordem = tuple(sorted(brasileirao))
print(f'Os times em ordem alfabetica {ordem}\n')

for pos,i in enumerate(brasileirao):
    if i == 'chapecoense':
       print(f'A Chapecoense está na {pos}° posição')

    

