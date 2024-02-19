def dfs(st, find):
    ST = []
    visited = [0] * (N+1)
    ST.append(st)
    visited[st] = 1

    while ST:
        v = ST.pop()

        for w in G[v]:
            if w == find: return visited[v]

            if visited[w] == 0:
                ST.append(w)
                visited[w] = visited[v] + 1

    return -1

import sys

N = int(sys.stdin.readline()) # 노드 개수
A, B = map(int, sys.stdin.readline().split())
R = int(sys.stdin.readline()) # 엣지의 개수

G = [[] for _ in range(N+1)]
for _ in range(R):
    v1, v2 = map(int, sys.stdin.readline().split())
    G[v1].append(v2)
    G[v2].append(v1)

print(dfs(A, B))