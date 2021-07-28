import sys
cycle = 1
a = int(sys.stdin.readline())
b = (a%10)*10 + (a//10 + a%10)%10
while b != a:
    b = (b%10)*10 + (b//10 + b%10)%10
    cycle += 1
    if b == a:
        break

print(cycle)




