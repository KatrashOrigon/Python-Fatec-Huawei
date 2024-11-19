"""
	Escreva um programa que leia um número inteiro N. Em seguida
	calcule e mostre na tela o fatorial de N (N!).
"""

numero = int(input("Digite um número inteiro: "))
fatorial = 1

while numero >= 1:
	fatorial = fatorial * numero
	numero -= 1

print(f"O fatorial de {numero} é {fatorial}.")
