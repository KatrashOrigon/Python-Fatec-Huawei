"""
	Escreva um programa que leia um número inteiro Qtde e carregue uma
	lista com essa quantidade de números inteiros aleatórios entre
	1 e 100. Exiba a lista na tela. Em seguida inicie um laço que deve
	permanecer em execução enquanto um valor inteiro X for maior que
	zero. Para cada valor de X verifique se ele está na lista gerada e
	caso esteja elimine-o. Se houver mais de uma ocorrência de X na
	lista, elimine todas. Após as eliminações exiba a lista novamente.
"""

from random import randint

lista_rnd = []

qtde = int(input("Digite a quantidade: "))

for loop in range(qtde) :
	rnd = randint(1,10)
	lista_rnd.append(rnd)
print("Lista: ", lista_rnd)

indice = 1
while len(lista_rnd) > 0:
	elemento = int(input("Digite um elemento da lista para ser removido: "))
	while lista_rnd.count(elemento) > 1:
		lista_rnd.remove(elemento)
	print("Lista: {}  -  Tamanho: {}".format(lista_rnd, len(lista_rnd)))
	
			
	



	



