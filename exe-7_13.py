"""
	Escreva um programa que permaneça em laço lendo três dados de um
	produto: o código (int), o preço de compra (float) e o preço de
	venda(float). Com esses dados forme uma tupla e armazene-a em uma
	lista. Os três dados devem ser lidos em uma única linha separados
	por espaço em branco. O laço termina quando forem digitados três
	zeros: 0 0 0
	Em seguida, para todas as tuplas presentes na lista, exiba o código
	do produto e a margem bruta de lucro do produto em porcentagem e
	com uma casa decimal. A margem bruta de lucro é calculada com
	a expressão:
	
	MargemBruta = ((venda/compra)-1)*100%
"""

dados = ""
lista = []

dados = input("Digite as informações do produto: ")
while dados != "0 0 0":
	fatias = dados.split(" ")
	#print(fatias)
	lista.append((fatias[0], float(fatias[1]), float(fatias[2])))
	dados = input("Digite as informações do produto: ")

for item in lista:
	lucro = ((item[2]/item[1])-1)*100
	print("Código do produto {} - Lucro {:.1f}%".format(item[0], lucro))
