def perm(level, cur_s, check):
    global max_v
    if cur_s > M:
        return

    if level == 3:
        if cur_s > max_v:
            max_v = cur_s
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        perm(level + 1, cur_s + arr[i], check)
        check[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
check = [False] * N
max_v = -1e10
perm(0, 0, check)
print(max_v)