import sys
from collections import deque
input = sys.stdin.readline

def bfs(stR, stC):
    global visited

    Q = deque()

    Q.append((stR, stC))
    visited[stR][stC] = 0

    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = vR + dr
            newC = vC + dc

            if 0<=newR<N and 0<=newC<N and visited[newR][newC] == 1:
                Q.append((newR, newC))
                visited[newR][newC] = 0

# N x N 행렬 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 해당 행렬의 최대값 구하기
max_v = -1e10
for row in range(N):
    for col in range(N):
        max_v = max(max_v, arr[row][col])

# 결과값을 저장할 빈 리스트 생성
result = []

# 0부터 최대값까지 BFS
for value in range(max_v + 1):
    cnt = 0             # bfs 시행 횟수 세기
    visited = [[0]*N for _ in range(N)]
    # 강수량보다 높은 건물인 경우 값을 1로 변경
    for row in range(N):
        for col in range(N):
            if arr[row][col] >= value:
                visited[row][col] = 1


    for row in range(N):
        for col in range(N):
            if visited[row][col] == 1:
                cnt += 1
                bfs(row, col)

    result.append(cnt)

print(max(result))