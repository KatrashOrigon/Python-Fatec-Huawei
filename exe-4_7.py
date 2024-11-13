"""
	Em Albalândia mulheres e homens podem servir o exército do país.
	O serviço é opcional e é muito comum que as pessoas se apresentem
	para o serviço em algum momento da vida. Existe uma única restrição
	para ingresso que é a idade da pessoa: para mulheres a idade aceita
	é entre 21 e 34 anos; para homens a idade aceita é entre 18 e 39
	anos. Escreva um programa que leia três dados de entrada: nome da
	pessoa, idade e sexo e informe se a pessoa será aceita ou não para
	o serviço.
	Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou
	'F' para feminino e 'm' ou 'M' para masculino, qualquer coisa
	diferente deve ser informado como inválido.
"""

nome = input("Qual o nome do candidato(a)? ")
idade = int(input("Qual a idade do candidato(a)? "))
sexo = input("Qual a sexo do candidato(a)? ")

if sexo == "f" or sexo == "F":
	if idade >= 21 and idade <= 34:
		print("Candidata aceita no serviço militar.")
	else:
		print("Candidata não aceita no serviço militar.")
elif sexo == "m" or sexo == "M":
	if idade >= 18 and idade <= 39:
		print("Candidato aceito no serviço militar.")
	else:
		print("Candidato não aceito no serviço militar.")
else:
	print("Inválido.")
	
