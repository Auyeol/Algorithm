import sys
N = int(sys.stdin.readline())
sum_v = 0

for _ in range(N):
    num1, num2 = map(int, sys.stdin.readline().split())
    sum_v += num2%num1
print(sum_v)