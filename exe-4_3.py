"""
	Uma empresa financeira concede empréstimos a pessoas físicas
	quando o valor da parcela é menor que 8% do salário da pessoa.
	Escreva um programa que leia dois números reais: o valor do
	salário e o valor da parcela e informe se o empréstimo será
	concedido ou não.
"""

salario = float(input("Qual valor do salário (R$)? "))
parcela = float(input("Qual valor da parcela (R$)? "))

if  parcela < salario * 0.08:
	print(f"Empréstimo concedido.")
else:
	print(f"Empréstimo negado.")
