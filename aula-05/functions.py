
def print_bonito(conteudo):
	print("===================")
	print(conteudo)
	print("===================")


def soma(x,y):
	return x + y


# programa
print_bonito("Calculadora")

# ler 2 numeros
print_bonito("Insira 2 números")
a = int(input())
b = int(input())

# calcular a soma
s = soma(a, b)

# imprimir o resultado
print_bonito(f'O resultado é {s}')

print_bonito("Calculadora desligada")


