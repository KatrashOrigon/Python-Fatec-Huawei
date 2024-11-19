"""
	Escreva um programa que permaneça em laço lendo cadeias de
	caracteres (strings). Para cada cadeia digitada o programa deve
	exibir a cadeia seguida da quantidade de caracteres que ela contém.
	O programa termina quando for digitado "FIM" (em letras maiúsculas).
"""

while True:
	cadeia = input("Digite uma cadeia de caracteres: ")
	if cadeia == "FIM":
		break
	tamanho = len(cadeia)
	print(f"A cadeia '{cadeia}' tem {tamanho} caracteres")
