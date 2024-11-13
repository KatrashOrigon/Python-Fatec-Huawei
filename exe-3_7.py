"""
	Quando uma pessoa ou uma empresa realiza um investimento espera-se
	um retorno positivo (lucro), embora também possa ocorrer um retorno
	negativo (prejuízo). Uma forma inicial de avaliar o retorno é
	conhecida com Retorno sobre Investimento (ou ROI, uma sigla em
	inglês). Cálculo do ROI:
	
	ROI = ((Rec - (Cust + Inv)) * 100) / (Cust + Inv)
	
	Escreva um programa que leia 3 dados de entrada reais:
	Investimento, Custos e Receita, calcule o ROI usando a fórmula
	acima e exiba o resultado com uma casa decimal no formato mostrado
	abaixo.
	
	Testes
	
	Investimento	Custos	Receita		ROI
	22500.00		535.83	25419.61	10.3%
	15000.00		419.35	14403.44	-6.6%
	18000.00		837.40	19132.28	1.6%
"""


inv = float(input("Qual o investimento? "))
cus = float(input("Qual o custo? "))
rec = float(input("Qual a receita? "))

roi = ((rec - (cus + inv)) / (cus + inv)) * 100

print(F"ROI = {roi: .1f}%")
