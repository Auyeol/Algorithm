def dfs(now, lst):
    if now == M:
        S.append(lst)
        return

    for i in range(1, N+1):
        if not visited[now]:
            visited[now] = 1
            dfs(now + 1, lst + [i])
            visited[now] = 0

N, M = map(int, input().split())
visited = [0] * (N+1)
S = []
dfs(0,[])

for elem in S:
    print(*elem)