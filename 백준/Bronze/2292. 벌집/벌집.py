import sys
num = int(sys.stdin.readline())

idx = 1
cnt = 0
while True:
    if num > idx:
        cnt += 1
        idx += (6 * cnt)

    else:
        break
print(cnt+1)