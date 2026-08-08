#Resolução do exercicio 070 - Curso em Video
barato = ''  
cont = i = compra = 0
while True:
    produto = input('Digite o nome do Produto: ') 
    valor = int(input('Digite o preço do produto: '))
    
    if i == 0:
        menor = valor
        barato = produto
    else:
        if menor > valor:
            menor = valor
            barato = produto

    if valor > 1000:
        cont += 1
    
    compra += valor 
    
    resposta = input('Quer continuar, [S/N]?').upper()
    if resposta == 'N':
        break
    i += 1

print(f'o total gasto na compra foi R${compra}')
print(f'{cont} produtos custam mais de 1000 reais')
print(f'o produto mais barato e o {barato} custando R${menor}')
