"""
	Escreva um programa que leia e armazene em um dicionário os
	seguintes dados dos seus contatos: nome, número celular, email e
	data de aniversário.
	A chave deve o nome. O valor deve ser um dicionário aninhado
	contendo os demais dados. Se o nome já existir no dicionário o
	programa deve perguntar se o usuário deseja alterar o cadastro.
	Ao digitar um string vazio para o nome, o programa interrompe a
	leitura. Antes de encerrar o programa apresente os dados em um
	formato de tabela.
"""

agenda = {}

while True:
	nome = input("Nome do Contato: ")
	if nome == "":
		break
	telefone = input("Telefone: ")
	email = input("E-mail: ")
	data = input("Aniversário: ")
	if nome in agenda:
		resposta = input("Deseja atualizar o cadastro? (s/n) ")
		if resposta == "N":
			continue
	agenda[nome] = {
		'telefone': telefone,
		'email': email,
		'data': data}
	print("\n")

print('\n{:30}{:15}{:30}{:10}'.format('Nome', 'Telefone', 'email', 'Aniversário'))
for nome, dados in agenda.items():
	print('{:30}{:15}{:30}{:10}'.format(
		nome,
		dados['telefone'],
		dados['email'],
		dados['data'])
	)
