# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def dfs(now, lst):
    if now == M:
        S.append(lst)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(now+1, lst + [i])
            visited[i] = 0

N, M = map(int, input().split())
visited = [0] * (N+1)
S = []

dfs(0, [])

for elem in S:
    print(*elem)