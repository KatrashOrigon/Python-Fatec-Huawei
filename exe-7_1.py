"""
	Altere a solução do ex.resolvido 7.3 para exibir os números reais
	da lista com duas casas decimais.
	
	Exercício Resolvido 7.3
	Escreva um programa que leia um número inteiro N. Em seguida leia
	N números reais carregando-os em uma lista. Ao final exiba os
	elementos da lista na tela, sendo um em cada linha.
	
"""

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
	X = float(input(f' elemento {i}: '))
	L.append(X)
	print('\nResultado:')
for valor in L:
	print(f' {valor:.2f}') # Linha alterada.
print('Fim do Programa')
