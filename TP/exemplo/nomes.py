import sys

def adicionar_nome(nome):
    """
    Estratégia:
        1. Ler o conteúdo do ficheiro 'nomes.txt', e guardar os nomes
        numa lista
        2. Adicionar o novo nome à lista
        3. Voltar a escrever todos os nomes da lista, no ficheiro 'nomes.txt'
    """
    # Passo 1
    f = open("nomes.txt")
    lista = f.readlines()
    f.close()

    # Passo 2
    lista.append(nome)

    # Passo 3
    f = open("nomes.txt", mode='w')
    for nome in lista:
        f.write(nome.strip() + '\n')
    f.close()


def remover_nome(nome):
    """
    Estratégia:
        1. Ler o conteúdo do ficheiro 'nomes.txt', e guardar os nomes
        numa lista
        2. Remover o nome da lista, apenas se ele existir
        3. Voltar a escrever todos os nomes da lista, no ficheiro 'nomes.txt'
    """

    # Passo 1
    f = open("nomes.txt")
    lista = f.readlines()
    f.close()

    # Passo 2
    if nome + '\n' in lista:
        lista.remove(nome + '\n')

    # Passo 3
    f = open("nomes.txt", mode='w')
    for nome in lista:
        f.write(nome.strip() + '\n')

    f.close()


# guardar a lista de argumentos
argumentos = sys.argv[1:]
print("argumentos:", argumentos)

# extrair o comando da lista de argumentos
comando = argumentos[0]
print("comando:", comando)

if comando == 'adicionar':
    nome_inserido = input("Insira um nome: ")
    adicionar_nome(nome_inserido)

elif comando == 'remover':
    if len(argumentos) == 2:
        nome = argumentos[1]
        remover_nome(nome)
    else:
        print("Erro: O comando 'remover' tem de ter 1 argumento")

else:
    print("Erro: Comando inválido")