import json


f = open("pessoas.txt")
l = json.load(f)
f.close()

# l = ["a", "b", "c", "d", "e"]

# for e in l:
# 	print(e)

size = len(l)
x = size - 1
while x >= 0:
	print(l[x])
	x = x - 1

