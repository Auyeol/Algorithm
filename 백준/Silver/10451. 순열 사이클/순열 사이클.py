import sys
input = sys.stdin.readline

def dfs(now):
    visited[now] = True

    for w in G[now]:
        if not visited[w]:
            dfs(w)

T = int(input())

for _ in range(T):
    N = int(input())
    lst = [i+1 for i in range(N)]
    input_lst = list(map(int, input().split()))
    cnt = 0
    G = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for i in range(N):
        G[lst[i]].append(input_lst[i])

    for j in range(1, N+1):
        if visited[j] == False:
            dfs(j)
            cnt += 1
    print(cnt)