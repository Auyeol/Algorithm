def dfs(now, result):
    if now == M + 1:
        print(*result)
        return

    for i in range(1, N+1):
        dfs(now+1, result + [i])


N, M = map(int, input().split())
dfs(1, [])
