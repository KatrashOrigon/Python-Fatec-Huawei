"""
	Escreva um programa que leia um número inteiro que representa uma
	quantidade de tempo em segundos. Calcule e mostre na tela a
	quantidade de horas, minutos e segundos.
	
	
	Entrada (segundos)	Saída
	1					0 hora(s), 0 minuto(s), 1 segundo(s)
	38					0 hora(s), 0 minuto(s), 38 segundo(s)
	746					0 hora(s), 12 minuto(s), 26 segundo(s)
	4578				1 hora(s), 16 minuto(s), 18 segundo(s)
	73551				20 hora(s), 25 minuto(s), 51 segundo(s)
"""

segundo = int(input("Digite uma medida de tempo em segundos: "))

hora = segundo // 3600
minuto = segundo % 3600 // 60
segundo = segundo % 60

print("{} hora(s), {} minuto(s), {} segundo(s)".format(hora, minuto, segundo))
