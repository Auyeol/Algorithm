import sys
N = 9

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_arr = []
for row in range(N):
    max_v = -1e10
    for col in range(N):
        if max_v < arr[row][col]:
            max_v = arr[row][col]
            r = row + 1
            c = col + 1
    max_arr.append((max_v,r,c))

result = list(max(max_arr))
print(result[0])
print(result[1], result[2])