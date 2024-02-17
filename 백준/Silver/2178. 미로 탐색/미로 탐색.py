def bfs(stR, stC): # 시작 행, 열을 매개변수로 받음
    Q = []          # 큐 생성
    visited = [[0] * M for _ in range(N)] # 방문표시를 할 리스트 NxM 생성
    Q.append((stR, stC))            # 시작행, 시작열 append
    visited[stR][stC] = 1          # append한 위치에 1로 방문표시, 이후에 값을 반환할 때 -1

    while Q: # 큐가 존재하는 동안 반복
        vR, vC = Q.pop(0) # 맨 앞의 값 pop

        for dr, dc in [(0,-1),(0,1),(-1,0),(1,0)]: # 상, 하, 좌, 우 이동
            newR = dr + vR # 이동한 좌표
            newC = dc + vC
            if 0<=newR<N and 0<=newC<M and visited[newR][newC] == 0 and arr[newR][newC] == 1: # 이동한 좌표가 범위 내에 존재하고, 방문하지 않은 곳일 떄
                if newR == N - 1 and newC == M - 1:  # 4x6 배열의 좌표는 (3, 5)이므로
                    return visited[vR][vC] + 1 # 현재까지의 이동거리에 + 1한 값을 반환
                                                # visited[vR][vC]에는 현재까지의 이동거리가 저장되어있기 때문에
                Q.append((newR, newC))  # Q에 새로운 좌표 append
                visited[newR][newC] = visited[vR][vC] + 1 # 방문표시, 지금까지 이동한 거리에 + 1

    return 0

import sys
N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, input().strip())) for _ in range(N)] # 2차원 리스트로 변경

print(bfs(0,0)) # (1,1)에서 출발