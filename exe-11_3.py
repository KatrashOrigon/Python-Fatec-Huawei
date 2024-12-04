"""
	Escreva um programa que leia um número inteiro N (10 < N < 10.000)
	e grave um arquivo com N linhas com os dados listados na tabela
	abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
	caractere ';' (ponto e vírgula) como delimitador. Não é necessário
	que o arquivo esteja ordenado.
"""

from random import randint, uniform

codigos = []
teste = {}
alicotas = [7, 12, 18]
arquivo = open("Estoque.csv", 'w')
linhas = int(input("Quantas linhas deverá ter o arquivo? "))

while linhas != 0:
	cod = randint(10000, 50000)
	if not cod in codigos:
		quantidade = randint(1, 3800)
		preco = round(uniform(1.80, 435.90), 2)
		aliquota = alicotas[randint(0, 2)]
		linhas -= 1
		arquivo.write(f"{cod};{quantidade};{preco};{aliquota}\n")
arquivo.close()
