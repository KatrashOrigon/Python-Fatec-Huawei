"""
	Uma empresa comercial trabalha com 3 vendedores externos e os
	remunera com R$ 1200,00 fixos mais comissão de 6% sobre o valor
	total vendido no mês. Escreva um programa que leia o nome e o
	total vendido pelos 3 vendedores, calcule e exiba na tela a
	mensagem de saída conforme o exemplo a seguir. Exiba os valores
	numéricos com duas casas decimais.
	
	Exemplo
	
		+ vendedor José Carlos Santos vendeu R$ 43759.35 e faz jus a
			uma comissão de R$ 3825.56
		+ vendedor Manoel Guimarães vendeu R$ 61417.81 e faz jus a
			uma comissão de R$ 4885.07
		+ vendedor Plínio Pereira vendeu R$ 39336.87 e faz jus a
			uma comissão de R$ 3560.21
"""

nome = input("Qual o nome do vendedor? ")
vendido = float(input("Qual o valor das vendas? "))
comissao = 1200 + vendido * 0.06

print(f"O vendedor {nome} vendeu R${vendido} e faz jus a uma comissão de R${comissao: .2f}")
