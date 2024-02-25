import sys
N, M = map(int, sys.stdin.readline().split())

arr_1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr_2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for row in range(N):
    for col in range(M):
        arr_1[row][col] += arr_2[row][col]

for row in range(N):
    for col in range(M):
        print(arr_1[row][col], end=' ')
    print()