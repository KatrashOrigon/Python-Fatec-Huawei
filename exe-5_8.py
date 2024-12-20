"""
	Uma indústria metalúrgica adota um código de produto com o seguinte
	formato TMMM, onde T indica o uso do produto, sendo 1 para
	residencial; 2 para industrial e MMM indica qual é o produto.
	Escreva um programa que permaneça em laço até que seja digitado 0.
	Em cada repetição leia duas informações:
		a) O código do produto;
		b) A quantidade vendida desse produto.

	O programa deve totalizar separadamente e exibir na tela as
	quantidades de produtos residenciais e industriais vendidos. Se o
	dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido"
	e a quantidade deve ser ignorada.
"""

residencial = 0
industrial = 0

while True:
	codigo = input("Digite o código do produto: ")
	if codigo == "0":
		break
	quantidade = int(input("Quantidade: "))
	if codigo[0] == "1":
		residencial += quantidade
	elif codigo[0] == "2":
		industrial += quantidade
	else:
		print("Tipo Inválido.")
print(f"Total Residencial: {residencial}")
print(f"Total Industrial: {industrial}")
