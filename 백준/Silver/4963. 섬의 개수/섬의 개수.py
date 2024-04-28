import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC):
    Q = deque()

    Q.append((stR, stC))
    arr[stR][stC] = 0

    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(1,-1),(-1,1)]:
            newR = vR + dr
            newC = vC + dc

            if 0<=newR<H and 0<=newC<W and arr[newR][newC] != 0:
                Q.append((newR, newC))
                arr[newR][newC] = 0

while True:
    W, H = map(int, input().strip().split())

    if W == H == 0:
        break

    arr = [list(map(int, input().strip().split())) for _ in range(H)]
    cnt = 0

    for row in range(H):
        for col in range(W):
            if arr[row][col] == 1:
                cnt += 1
                bfs(row, col)
    print(cnt)