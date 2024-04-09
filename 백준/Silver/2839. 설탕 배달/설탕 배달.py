N = int(input())
result = 0
cnt = 0
while True:
    if N % 5 == 0:  # 5로 나누어지면 현재 결과에 나눈값 +
        result = cnt + N//5
        break
    else:
        N -= 3
        cnt += 1

    if 0 < N <= 2:
        result = -1
        break

    if N <= 0:  # 멈추는 조건
        result = cnt
        break

print(result)