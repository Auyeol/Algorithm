import sys
from collections import deque
input = sys.stdin.readline

def dfs(now):
    dfs_result.append(now)
    visited[now] = True

    for w in sorted(G[now]):
        if not visited[w]:
            dfs(w)
    return dfs_result

def bfs(now):
    Q = deque()
    visited = [False] * (N+1)
    Q.append(now)
    visited[now] = True
    while Q:
        v = Q.popleft()
        bfs_result.append(v)
        for w in sorted(G[v]):
            if not visited[w]:
                Q.append(w)
                visited[w] = True


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dfs_result = []
bfs_result = []
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)