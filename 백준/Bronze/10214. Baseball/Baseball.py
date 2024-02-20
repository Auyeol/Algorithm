import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A_cnt = 0
    B_cnt = 0
    for i in range(9):
        A, B = map(int, sys.stdin.readline().split())

        if A > 0:
            A_cnt += A
        if B > 0:
            B_cnt += B

    if A_cnt > B_cnt:
        print('Yonsei')
    elif A_cnt < B_cnt:
        print('Korea')
    else:
        print('Draw')
