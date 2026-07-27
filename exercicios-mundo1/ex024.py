#resolução do exercicio 024 - curso em video
#a resolução foi feita baseado no conhecimento de python pré adquirido na universidade

cidade = input('digite o nome da sua cidade: ')
cid = cidade.split()

resposta = cid[0].upper().find('SANTO')

if resposta == 0:
    print(f'a cidade de {cidade}, começa com o nome santo')
else:
    print(f'a cidade de {cidade}, não começa com o nome santo')

