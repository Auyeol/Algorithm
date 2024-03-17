import sys
num = int(sys.stdin.readline())
result = 0

for i in range(1, num):
    sum_v = i
    arr = list(str(i))
    for v in arr:
        sum_v += int(v)
    if sum_v == num:
        result = i
        break

print(result)