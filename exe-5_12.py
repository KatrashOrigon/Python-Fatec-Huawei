"""
	Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida
	mostre na tela os Qtde termos da sequência de Fibonacci que sejam
	maiores que Prim.
"""

qtde = int(input("Quantos números você deseja na sequência de Fibonacci? "))
prim = int(input("A partir de qual número? "))

a = 0
b = 1

while qtde > 0:
	if a >= prim:
		print(a)
		qtde -= 1
	a, b = b, a + b
