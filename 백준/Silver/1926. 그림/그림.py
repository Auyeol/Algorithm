from collections import deque

def bfs(stR, stC, visited, arr, N, M):
    bfs_cnt = 1
    Q = deque()
    Q.append((stR, stC))
    visited[stR][stC] = 1  # 시작점을 방문했다고 표시

    while Q:
        vR, vC = Q.popleft()

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            newR = vR + dr
            newC = vC + dc

            if 0 <= newR < N and 0 <= newC < M and visited[newR][newC] != 1 and arr[newR][newC] != 0:
                Q.append((newR, newC))
                bfs_cnt += 1
                visited[newR][newC] = 1  # 방문했다고 표시

    return bfs_cnt

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
max_v = 0

# 모든 위치를 확인
for row in range(N):
    for col in range(M):
        if arr[row][col] == 1 and visited[row][col] != 1:
            area = bfs(row, col, visited, arr, N, M)
            cnt += 1
            max_v = max(area, max_v)

print(cnt)
print(max_v)
