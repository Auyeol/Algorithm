import sys
T = int(sys.stdin.readline())

for tc in range(1,T+1):
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        name, num = sys.stdin.readline().split()
        num = int(num)
        arr.append((num,name))

    print(max(arr)[1])