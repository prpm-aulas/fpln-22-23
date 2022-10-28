
pessoa = {
	"nome": "João Silva",
	"idade": 20,
	"naturalidade": "Porto",
	"altura": 1.80,
	"casado": True,
	"notas": {
		"Português": 10,
		"Matemática": 20,
		"Inglês": 15
	}
}

# aceder a elemento
print(pessoa["nome"])

# alterar elemento
pessoa["altura"] = 1.90
pessoa["idade"] += 1

# adicionar elemento
pessoa["universidade"] = "UMinho"

# ver se chave existe
if "casado" in pessoa:
	print("a chave 'casado' existe")
else:
	print("a chave 'casado' não existe")

if "sexo" in pessoa:
	print("a chave 'sexo' existe")
else:
	print("a chave 'sexo' não existe")

print("\n")

# eliminar elemento
del pessoa["casado"]


# percorrer um dicionario
for chave in pessoa:
	# imprimir chave
	print("Chave:", chave)

	# imprimir valor
	print("Valor:", pessoa[chave])

	print("-------------")


