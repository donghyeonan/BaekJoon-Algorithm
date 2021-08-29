import sys
N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
	word = sys.stdin.readline().rstrip()
	a = []
	for i in range(len(word)):
		if word[i] not in a:
			a.append(word[i])
		elif word[i] in a and a[i-1] == word[i]:
			a.append(word[i])
		elif word[i] in a and a[i-1] != word[i]:
			break
			
	if len(a) == len(word):
		cnt += 1
	else:
		pass
		
print(cnt)
