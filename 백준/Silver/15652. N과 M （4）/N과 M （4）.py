def dfs(now, st, lst):
    if now == M:
        result.append(lst)
        return
    for i in range(st, N+1):
        dfs(now + 1, st, lst + [i])
        st += 1

N, M = map(int, input().split())    # 첫째 줄에 자연수 N과 M이 주어진다
result = []
dfs(0,1,[])

for elem in result:
    print(*elem)