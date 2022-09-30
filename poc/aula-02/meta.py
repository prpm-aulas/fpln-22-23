
titulo = input("Insira o título: ")
autor = input("Insira o autor: ")
ano = input("Insira o ano: ")
formato = input("Insira o formato: ")
nome_ficheiro = input("Insira o nome do ficheiro: ")

if formato == "YAML":

	extensao = ".yml"

	f = open(nome_ficheiro + extensao, "w")

	f.write("titulo: " + titulo)
	f.write("autor: " + autor)
	f.write("ano: " + ano)

	f.close()

else:
	extensao = ".json"

	f = open(nome_ficheiro + extensao)

	f.write("{\n")
	f.write("\t\"titulo\": \"" + titulo + "\",\n")
	f.write("\t\"autor\": \"" + autor + "\",\n")
	f.write("\t\"ano\": \"" + ano + "\"\n")
	f.write("}\n")

	f.close()
