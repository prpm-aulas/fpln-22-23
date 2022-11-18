import sys
import json

def busca_codigo(nome_local):
    f = open("previsoes/locais.json")
    # importar o ficheiro para um dicionário
    dicionario_codigos = json.load(f)
    f.close()

    return dicionario_codigos[nome_local]


def busca_previsoes(codigo):
    f = open(f"previsoes/{codigo}.json")
    previsoes = json.load(f)
    f.close()

    return previsoes['data']


def busca_previsao_dia(codigo, dia):
    f = open(f"previsoes/{codigo}.json")
    previsoes = json.load(f)
    f.close()

    return previsoes['data'][dia - 1]
    


def imprime_previsoes(previsoes):
    for previsao in previsoes:
        data = previsao["forecastDate"]
        t_min = previsao["tMin"]
        t_max = previsao["tMax"]
        prob_chuva = previsao["precipitaProb"]

        print(f"----------------------")
        print(f"Previsão - {data}")
        print(f"----------------------")
        print(f"Temperatura Máxima: {t_max} C")
        print(f"Temperatura Mínima: {t_min} C")
        print(f"Probabilidade de precipitação: {prob_chuva}%")
        print()


def imprime_ajuda():
    print("Utilização:")
    print("  python3 meteo.py [comando] [argumentos...]")
    print()
    print("  Comando:")
    print("    min - Imprimir as localidades com a temperatura mínima mais alta e mais baixa")
    print("    max - Imprimir as localidades com a temperatura máxima mais alta e mais baixa")
    print("    [local] [dia] - Local do qual queremos ir buscar as previsões (obrigatório),")
    print("                    podendo passar um dia em específico") 
    print("                      Ex.: Braga 1")



# lista de argumentos, exceto o nome do programa
args = sys.argv[1:]
n_args = len(args)

if n_args == 0:
    print("Erro: Não foi introduzido um local.")
    # parar o programa
    exit()

elif n_args == 1:
    # verificar se o argumento é "ajuda"
    if args[0] == "ajuda":
        imprime_ajuda()
        exit()

    # if args[0] == "help":
    #     print_help()
    #     exit()

    # apenas foi passado um local
    local = args[0]

    codigo = busca_codigo(local)
    previsoes = busca_previsoes(codigo)
    imprime_previsoes(previsoes)

elif n_args == 2:
    # foram passados um local e uma dia
    local = args[0]

    dia = int(args[1])
    if dia < 1 or dia > 5:
        print("Erro: Dia inválido (tem de ser: 1-5).")
        exit()
    
    codigo = busca_codigo(local)
    previsao = busca_previsao_dia(codigo, dia)
    imprime_previsoes([previsao])





