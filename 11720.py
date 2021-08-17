import sys
a = int(sys.stdin.readline())
b = str(sys.stdin.readline())
c = []
for N in range(a):
    c.append(int(b[N]))
    total = sum(c)

print(total)


