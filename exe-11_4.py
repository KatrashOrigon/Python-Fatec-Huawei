"""
	Escreva um programa que grave o arquivo NUMEROS.TXT com 2.000
	números, um em cada linha, gerados com a função randint() do módulo
	random no intervalo [1, 5.000].
	Altere este programa substituindo o tamanho fixo de 2.000 por uma
	quantidade de entrada a ser lida do teclado.
"""

from random import randint

linhas = int(input('Deseja gerar quantos números? '))
arquivo = open('NUMEROS.TXT', 'w')

while linhas != 0:
	arquivo.write(str(randint(1, 5000)) + "\n")
	linhas -= 1

arquivo.close()
