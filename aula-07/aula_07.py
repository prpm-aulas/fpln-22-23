# importar a função WordCloud da biblioteca wordcloud
from wordcloud import WordCloud

def limpa(texto):
	sinais = ".,!?:…"
	# sinais = [".", ",", "!", "?", ":"]

	for s in sinais:
		texto = texto.replace(s, "")

	return texto
	

def remove_stop_words(lista_palavras):
	nova_lista = []
	stop_words = ["uma", "um", "uns", "umas", "o", "a", "os", "as", "em", "e", "ou", "se", "mas", "que", "de", "da"]

	for palavra in lista_palavras:
		if palavra not in stop_words:
			nova_lista.append(palavra)

	return nova_lista


def conta(nome_ficheiro):
	# ler o ficheiro
	f = open(nome_ficheiro)
	conteudo = f.read()
	f.close()

	# limpar o conteudo
	conteudo = limpa(conteudo)

	# colocar o conteudo em minuscula
	conteudo = conteudo.lower()

	# dividir o conteudo por espaços
	palavras = conteudo.split()

	# remover as stopwords
	palavras = remove_stop_words(palavras)

	ocorrencias = {}
	for palavra in palavras:
		if palavra in ocorrencias:
			ocorrencias[palavra] += 1
		else:
			ocorrencias[palavra] = 1

	# retornar o numero total de palavras
	return ocorrencias


def dicionario_para_listas(dicionario):
	chaves = []
	valores = []
	for k in dicionario:
		chaves.append(k)
		valores.append(dicionario[k])

	return chaves, valores


def ordena_duas_listas(lista_base, outra_lista):
	lista_base_ordenada = [x for x, _ in sorted(zip(lista_base, outra_lista))]
	outra_lista_ordenada = [y for _, y in sorted(zip(lista_base, outra_lista))]

	lista_base[:] = lista_base_ordenada
	outra_lista[:] = outra_lista_ordenada


def desenha_nuvem(dicionario_ocorrencias):
	# gerar a nuvem a partir do nosso dicionario de ocorrencias
	wc = WordCloud(width=1200, height=600).generate_from_frequencies(dicionario_ocorrencias)

	# desenhar a nuvem
	image = wc.to_image()
	image.show()


def desenha_grafico_de_barras(dicionario_ocorrencias, limite):
	xx, yy = dicionario_para_listas(dicionario_ocorrencias)
	ordena_duas_listas(yy, xx)

	xx = xx[-limite:]
	yy = yy[-limite:]

	plt.bar(xx, yy)

	# plt.xticks(range(max(yy) + 1))
	plt.title("Distribuição de palavras")
	plt.xlabel("Ocorrências")
	plt.ylabel("Palavras")
	plt.show()


def desenha_bolo(dicionario_ocorrencias, limite):
	xx, yy = dicionario_para_listas(dicionario_ocorrencias)
	ordena_duas_listas(yy, xx)

	xx = xx[-limite:]
	yy = yy[-limite:]

	plt.pie(yy, labels=xx)

	plt.show()



import sys

args = sys.argv
print(args)




