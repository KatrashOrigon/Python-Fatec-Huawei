"""
	Escreva um programa para uma fábrica de calçados que leia o código
	LL de um calçado, que é um número inteiro com 2 dígitos. Exiba
	na tela a linha do calçado, conforme a tabela a seguir. Se o
	número fornecido não estiver na tabela, deve-se exibir a
	mensagem "Código inválido".
"""

ll = int(input("Código do calçado: "))

if ll == 16:
	print("Bebê")
elif ll == 23:
	print("Infantil Feminino")
elif ll == 25:
	print("Infantil Masculino")
elif ll == 29:
	print("Infantil Esportivo")
elif ll == 42:
	print("Masculino Formal")
elif ll == 43:
	print("Masculino Casual")
elif ll == 49:
	print("Masculino Esportivo")
elif ll == 52:
	print("Feminino Formal Salto Baixo")
elif ll == 53:
	print("Feminino Formal Salto Alto")
elif ll == 55:
	print("Feminino Casual Salto Baixo")
elif ll == 56:
	print("Feminino Casual Salto Alto")
elif ll == 59:
	print("Feminino Esportivo")
else:
	print("Código Inválido")
