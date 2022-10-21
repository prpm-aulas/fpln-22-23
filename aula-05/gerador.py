from gerador_funcoes import ordenar, insere_co_autores, write_yaml, write_json, print_erro

titulo = input("Insira o título: ")
autor = input("Insira o autor: ")

# lista de co_autores
co_autores = insere_co_autores()

# ordenar a lista
co_autores = ordenar(co_autores)

data = input("Insira a data: ")
formato = input("Insira o formato: ")
ficheiro = input("Insira o nome do ficheiro: ")


if formato == "YAML" or formato == "yaml" or formato == "":
    write_yaml(ficheiro, titulo, autor, co_autores, data)
elif formato == "JSON" or formato == "json":
    write_json(ficheiro, titulo, autor, co_autores, data)
else:
    print_erro()
