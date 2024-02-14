def perm(k):
    if k == N:
        for i in range(N):
            idx = check[i]
            print(arr[idx], end=' ')
        print()
        return
    for i in range(N):
        if visited[i] == False:
            check[k] = i
            visited[i] = True
            perm(k + 1)
            visited[i] = False

N = int(input())
arr = [(i+1) for i in range(N)]
check = [-1] * N
visited = [False] * N
perm(0)