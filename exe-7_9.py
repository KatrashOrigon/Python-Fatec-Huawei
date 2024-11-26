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

meses30 = [1, 3, 5, 7, 8, 10, 12]
meses31 = [4, 6, 9, 7, 11]

if len(data) == 8:
	if data.isnumeric():
		dia = int(data[6:])
		mes = int(data[4:6])
		ano = int(data[:4])
		if ano > 0:
			if mes >=1 and mes <= 12:
				validado = False
				if (dia >= 1 and dia <= 30) and (dia in meses30):
					print("ok")
				else:
					print("Data inválida. Este mês deve ter 30 dias.")
			else:
				print("O mês deve ser um valor entre 1 e 12.")
		else:
			print("O ano deve ser maior que zero.")
	else:
		print("Um ou mais digitos não são numéricos.")
else:
	print("Digite uma data com 8 digitos.")
