def dfs(now, start, result):
    if now == M:
        print(*result)
        return

    for i in range(start, N+1):
        if not visited[i]:
            dfs(now+1, start, result + [i])
            start += 1

N, M = map(int, input().split())
visited = [False] * (N+1)
dfs(0, 1, [])