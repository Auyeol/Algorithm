import sys
N = int(sys.stdin.readline())
fact = 1
for i in range(N, 1, -1):
    fact *= i

fact = str(fact)[::-1]
cnt = 0

for i in range(len(fact)):
    if fact[i] == '0':
        cnt += 1
    else:
        break

print(cnt)