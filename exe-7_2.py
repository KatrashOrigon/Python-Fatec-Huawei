"""
	Altere a solução do ex.resolvido 7.3 incluindo o comando try-except
	na leitura dos números reais para evitar a digitação incorreta dos
	valores. Quando ocorrer uma exceção uma mensagem deve ser exibida
	na tela informando esta condição.
	
	Exercício Resolvido 7.3
	Escreva um programa que leia um número inteiro N. Em seguida leia
	N números reais carregando-os em uma lista. Ao final exiba os
	elementos da lista na tela, sendo um em cada linha.
	
"""

N = int(input('Digite a quantidade: '))
L = []

for i in range(N):
	try:
		X = float(input(f' elemento {i}: '))
		L.append(X)
		print('\nResultado:')
	except ValueError:
		print("Digite somente números reais.")
		break

for valor in L:
	print(f' {valor:.2f}') # Linha alterada.
print('Fim do Programa')
