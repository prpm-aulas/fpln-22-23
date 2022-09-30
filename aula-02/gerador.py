
titulo = input("Insira o título: ")
autor = input("Insira o autor: ")
data = input("Insira a data: ")

formato = input("Insira o formato: ")

if formato == "YAML" or formato == "yaml" or formato == "":
    # o formato é YAML
    print("titulo: " + titulo)
    print("autor: " + autor)
    print("data: " + data)
elif formato == "JSON" or formato == "json":
    # o formato é JSON
    print("{")
    print('\t"titulo": "' + titulo + '",')
    print('\t"autor": "' + autor + '",')
    print('\t"data": "' + data + '"')
    print("}")
else:
    print("ERRO: Formato Inválido.")
    print("Não foi possível gerar o resultado.")


