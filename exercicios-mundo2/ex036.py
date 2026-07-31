#Resolução do ex036 - Curso em Video 

casa = float(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
salario = float(input('Qual o seu salario? '))

prestacao = (casa / (anos * 12))

execao = salario * 30 / 100

if execao > prestacao:
    print('Seu emprestimo está aprovado, você ira comprar')
else:
    print('Seu emprestimo está reprovado, você não pode comprar')




