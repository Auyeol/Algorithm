import sys
from collections import deque
input = sys.stdin.readline

# 방향 (북, 동, 남, 서)
dr = [-1, 0, 1, 0]
dc = [0,  1, 0, -1]

def solve(stR, stC, D):
    global cnt
    Q = deque()
    Q.append((stR, stC))
    visited[stR][stC] = 1
    cnt += 1
    while Q:
        curR, curC = Q.popleft()
        flag = 0

        # 현재 칸의 주변 4칸 충 청소되지 않은 빈 칸이 있는 경우
        # 플래그를 1로 설정하고 플래그가 1인동안 반복하여 방향 바꾸기
        for _ in range(4):
            D = (D + 3) % 4
            newR = curR + dr[D]
            newC = curC + dc[D]

            if 0<=newR<N and 0<=newC<M and arr[newR][newC] != 1 and visited[newR][newC] != 1:
                visited[newR][newC] = 1
                Q.append((newR, newC))
                cnt += 1
                flag = 1
                break

        if flag == 0:
            if arr[curR - dr[D]][curC - dc[D]] != 1:
                Q.append((curR-dr[D], curC-dc[D]))
            else:
                break

    return

N, M = map(int, input().split())
stR, stC, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

cnt = 0

solve(stR, stC, D)
print(cnt)