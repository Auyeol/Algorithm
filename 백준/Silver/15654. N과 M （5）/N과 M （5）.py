# 자신을 제외한 모든 것
def dfs(now, lst):
    if now == M:
        S.append(lst)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(now+1, lst+[arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
arr.sort()
S = []
visited = [0] * (N+1)
dfs(0, [])

for elem in S:
    print(*elem)