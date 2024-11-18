"""
	Escreva um programa que leia um número N e em seguida exiba na
	tela todos os números divisíveis por 7 entre 1 e N (inclusive).
"""

numero = int(input("Digite um número: "))
n = 1

while n <= numero:
	if n % 7 == 0:
		print(f"{n} é divisível po 7.")
	n += 1

		
