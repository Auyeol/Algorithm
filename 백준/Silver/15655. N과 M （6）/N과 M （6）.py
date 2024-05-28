def dfs(now, start, result):
    if now == M:
        result_set.add(tuple(sorted(result)))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            dfs(now+1, start, result + [arr[i]])
            visited[i] = False
            start += 1


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result_set = set()
visited = [False] * (N+1)
dfs(0, 0, [])

for r in sorted(result_set):
    print(*r)