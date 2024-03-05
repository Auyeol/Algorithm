import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(sys.stdin.readline().split())
        arr[i][0] = int(arr[i][0])

    print(max(arr)[1])