"""
	Nas eleições municipais os municípios com 200 mil eleitores ou
	mais tem segundo turno caso o primeiro colocado não tenha mais do
	que 50% dos votos. Escreva um programa que leia o nome do
	município, a quantidade de eleitores e a quantidade de votos do
	candidato mais votado e informe se haverá segundo turno ou não.
"""

cidade = input("Qual o nome do município? ")
eleitores = int(input("Qual a quantidade de eleitores? "))
votos = int(input("Qual a quantidade de votos do primeiro colocado? "))

if eleitores >= 200000:
	if votos > eleitores * 0.5:
		print("Este município não terá segundo turno.")
	else:
		print("Este município terá segundo turno.")
else:
	print("Este município não terá segundo turno.")
