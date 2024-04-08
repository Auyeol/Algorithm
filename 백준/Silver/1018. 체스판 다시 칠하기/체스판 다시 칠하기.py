import sys
N, M = map(int, sys.stdin.readline().split())   # N, M을 입력받음
arr = [sys.stdin.readline() for _ in range(N)]   # 주어진 체스판을 입력받음

row_repeat = N - 7                  # 행에 대한 반복 횟수
col_repeat = M - 7                  # 열에 대한 반복 횟수
result = 1e10                       # 결과값 큰 값으로 초기화
for r in range(row_repeat):
    for c in range(col_repeat):
        W_case = 0                  # 흰색이 첫번째 칸인 경우
        B_case = 0                  # 검은색이 첫번째 칸인 경우

        for row in range(r, r + 8): # 8행 반복
            for col in range(c, c + 8): # 8열 반복
                if (row+col) % 2 == 0:  # 해당 위치가 짝수 위치인 경우
                    if arr[row][col] == 'W': # 해당 위치가 흰색이면
                        # W_case 흰색은 칠할 필요 없음
                        B_case += 1         # 검은색으로 시작하는 경우 검은색으로 칠해줘야함
                    else:                    # 해당 위치가 검은색인경우
                        # B_case 검은색은 칠할 필요 없음
                        W_case += 1         # 흰색으로 시작하는 경우 흰색으로 칠해주어야함
                else:                   # 해당 위치가 홀수 위치인 경우
                    if arr[row][col] == 'W': # 해당 위치가 흰색이면
                        W_case += 1         # 흰색으로 시작하는 경우 검은색으로 칠해주어야함
                    else:                    # 해당 위치가 검은색인 경우
                        B_case += 1         # 검은색으로 시작하는 경우 흰색으로 칠해주어야함

        min_v = min(W_case, B_case)
        result = min(min_v, result)

print(result)
