import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split()) # 총감독관 B명, 부감독관 C명

# 총감독관 1명씩은 무조건 있어야함
# N = 3 / arr = 3 4 5 / B, C = 2 2  입력한 경우
cnt = N     # 3명은 무조건 고정
for i in range(len(arr)):
    arr[i] -= B
    if arr[i] <= 0:
        continue
    else:
        cnt += arr[i]//C
        arr[i] %= C
        if arr[i] > 0:
            cnt += 1

print(cnt)

