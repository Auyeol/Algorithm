import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC, visited):
    Q = deque()
    Q.append((stR, stC))
    visited[stR][stC] = 1

    while Q:
        vR, vC = Q.pop()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = vR + dr
            newC = vC + dc

            if arr[newR][newC]>0 and visited[newR][newC] != 1:
                Q.append((newR, newC))
                visited[newR][newC] = 1


def solve():
    for year in range(1, 900000):

        check = [[0]*M for _ in range(N)]
        for row in range(1, N):
            for col in range(1, M):
                if arr[row][col] == 0:
                    continue
                else:
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if arr[row+dr][col+dc] == 0:
                            check[row][col] += 1

        for row in range(1, N):
            for col in range(1, M):
                arr[row][col] = max(0, arr[row][col] - check[row][col])


        bfs_cnt = 0
        visited = [[0]*M for _ in range(N)]
        for row in range(1, N):
            for col in range(1, M):
                if arr[row][col] != 0 and visited[row][col] == 0:
                    bfs(row, col, visited)
                    bfs_cnt += 1

                if bfs_cnt > 1:
                    return year

        if bfs_cnt == 0:
            return 0




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = solve()

print(result)