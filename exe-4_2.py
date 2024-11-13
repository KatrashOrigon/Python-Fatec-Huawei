"""
	Classificação indicativa é um conceito que se aplica à faixa
	etária para a qual uma obra audiovisual se recomenda ou não.
	Suponha que um filme em cartaz no cinema tenha a Classificação
	de 16 anos. Escreva um programa que leia a idade de uma pessoa
	e mostre se está de acordo ou não com a classificação.
"""

numero = int(input("Digite um número: "))

if  numero % 10 == 0:
	print(f"O número {numero} é divisível por 10.")
else:
	print(f"O número {numero} não é divisível por 10.")
