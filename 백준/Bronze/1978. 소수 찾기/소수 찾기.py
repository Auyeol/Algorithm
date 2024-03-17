import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for num in arr:
    cnt = 0
    if num == 1:
        continue
    else:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            result += 1

print(result)