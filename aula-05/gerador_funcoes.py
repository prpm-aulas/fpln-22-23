def ordenar(lista_nao_ordenada):
    lista_ordenada = []

    while lista_nao_ordenada != []:
        # calcular o minimo da lista
        minimo = min(lista_nao_ordenada)

        # acrescentar o minimo à nova lista
        lista_ordenada.append(minimo)

        # eliminar o minimo da lista original
        i = lista_nao_ordenada.index(minimo)
        lista_nao_ordenada.pop(i)

    return lista_ordenada


def insere_co_autores():
    limite = 5
    lista_co_autores = []
    numero_co_autores = 0

    while numero_co_autores < limite:
        co_autor = input(f"Insira um co-autor ({numero_co_autores}/{limite}): ")
        if co_autor == "":
            break

        if co_autor in lista_co_autores:
            print(f'AVISO: co-autor "{co_autor}" já existe!')
            continue # proxima iteração

        lista_co_autores.append(co_autor)
        numero_co_autores += 1


    if numero_co_autores == limite:
        print(f"AVISO: Limite de co-autores atingido! ({numero_co_autores}/{limite})")

    return lista_co_autores


def write_yaml(ficheiro_arg, titulo_arg, autor_arg, co_autores_arg, data_arg):
    extensao = "yml"
    f = open(ficheiro_arg + "." + extensao, 'w')
    f.write("titulo: " + titulo_arg + "\n")
    f.write("autor: " + autor_arg + "\n")

    if co_autores_arg != []:
        f.write("co-autores:\n")
        for co_autor in co_autores_arg:
            f.write(f"\t- {co_autor}\n")

    f.write("data: " + data_arg + "\n")
    f.close()


def write_json(ficheiro_arg, titulo_arg, autor_arg, co_autores_arg, data_arg):
    f = open(ficheiro_arg + ".json", 'w')
    f.write("{\n")
    f.write('\t"titulo": "' + titulo_arg + '",\n')
    f.write('\t"autor": "' + autor_arg + '",\n')

    if co_autores_arg != []:
        f.write('\t"co_autores": [\n')

        i = 0
        while i < len(co_autores_arg) - 1:
            f.write(f'\t\t"{co_autores_arg[i]}",\n')
            i += 1

        f.write(f'\t\t"{co_autores_arg[i]}"\n')
        f.write('\t],\n')

    f.write('\t"data": "' + data_arg + '"\n')
    f.write("}\n")
    f.close()


def print_erro():
    print("ERRO: Formato Inválido.")
    print("Não foi possível gerar o resultado.")
