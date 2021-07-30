a = []
for b in range(1, 100):
    a.append(b)
for x in range(100,1001):
    k = str(x)
    if int(k[2])-int(k[1]) == int(k[1])-int(k[0]):
        a.append(int(x))

import sys
n = int(sys.stdin.readline())
y = []
for i in a:
    if i <= n:
        y.append(i)

print(len(y))


