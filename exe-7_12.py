"""
	Escreva um programa que permaneça em laço de modo que em cada
	repetição seja lido e armazenado em uma lista o nome de uma pessoa.
	O laço termina quando o usuário entrar com um string vazio.
	Exiba na tela a lista de nomes em ordem alfabética e precedida de
	um número de ordem começando em 1.
"""

lista = []
nome = "a"

while nome != "":
	nome = input("Digite um nome: ")
	if nome != "":
		lista.append(nome)

lista.sort()
indice = 0
for nome in lista:
	indice += 1
	print(indice, nome)
