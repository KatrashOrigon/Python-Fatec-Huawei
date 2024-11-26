"""
	Altere a solução do ex.resolvido 7.3 para exibir os resultados em
	ordem inversa à ordem de leitura.
"""

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
	X = float(input(f' elemento {i}: '))
	L.append(X)
	print('\nResultado:')
L.reverse()
for valor in L:
	print(f' {valor}')
print('Fim do Programa')
