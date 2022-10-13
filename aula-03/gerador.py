
titulo = input("Insira o título: ")
autor = input("Insira o autor: ")


limite = 5
co_autores = ""
numero_co_autores = 0

while numero_co_autores < 5:
    co_autor = input(f"Insira um co-autor ({numero_co_autores}/{limite}: ")
    if co_autor == "":
        break

    co_autores = co_autores + co_autor + "; "
    numero_co_autores += 1


if numero_co_autores == limite:
    print(f"AVISO: Limite de co-autores atingido! ({numero_co_autores}/{limite})")

# Outra abordagem
# co_autor = input("Insira um co-autor: ")
# while co_autor != "":
#     co_autores = co_autores + co_autor + "; "
#     co_autor = input("Insira um co-autor: ")

data = input("Insira a data: ")

formato = input("Insira o formato: ")
ficheiro = input("Insira o nome do ficheiro: ")


if formato == "YAML" or formato == "yaml" or formato == "":
    # o formato é YAML
    extensao = "yml"
    f = open(ficheiro + "." + extensao, 'w')
    f.write("titulo: " + titulo + "\n")
    f.write("autor: " + autor + "\n")
    if co_autores != "":
        f.write("co-autores: " + co_autores + "\n")
    f.write("data: " + data + "\n")
    f.close()

elif formato == "JSON" or formato == "json":
    # o formato é JSON
    f = open(ficheiro + ".json", 'w')
    f.write("{\n")
    f.write('\t"titulo": "' + titulo + '",\n')
    f.write('\t"autor": "' + autor + '",\n')
    if co_autores != "":
        f.write('\t"co-autores": "' + co_autores + '",\n')
    f.write('\t"data": "' + data + '"\n')
    f.write("}\n")
    f.close()

else:
    print("ERRO: Formato Inválido.")
    print("Não foi possível gerar o resultado.")


