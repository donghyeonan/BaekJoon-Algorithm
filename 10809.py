import sys
eng = []
word = sys.stdin.readline()

for i in range(97,123):
	eng.append(chr(i))

new = []

for l in range(len(eng)):
	if eng[l] in word:
		new.append(word.index(eng[l]))
	else:
		new.append(-1)
	print(new[l], end=' ')


