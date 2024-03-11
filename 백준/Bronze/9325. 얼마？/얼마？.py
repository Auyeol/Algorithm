import sys
T = int(sys.stdin.readline())

for _ in range(T):
    S = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    for _ in range(N):
        num, money = map(int, sys.stdin.readline().split())
        S += num * money

    print(S)