import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    b = a[1:]
    m = sum(b) / a[0]
    count = 0
    for i in range(1, len(a)):
        if a[i] > m:
            count += 1
        result = (count/a[0]) * 100

    print(('%.3f' %result)+'%')