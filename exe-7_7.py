"""
	Altere a solução ex.resolvido 7.6 de modo que todos os valores
	repetidos sejam incluídos em uma segunda lista. Ao final exiba essa
	segunda lista juntamente com seu tamanho.
"""

LstValores = []
LstRepetidos = []
valor = 1

while valor != 0:
	valor = int(input('Digite um inteiro: '))
	if valor not in LstValores:
		LstValores.append(valor)
	else:
		LstRepetidos.append(valor)

print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print(LstRepetidos)
print(f'\nA lista dos repetidos contém {len(LstRepetidos)} elementos')
print('Fim do Programa')
