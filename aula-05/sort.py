
lista = [2,5,1,4,3] # -> [1,2,3,4,5]

lista_ordenada = []

while lista != []:
	# calcular o minimo da lista
	minimo = min(lista)

	# acrescentar o minimo à nova lista
	lista_ordenada.append(minimo)

	# eliminar o minimo da lista original
	i = lista.index(minimo)
	lista.pop(i)

	print("lista:", lista)
	print("lista ordenada:", lista_ordenada)
	print("----------------------------")

