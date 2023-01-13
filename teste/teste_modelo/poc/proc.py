import json


f = open("pessoas.txt", "w")

json.dump({"numero": 123}, f)

f.close()







"""
f = open("pessoas.json")

c1 = f.read()
print(c1)
print(type(c1))

f.close()


print("\n#####################\n\n")

f = open("pessoas.json")

c2 = json.load(f)
print(c2)
print(type(c2))

f.close()
"""






