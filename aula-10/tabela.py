


def busca_alimento(nome):
	tabela_alimentos = open("tca.txt", encoding="utf-8")

	# next(f) passa à frente uma linha
	next(tabela_alimentos)

	info = {}
	for linha in tabela_alimentos:
		# strip() tira o '\n' do fim da linha
		# split('::') divide a linha pelo separador '::'
		info_lista = linha.strip().split('::')

		if info_lista[0].lower().strip() == nome.lower().strip():
			info = {
				"nome": info_lista[0],
				"energia": int(info_lista[1]),
				"gordura": float(info_lista[2]),
				"hidratos": float(info_lista[3]),
				"proteina": float(info_lista[4])
			}
			break

	tabela_alimentos.close()

	return info

