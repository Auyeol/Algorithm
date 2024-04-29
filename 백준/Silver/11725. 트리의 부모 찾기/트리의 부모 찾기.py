import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(now, lst):
    visited[now] = 1
    for w in G[now]:
        if not visited[w]:
            lst.append((w, now))

            dfs(w, lst)
    return lst

N = int(input())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

result = dfs(1, [])
result.sort()

for elem in result:
    print(elem[1])