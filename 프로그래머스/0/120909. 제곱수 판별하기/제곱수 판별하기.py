def solution(n):
    idx = 1
    while idx ** 2 <= n:
        if idx ** 2 == n:
            return 1
        idx += 1
    return 2