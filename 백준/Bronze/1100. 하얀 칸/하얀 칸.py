N = 8
M = 8

arr = [input() for _ in range(N)]
cnt = 0
check = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]

for row in range(8):
    for col in range(8):
        if check[row][col] == 'W' and arr[row][col] == 'F':
            cnt += 1

print(cnt)