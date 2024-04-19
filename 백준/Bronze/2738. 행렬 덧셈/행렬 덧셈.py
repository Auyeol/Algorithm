import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(M):
        arr1[row][col] += arr2[row][col]

for row in range(N):
    print(*arr1[row])