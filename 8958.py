import sys
n = int(sys.stdin.readline())

for i in range(n):
    m = sys.stdin.readline()
    count = 0
    score = 0
    for a in range(len(m)):
        if m[a] == 'O':
            count += 1
            score += count
        if m[a] == 'X':
            count = 0

    print(score)