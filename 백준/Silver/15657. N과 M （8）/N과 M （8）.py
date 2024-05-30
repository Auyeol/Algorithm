N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * N
result = []

def dfs(now, st, lst):
    if now == M:
        result.append(lst)
        return

    for i in range(st, N):
        dfs(now+1, st, lst + [arr[i]])
        st += 1

dfs(0,0, [])

for i in result:
    print(*i)