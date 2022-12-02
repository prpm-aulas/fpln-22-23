import re

f = open("processos.txt")

for line in f:

	# procurar por um certo padrao na linha
	# if re.search(r"Benedito|Benedita", line):
	# 	print(line)

	# Procurar todas as linhas que têm ou Benedito ou Benedita
	# if re.search(r"Benedit[oa]", line):
	# 	print(line)

	# Procurar todas as linhas que têm Baptista, com o 'p' opcional, sendo que o 'B' 
	# pode ser minusculo ou maiusculo, OU Polidoro
	# if re.search(r"[Bb]ap?tista|Polidoro", line):
	# 	print(line)

	# Procurar todos os nomes que começam em 'B' e acabam em 'a'
	# if re.search(r"[^a-z][Bb][a-z]*a[^a-z]", line):
	# 	print(line)

	# Procurar todos os nomes completos que têm como primeiro nome 'Adelino' e como ultimo nome 'Ferreira'
	if re.search(r":Adelino ([A-Z][a-z]+ )*Ferreira:", line):
		print(line)


f.close()