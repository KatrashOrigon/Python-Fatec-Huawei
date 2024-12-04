"""
Reescreva o programa exercício resolvido 11.6 usando um dicionário aninhado no lugar da tupla
como valor para o dicionário Estoque.
"""

Estoque = {}
for linha in open('entrada_er_11.1.txt'):
	lst = linha.rstrip().split(';')
	cod = int(lst[0])
	qtde = int(lst[1])
	pcunit = float(lst[2])
	Estoque[cod] = {'qtde': qtde, 'pcunit': pcunit}
print('Valores carregados no dicionário')
print(Estoque)
print('\nExibição dos dados na forma de tabela')
TotGeral = 0
for cod, dados in Estoque.items():
	tot = dados['qtde'] * dados['pcunit']
	TotGeral += tot
	print(f" {cod}: {dados['qtde']:5d} x {dados['pcunit']:6.2f} = {tot:8.2f}")
print(' ' * 24, f'{TotGeral:8.2f}')
print('\nFim do Programa')
