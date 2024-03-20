# 그래프를 DFS로 탐색한 결과, BFS로 탐색한 결과를 출력하는 프로그램 작성
# 방문할 수 있는 점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 탐색
# 방문할 수 있는 점이 없는 경우 종료
# 정점 번호는 1~N
from collections import deque


def dfs(num):
    visited[num] = True
    path_dfs.append(num)

    """
    print('sorted -> ', sorted(G[num]))
    sorted ->  [1, 4]
    sorted ->  [2, 3]
    sorted ->  [1, 5]
    sorted ->  [2, 4]
    sorted ->  [3, 5]
    """

    for w in sorted(G[num]):
        if not visited[w]:
            dfs(w)


def bfs(num):
    Q = deque()
    visited = [False] * (N + 1)
    Q.append(num)
    visited[num] = True

    while Q:
        v = Q.popleft()
        path_bfs.append(v)

        for w in sorted(G[v]):
            if not visited[w]:
                visited[w] = True
                Q.append(w)





N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False] * (N+1)
path_dfs = []
path_bfs = []
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

dfs(V)
bfs(V)

print(*path_dfs)
print(*path_bfs)
