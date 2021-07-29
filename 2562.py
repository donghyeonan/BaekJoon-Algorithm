import sys
A = []
for _ in range(9):
    A.append(int(sys.stdin.readline()))
print(max(A))
print(A.index(max(A))+1)
