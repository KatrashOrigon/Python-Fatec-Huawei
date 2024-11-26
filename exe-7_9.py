"""
	Altere o programa do Exercício Proposto 7.8 acrescentando uma
	validação adicional para garantir que a data fornecida seja válida.
	Por exemplo: a entrada 20242255 é válida segundo os critérios
	estabelecidos no enunciado 7.8. Porém, 55/22/2024 não é uma data
	válida.

	Neste exercício você deve garantir que a data seja válida
	(incluindo anos bissextos – para identificarse um ano é bissexto
	veja o Exercício Proposto 4.8).
"""

data = input("Digite uma data no formato aaaammdd: ")

meses = [31, 00, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if len(data) == 8:
	if data.isnumeric():
		dia = int(data[6:])
		mes = int(data[4:6])
		ano = int(data[:4])
		if ano > 0:
			if mes >=1 and mes <= 12:
				validado = False
				if dia >= 1 and dia <= meses[mes-1]:
					validado = True
				elif mes == 2:
					#Verifica se o ano é bissexto.
					if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
						if dia >= 1 and dia <= 29:
							validado = True
					else:
						if dia >= 1 and dia <= 28:
							validado = True
				if validado:
						print(f"A data fornecida é: {dia:02}/{mes:02}/{ano:04}")
				else:
					print("Dia inválido.")
			else:
				print("Mês inválido.")
		else:
			print("Data inválida.")
	else:
		print("Um ou mais digitos não são numéricos.")
else:
	print("Digite uma data com 8 digitos.")
