co_autores = ["Pedro", "Sara", "João", "Carlos"]

# tamanho da lista
tamanho = len(co_autores)
print("Tamanho da lista: " + str(tamanho))

# aceder a um elemento
print(co_autores[0])
print(co_autores[-1])

# acrescentar um elemento
print(co_autores)
co_autores.append("Diogo")
co_autores.append("Paula")
print(co_autores)

# juntar listas
disciplinas_1 = ["Português", "Inglês"]
disciplinas_2 = ["Matemática", "Filosofia", "Biologia"]
displicinas = disciplinas_2 + disciplinas_1
# print(displicinas)

# apagar elementos
co_autores.pop(2)
print(co_autores)

# modificar elementos
co_autores[0] = "José"
print(co_autores)

# testar se um elemento pertence a uma lista
if "Sara" in co_autores:
	print(True)
else:
	print(False)

# percorrer os elementos da lista (while)
i = 0
while i < len(co_autores):
	valor = co_autores[i]
	print(f"{i}: {valor}")
	i += 1

# percorrer os elementos da lista (for)
for elemento in co_autores:
	print(elemento)

print("\n\n\n\n\n\n\n")

print(co_autores)

# testar manualmente se um elemento pertence a uma lista
nome = "Diogo"
pertence = False
for co_autor in co_autores:
	if co_autor == nome:
		pertence = True
		break

if pertence == True:
	print(f"{nome} pertence à lista")
else:
	print(f"{nome} não pertence à lista")

