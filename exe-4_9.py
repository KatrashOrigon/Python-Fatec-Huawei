"""
	Escreva um programa que leia 3 números inteiros e mostre na tela
	uma das seguintes opções:
		a) "Os três valores são iguais."
		b) "Há dois valores iguais e um diferente." 
		c) "Os três valores são diferentes."
"""

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b and b == c:
	print("Os três valores são iguais.")
elif a == b or b == c:
	print("Há dois valores iguais e um diferente.")
else:
	print("Os três valores são diferentes.")
