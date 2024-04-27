import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC, visit):
    Q = deque()

    Q.append((stR, stC))
    arr[stR][stC] = 0

    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = vR + dr
            newC = vC + dc

            if 0<=newR<N and 0<=newC<N and arr[newR][newC] != 0:
                visit += 1
                Q.append((newR, newC))
                arr[newR][newC] = 0
    return visit

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0
result = []
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            cnt += 1
            result.append(bfs(row, col, 1))

print(cnt)
result.sort()

for r in result:
    print(r)