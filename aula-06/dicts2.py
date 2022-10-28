
pessoa = {}

pessoa["nome"] = "João Silva"
pessoa["idade"] = 20
pessoa["naturalidade"] = "Porto"
pessoa["notas"] = {}
pessoa["notas"]["Português"] = 10
pessoa["notas"]["Matemática"] = 20
pessoa["notas"]["Inglês"] = 15

for chave in pessoa:
	print(pessoa[chave])