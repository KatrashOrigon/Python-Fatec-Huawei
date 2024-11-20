"""
	Escreva um programa que leia uma quantidade Qtde e mostre na tela
	os Qtde primeiros termos da sequência de Fibonacci. A sequência de
	Fibonacci é definida da seguinte forma:
	a) os dois primeiros termos da sequência são 0 e 1.
	b) Do terceiro termo em diante cada termo é a soma dos dois
	anteriores.
"""

qtde = int(input("Quantos números você deseja na sequência de Fibonacci? "))

a = 0
b = 1

while qtde > 0:
	print(a)
	a, b = b, a + b
	qtde -= 1

