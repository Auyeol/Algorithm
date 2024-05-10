import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC):
    Q = deque()
    Q.append((stR, stC))
    visited[stR][stC] = 1
    melt = []
    cnt = 0
    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = vR + dr
            newC = vC + dc


            if 0<=newR<N and 0<=newC<M and visited[newR][newC] != 1:
                visited[newR][newC] = 1
                if arr[newR][newC] == 0:
                    Q.append((newR, newC))
                else:
                    melt.append((newR, newC))

    for x, y in melt:
        arr[x][y] = 0

    return len(melt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = []
bfs_cnt = 1
cnt = 0
for i in range(N):
    cnt += sum(arr[i])

while True:
    visited = [[0]*M for _ in range(N)]
    meltCnt = bfs(0, 0)
    cnt -= meltCnt
    if cnt == 0:
        break
    bfs_cnt += 1

print(bfs_cnt)
print(meltCnt)
