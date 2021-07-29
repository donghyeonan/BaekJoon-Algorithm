import sys
n = []
for i in range(10):
    a = int(sys.stdin.readline())
    b = a % 42
    n.append(b)
n2 = set(n)
print(len(n2))