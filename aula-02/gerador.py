
titulo = input("Insira o título: ")
autor = input("Insira o autor: ")
data = input("Insira a data: ")

formato = input("Insira o formato: ")
ficheiro = input("Insira o nome do ficheiro: ")


if formato == "YAML" or formato == "yaml" or formato == "":
    # o formato é YAML
    extensao = "yml"
    f = open(ficheiro + "." + extensao, 'w')
    f.write("titulo: " + titulo + "\n")
    f.write("autor: " + autor + "\n")
    f.write("data: " + data + "\n")
    f.close()

    # print("titulo: " + titulo)
    # print("autor: " + autor)
    # print("data: " + data)
elif formato == "JSON" or formato == "json":
    # o formato é JSON
    f = open(ficheiro + ".json", 'w')
    f.write("{\n")
    f.write('\t"titulo": "' + titulo + '",\n')
    f.write('\t"autor": "' + autor + '",\n')
    f.write('\t"data": "' + data + '"\n')
    f.write("}\n")
    f.close()

    # print("{")
    # print('\t"titulo": "' + titulo + '",')
    # print('\t"autor": "' + autor + '",')
    # print('\t"data": "' + data + '"')
    # print("}")
else:
    print("ERRO: Formato Inválido.")
    print("Não foi possível gerar o resultado.")


