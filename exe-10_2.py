"""
	Escreva um programa que permaneça em laço lendo do teclado números
	inteiros entre 1 e 9. Outros valores devem ser ignorados. Esse laço
	termina quando for digitado zero ou qualquer valor negativo.
	O objetivo deste programa é contar quantas vezes cada valor entre
	1 e 9 foi digitado. Ao término do laço de leitura o programa deve
	mostrar quais valores foram digitados e quantas vezes cada um.
	Obrigatoriamente use um dicionário.
"""

dic = {}

while True:
	numero = int(input("Digite um número: "))
	if numero < 0:
		break
	elif numero in dic:
		dic[numero] += 1
	else:
		dic[numero] = 1
			
print(dic)
