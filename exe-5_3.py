"""
	Escreva um programa que obrigatoriamente leia um inteiro que esteja
	no intervalo fechado [100, 200]. Se o valor fornecido estiver fora
	do intervalo o programa deve avisar que o valor é inválido e
	permanecer no laço. Quando um valor válido for fornecido o programa
	deve informar que o valor foi aceito e terminar.
"""

while True:
	numero = int(input("Digite um valor no intervalo [100,200]: "))
	if numero >= 100 and numero <= 200:
		print("Valor válido.")
		break
	else:
		print("Valor inválido.")	


