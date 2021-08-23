import sys
word = sys.stdin.readline().rstrip().upper()
cnt = list(set(word))
a = []

for i in range(len(cnt)):
	a.append(word.count(cnt[i]))
	m = max(a)
	b = a.index(m)

if a.count(m) == 1:
	print(cnt[b])
elif a.count(m) >= 2:
	print('?')
