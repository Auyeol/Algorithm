import sys
num = int(sys.stdin.readline())
result = 0

for i in range(1, num):
    sum_v = i + sum(map(int, str(i)))
    
    if sum_v == num:
        result = i
        break

print(result)