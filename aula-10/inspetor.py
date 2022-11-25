import sys
import json

import tabela



def busca_calorias(nome_alimento):
	info_alimento = tabela.busca_alimento(nome_alimento)
	return info_alimento["energia"]


def total_calorias_refeicao(plano, refeicao):
	total = 0
	for alimento in plano[refeicao]:
		doses = alimento[0]
		nome = alimento[1]
		peso = alimento[2]

		kcal_100 = busca_calorias(nome)
		kcal = peso * kcal_100 / 100

		total += kcal * doses

	return total


def total_calorias(nome_plano):
	f = open(nome_plano)
	plano = json.load(f)
	f.close()

	total = 0

	refeicoes = ["pequeno-almoço", "almoço", "lanche", "jantar"]

	for refeicao in refeicoes:
		kcal = total_calorias_refeicao(plano,refeicao)
		total += kcal

	return total






# sys.argv -> Lista que contém os argumentos passados ao
# programa



nome_plano = "plano_alimentar.json"

# remover o nome do programa da lista de argumentos
args = sys.argv[1:]
n_args = len(args)

if n_args == 0:
	print("Erro: Não passou nenhum comando.")
	exit()


comando = args[0]
if comando == "info":
	print("Imprimir as informações energéticas do plano")

elif comando == "validar":
	print("Validar o plano")

elif comando == "total":
	args_total = args[1:]
	n_args_total = len(args_total)

	if n_args_total == 0:
		t = total_calorias(nome_plano)
		print("Total:", t)
	
	elif n_args_total == 1:
		argumento = args_total[0]
		if argumento == "gordura":
			print("Calcular o total de gordura (gramas)")
		elif argumento == "hidratos":
			print("Calcular o total de hidratos (gramas)")
		elif argumento == "proteina":
			print("Calcular o total de proteina (gramas)")
		else:
			print(f"Erro: Argumento inválido: {argumento}")

else:
	print("Erro: Comando inválido")






