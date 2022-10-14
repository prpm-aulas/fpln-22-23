# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

l = ['abc', 'xyz', 'aba', '1221', 'olllllllla']

contador = 0
for elem in l:
	if len(elem) >= 2 and elem[0] == elem[-1]:
		contador += 1

print(contador)
