"""
	Escreva um programa que leia um número inteiro nA e gere uma
	lista A com nA valores inteiros aleatórios, não repetidos e
	situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
	Em seguida leia outro inteiro nB e gere a lista B usando as mesmas
	regras aplicadas à lista A. Mostre-a na tela também em ordem
	crescente.
	Crie e exiba uma lista contendo a união das listas A e B, sem
	conter valores repetidos. Mostre a lista resultante e a quantidade
	de elementos dela.
"""

from random import randint

A = []
B = []

nA = int(input("Quantidade de valores para a primeira lista: "))
loop = nA

while loop >=1:
	rnd = randint(1, 100)
	if not rnd in A:
		A.append(rnd)
		loop -= 1
A.sort()
print(f"\nLista A =", A)

nB = int(input("\nQuantidade de valores para a segunda lista: "))
loop = nB

while loop >=1:
	rnd = randint(1, 100)
	if not rnd in B:
		B.append(rnd)
		loop -= 1
B.sort()
print(f"\nListaBA =", B)

uniao = A + B

for elemento in uniao:
	if uniao.count(elemento) > 1:
		uniao.remove(elemento)
uniao.sort()
print("\nUnião de A e B: ", uniao)
print("\nTamnho de A e B: ", len(uniao))
