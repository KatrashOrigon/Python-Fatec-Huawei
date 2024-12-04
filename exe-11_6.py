"""
	Escreva um programa que leia um arquivo de entrada contendo números
	inteiros, sendo um por linha, e os coloque em uma lista. Em seguida
	pense em alguma forma de remover os valores repetidos, deixando
	apenas uma cópia de cada valor. A lista resultante após a
	eliminação dos repetidos, deve ser ordenada e salva no arquivo
	UNICOS.TXT, um inteiro por linha.
"""

lista = []

for linha in open('NUMEROS.TXT'):
	lista.append(int(linha))

lista.sort()
lista_unicos = []

arquivo = open('UNICOS.TXT', 'w')
for n in lista:
	if not n in lista_unicos:
		lista_unicos.append(n)
		arquivo.write(str(n) + '\n')

arquivo.close()



