"""
	Escreva um programa que leia um arquivo CSV de entrada que tenha
	dois inteiros em cada linha. O primeiro é um código de produto e o
	segundo é a quantidade vendida. O programa deve totalizar quantos
	itens foram vendidos para cada produto.
	
	Dica: use um dicionário tendo o código como chave e a quantidade
	como valor. Para cada código lido do arquivo verifique se ele já
	existe no dicionário usando o operador in. Se não existir, inclua;
	se existir some a quantidade existente com a nova quantidade lida
	do arquivo.
"""

vendidos = {}

for linha in open('entrada_ex_11.2.txt'):
	dados = linha.rstrip().split(';')
	if dados[0] in vendidos: # Busca o código do dicionário.
		vendidos[dados[0]] += int(dados[1])
	else:
		vendidos[dados[0]] = int(dados[1])

print(vendidos)






