import sys
n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
d = sum(m) / max(m) * 100 / n
print(d)