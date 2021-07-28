import sys
while True:
    A,B = map(int,sys.stdin.readline().split())
    if A != 0 and B != 0:
        print(A+B)
    elif A ==0 and B==0:
        break