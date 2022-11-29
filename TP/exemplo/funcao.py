
# definir uma função
def soma(x, y):
    print(f"A calcular a soma de {x} e {y}")
    return x + y



# a chamar a função
# print(soma(2, 5))
# print(soma(10, 15))
# print(soma(10, 20))


nome = "Pedro"

# Passo 1
f = open("nomes.txt")
lista = f.readlines()
f.close()

# Passo 2
print(lista)
lista.remove(nome + '\n')
print(lista)

# Passo 3
f = open("nomes.txt", mode='w')
for nome in lista:
    f.write(nome.strip() + '\n')

f.close()



