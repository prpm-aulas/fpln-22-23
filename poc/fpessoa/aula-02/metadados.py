
titulo = input("Título: ")
autor = input("Autor: ")
data = input("Data: ")


formato = input("Formato: ")
if formato == "yaml":
	print("titulo:", titulo)
	print("autor:", autor)
	print("data:", data)
else:
	print("{")
	print('\t"titulo": "' + titulo + '",')
	print('\t"autor": "' + autor + '",')
	print('\t"data": "' + data + '"')
	print("}")