import sys

N = int(sys.stdin.readline())
arr = [(i+1) for i in range(N)]
card_arr = list(map(int, sys.stdin.readline().split()))

for i in range(len(card_arr)):
    jump = card_arr[i] 
    for j in range(jump): 
        if i-j-1>=0:
            arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]

print(*arr)