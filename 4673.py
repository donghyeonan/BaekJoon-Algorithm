def num(i):
    a = 0
    for x in list(str(i)):
        a += int(x)
    return a + int(i)
a = []
for i in range(1,10001):
    k = num(i)
    a.append(k)

for b in range(1,10001):
    if b not in a:
        print(b)