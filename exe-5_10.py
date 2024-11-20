"""
	Escreva um programa que leia um número inteiro e informe se esse
	número é primo ou não.
"""

numero = int(input("Digite um número inteiro: "))
n = numero

while n > 2:
	n -= 1
	if numero % n == 0:
		print("Esse número NÃO é primo.")
		break
else:
	if numero != 1:
		print("Esse número é primo.")
	else:
		print("1 não é composto e nem primo.")
	
	
