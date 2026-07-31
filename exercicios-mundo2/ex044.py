#Resolução do exercicio 044 - Curso em Video

produto = int(input('Digite o valor do produto: '))

pagamento = int(input(' Cheque ou dinheiro, digite 1:\n Cartão digite 2:\n 2x no Cartão digite 3:\n 3x ou mais no cartão digite 4: '))

if pagamento == 1:
    print(f'O valor do produto será {produto - (produto * 10 / 100)}')
elif pagamento == 2:
    print(f'O valor do produto será {produto - (produto * 5 / 100)}')
elif pagamento == 3:
    print(f'O valor do produto será {produto}')
else:
    print(f'O valor do produto será {produto + (produto * 20 / 100)}')




