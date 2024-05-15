import sys
input = sys.stdin.readline
N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(N):
    N, M = map(int, input().split())
    for row in range(90-M, 100-M):
        for col in range(N, N+10):
            arr[row][col] = 1

for row in range(100):
    for col in range(100):
        if arr[row][col] == 1:
            cnt += 1

print(cnt)