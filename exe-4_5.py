"""
	Escreva um programa que leia a idade de uma pessoa e indique qual
	sua classe eleitoral:
		a) menor que 16 anos -> não eleitor
		b) entre 18 completos e 65 anos incompletos -> eleitor 
			obrigatório
		c) entre 16 anos completos e 18 anos incompletos ou 65 anos
			completos -> eleitor facultativo
"""

idade = int(input("Qual a idade do eleitor? "))

if idade < 16:
	print("Não eleitor")
elif idade >= 18 and idade < 65:
	print("Eleitor obrigatório")
else:
	print("Eleitor facultativo")
