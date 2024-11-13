"""
	Escreva um programa que leia o nome de um aluno e as notas obtidas
	em três avaliações. A média final é a média aritmética das três
	notas e a pessoa estará aprovada se essa média for maior ou igual
	a 7.0. Mostre na tela o nome, a média e a situação que será
	"Aprovado" ou "Reprovado".
"""

nome = input("Qual o nome do aluno? ")
nota1 = float(input("Qual valor da nota 1? "))
nota2 = float(input("Qual valor da nota 2? "))
nota3 = float(input("Qual valor da nota 3? "))
media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {nome}")
print(f"Média: {media:.1f}")

if media >= 7:
	print("Status: Aprovado")
else:
	print("Status: Reprovado")
