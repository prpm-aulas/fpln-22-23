# Write a Python program to get the largest number from a list.

l = [-2, -5, 20, -3, -1, -6]

maximo = -100000 # definir um valor que serve como limite inferior para o máximo
for elem in l:
	if elem > maximo:
		maximo = elem

print(maximo)

minimo = 100000 # definir um valor que serve como limite superior para o mínimo
for elem in l:
	if elem < minimo:
		minimo = elem

print(minimo)
