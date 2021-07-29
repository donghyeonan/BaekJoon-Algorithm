import sys
N = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
print(min(m),max(m))

# map은 한번만 순회할 수 있다. 그래서 list 형태로 가야한다.