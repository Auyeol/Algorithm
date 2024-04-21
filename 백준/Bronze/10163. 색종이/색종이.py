import sys

input = sys.stdin.readline
N = int(input())

board = [[0]*1001 for _ in range(1001)]
result = []
for i in range(1, N+1):
    stR, stC, width, height = map(int, input().split())

    for r in range(width):
        row = stR + r
        for c in range(height):
            col = stC + c

            if 0<=row<1001 and 0<=col<=1001:
                board[row][col] = i

for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] != 0:
            result.append(board[row][col])

if N == 0:
    print(0)
else:
    for j in range(1, N+1):
        print(result.count(j))