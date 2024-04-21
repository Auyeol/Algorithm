import sys

input = sys.stdin.readline
N = int(input())
num_dict = {}
for i in range(1, N+1):
    num_dict[i] = 0

board = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    stR, stC, width, height = map(int, input().split())

    for r in range(width):
        row = stR + r
        for c in range(height):
            col = stC + c
            board[row][col] = i

for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] != 0:
            if board[row][col] in num_dict:
                num_dict[board[row][col]] += 1

if N == 0:
    print(0)
else:
    for i in range(1, N+1):
        print(num_dict[i])

