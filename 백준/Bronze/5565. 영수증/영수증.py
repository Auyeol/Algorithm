import sys
N = 10
total = int(sys.stdin.readline())
for _ in range(N-1):
    total -= int(sys.stdin.readline())
print(total)
