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

def desenha_nuvem(dicionario_ocorrencias):
	# gerar a nuvem a partir do nosso dicionario de ocorrencias
	wc = WordCloud(width=1200, height=600).generate_from_frequencies(dicionario_ocorrencias)

	# desenhar a nuvem
	image = wc.to_image()
	image.show()


# programa
d = conta("texto.txt")
print(d)
desenha_nuvem(d)






