import sys
from collections import deque

def bfs(stR, stC):
    Q = deque()

    Q.append((stR, stC))
    arr[stR][stC] = 1
    cnt = 1
    while Q:
        vR, vC = Q.pop()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = dr + vR
            newC = dc + vC

            if 0<=newR<M and 0<=newC<N and arr[newR][newC] == 0:
                cnt += 1
                Q.append((newR, newC))
                arr[newR][newC] = 1
    return cnt

input = sys.stdin.readline

M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]
result = []
for _ in range(K):
    stR, stC, edR, edC = map(int, input().split())

    row_cnt = abs(stR-edR)
    col_cnt = abs(stC-edC)

    for row in range(row_cnt):
        for col in range(col_cnt):
            arr[stC+col][stR+row] = 1

for col in range(N):
    for row in range(M-1, -1, -1):
        if arr[row][col] == 0:
            result.append(bfs(row, col))
result.sort()

print(len(result))
print(*result)