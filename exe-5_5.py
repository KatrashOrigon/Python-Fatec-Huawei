"""
	Escreva um programa que leia três números inteiros: LMin, LMax e D.
	Em seguida exiba na tela todos os valores divisíveis por D que
	estão dentro do intervalo fechado [LMin, LMax].
"""
LMin = int(input("Digite LMin: "))
LMax = int(input("Digite LMax: "))
D = int(input("Digite D: "))

while LMin <= LMax:
	if LMin % D == 0:
		print(f"{LMin} é divisível por {D}.")
	LMin += 1
