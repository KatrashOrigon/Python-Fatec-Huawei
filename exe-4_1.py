"""
	Classificação indicativa é um conceito que se aplica à faixa etária
	para a qual uma obra audiovisual se recomenda ou não. Suponha que
	um filme em cartaz no cinema tenha a Classificação de 16 anos.
	Escreva um programa que leia a idade de uma pessoa e mostre se está
	de acordo ou não com a classificação.
"""

classificacao = 16

idade = int(input("Qual a sua idade? "))

if idade >= classificacao:
	print("Você pode assistir ao filme.")
else:
	print("Você não pode assistir ao filme.")
