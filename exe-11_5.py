"""
	Escreva um programa que leia o arquivo NUMEROS.TXT gerado no
	exercício proposto 11.4, colocando-os em uma lista. Ordene a
	lista usando o .sort() e grave os números ordenados no arquivo
	ORDENADOS.TXT.
"""

numeros = []

for linha in open('NUMEROS.TXT'):
	numeros.append(int(linha))

numeros.sort()
arquivo = open('ORDENADOS.TXT', 'w')

for n in numeros:
	arquivo.write(str(n) + "\n")

arquivo.close()
