import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(now):
    ST = []
    ST.append(now)

    while ST:
        v = ST.pop()
        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

for i in range(1, len(visited)):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)