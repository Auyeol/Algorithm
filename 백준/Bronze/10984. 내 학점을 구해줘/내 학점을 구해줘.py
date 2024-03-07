import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    sum_v = 0
    cnt = 0
    for _ in range(N):
        grade, score = map(float, sys.stdin.readline().split())
        cnt += grade
        sum_v += grade * score
    print(f'{int(cnt)}{sum_v/cnt: .1f}')