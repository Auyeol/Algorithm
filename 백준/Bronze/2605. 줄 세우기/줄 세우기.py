import sys

N = int(sys.stdin.readline())
arr = [(i+1) for i in range(N)]
card_arr = list(map(int, sys.stdin.readline().split()))
cur_idx = 0
for i in range(len(card_arr)):
    jump = card_arr[i] # 3이 들어오면 0,
    cur_idx = i # 0, 1, 2, 3, 4 ....
    for j in range(jump): # jump만큼 자리교체
        if i-j-1>=0:
            arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]


print(*arr)