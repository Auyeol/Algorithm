N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
def dfs(now, lst):
    if now == M:
        result.append(lst)
        return

    for i in range(N):
        dfs(now+1, lst + [arr[i]])


dfs(0, [])

result.sort()

for i in result:
    print(*i)
