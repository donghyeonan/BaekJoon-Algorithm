import sys
w = sys.stdin.readline().rstrip()
cnt = 0
cr = ['c=','c-','d-','lj','nj','s=','z=']

for i in range(len(w)-1):
	if w[i:i+2] in cr:
		cnt += 1
	elif w[i:i+3] == 'dz=':
		cnt += 1
		
print(len(w)-cnt)
