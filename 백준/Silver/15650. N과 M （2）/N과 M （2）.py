def dfs(now,st, lst):
    if now == M:
        S.append(lst)
        return


    for i in range(st +1 , N+1):
        if not visited[now]:
            visited[now] = 1
            dfs(now + 1, i, lst + [i])
            visited[now] = 0

N, M = map(int, input().split())
visited = [0] * (N+1)
S = []
dfs(0,0,[])

for elem in S:
    print(*elem)