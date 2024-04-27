import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC):
    Q = deque()

    Q.append((stR, stC))
    arr[stR][stC] = 0

    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newR = vR + dr
            newC = vC + dc

            if 0<=newR<N and 0<=newC<M and arr[newR][newC] != 0:

                Q.append((newR, newC))
                arr[newR][newC] = 0


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    cnt = 0
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1:
                bfs(row, col)
                cnt += 1

    print(cnt)



"""     
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
"""