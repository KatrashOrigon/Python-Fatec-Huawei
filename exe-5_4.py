"""
	Escreva um programa que leia dois números inteiros: LMin e LMax.
	Em seguida exiba na tela todos os valores dentro do intervalo
	fechado [LMin, LMax].
"""
LMin = int(input("Digite LMin: "))
LMax = int(input("Digite LMax: "))

while LMin <= LMax:
	print(LMin)
	LMin += 1
