"""
	Escreva um programa que leia um número real e mostre na tela os
	valores  de 25%, 50%, 75% do valor lido usando o formato com 3
	casas decimais mostrado abaixo:
		Exemplo Valor lido: 136.7
		Exibir 25% -> 34.175 - 50% -> 68.350 - 75% -> 102.525
"""

valor = float(input("Digite um valor: "))
p25 = valor * 0.25
p50 = valor * 0.50
p75 = valor * 0.75

print(f"25% de {valor} é {p25:.3f}")
print(f"50% de {valor} é {p50:.3f}")
print(f"75% de {valor} é {p75:.3f}")




