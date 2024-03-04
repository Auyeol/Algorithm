def cal(T):
    A = B = C = 0
    if T % 10 != 0:
        return -1
    while T:
        if T >= 300:
            A += 1
            T -= 300
        elif T >= 60:
            B += 1
            T -= 60
        elif T >= 10:
            C += 1
            T -= 10
    return A, B, C


import sys
T = int(sys.stdin.readline())
result = cal(T)
if result == -1:
    print(-1)
else:
    print(*result)