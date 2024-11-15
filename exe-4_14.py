"""
	Em um determinado momento do dia a cotação de compra das moedas
	estrangeiras é a seguinte:
	Dólar: US$ 1.00 = R$ 4.89
	Euro: € 1.00 = R$ 5.26
	Libra Esterlina: £ 1.00 = R$ 6.17
	Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o
	valor de moeda estrangeira que se quer comprar e calcule o valor
	em reais necessários.
"""

preco_dolar = 4.89
preco_euro = 5.26
preco_libre = 6.17

tipo = input("Qual o tipo de moeda? ")
moeda = float(input("Valor a comprar? "))

if tipo == "D":
	valor = moeda * preco_dolar
elif tipo == "E":
	valor = moeda * preco_euro
elif tipo == "L":
	valor = moeda * preco_libra

print(f"Valor de compra é R$ {valor:.2f}")
