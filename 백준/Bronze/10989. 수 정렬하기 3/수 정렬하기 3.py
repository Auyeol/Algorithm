import sys

N = int(sys.stdin.readline())

lst = []

# a를 이용해서 값을 append 하는 경우 a가 계속 재정의되기 떄문에
# 많은 메로리를 차지하게 됨
# for _ in range(N):
#     a = int(sys.stdin.readline())
#     lst.append(a)


lst = [0] * 10001   # 리스트 생성
for i in range(N):
    lst[(int(sys.stdin.readline()))] += 1
for i in range(1, len(lst)):   # 1000번 반복

    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i)