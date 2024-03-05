import sys
import math

arr = []
M = int(sys.stdin.readline()) # M 이상
N = int(sys.stdin.readline()) # N 이하

st = int(math.sqrt(M))
ed = int(math.sqrt(N))

for i in range(st, ed+1):
    num = i**2
    if M <= num <= N:
        arr.append(num)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))