N, M = map(int, input().split())
chess = list(input() for _ in range(N))

row_repeat = N - 7
col_repeat = M - 7
result = 1e10

for r in range(row_repeat):
    for c in range(col_repeat):

        W_cnt = 0   # 흰색으로 시작하는 경우
        B_cnt = 0   # 검은색으로 시작하는 경우
        for row in range(r, r + 8):
            for col in range(c, c + 8):
                if (row+col) % 2 == 0:  # 짝수인 경우
                    if chess[row][col] == 'B':  # 검은색이면
                        W_cnt += 1 # 흰색 기준, 흰색으로 칠해주어야함
                    else:                       # 흰색이면
                        B_cnt += 1 # 검은색 기준, 검은색으로 칠해주어야함

                else:                   # 홀수인 경우
                    if chess[row][col] == 'B':  # 검은색이면
                        B_cnt += 1  # 검은색 기준, 흰색으로 칠해주어야함
                    else:                       # 흰색이면
                        W_cnt += 1  # 흰색 기준, 검은색으로 칠해주어야함

        min_v = min(W_cnt, B_cnt)
        result = min(result, min_v)

print(result)


