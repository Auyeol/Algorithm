import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    global cnt
    visited[now] = cnt

    for w in sorted(G[now], reverse=True):
        if visited[w] == 0:
            cnt += 1
            dfs(w)

    return visited

cnt = 1

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
result = []
visited = [0] * (N + 1)
for _ in range(M):
    v1, v2 = map(int, input().split())

    G[v1].append(v2)
    G[v2].append(v1)

result = dfs(R)

for i in range(1, len(result)):
    print(result[i])