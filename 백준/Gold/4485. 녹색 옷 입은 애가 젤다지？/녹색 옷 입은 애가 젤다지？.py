import sys
from heapq import heappush, heappop

def solve():
    INF = 1e10
    cost = [[INF]*N for _ in range(N)]
    cost[0][0] = ARR[0][0]
    Q = [(0,0)]

    while Q:
        row, col = heappop(Q)

        # 상, 하, 좌, 우
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_r = row + dr
            new_c = col + dc


            if 0<=new_r<N and 0<=new_c<N:
                if cost[new_r][new_c] > cost[row][col] + ARR[new_r][new_c]:
                    cost[new_r][new_c] = cost[row][col] + ARR[new_r][new_c]
                    heappush(Q, (new_r, new_c))

    return cost[N-1][N-1]


tc = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    ARR = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(f'Problem {tc}: {solve()}')
    tc += 1
