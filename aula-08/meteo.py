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

# lista de argumentos, exceto o nome do programa
args = sys.argv[1:]

if args == []:
    print("Erro: Não foi introduzido um local.")
    # parar o programa
    exit()

# extrair o local
local = args[0]

codigo = busca_codigo(local)
previsoes = busca_previsoes(codigo)
imprime_previsoes(previsoes)
