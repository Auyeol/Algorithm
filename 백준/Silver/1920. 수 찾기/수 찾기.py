import sys
def func(st, ed, key):
    s = st
    e = ed

    while s <= e:
        mid = (s+e)//2
        if mid >= len(A):
            return 0
        elif A[mid] == key:
            return 1

        elif key > A[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return 0


# 첫째 줄에 자연수 N이 주어진다
N = int(sys.stdin.readline())
# N개의 정수가 주어진다 / A[0], A[1], A[2] ....
A = list(map(int, sys.stdin.readline().split()))

# M이 주어진다
M = int(sys.stdin.readline())
# M개의 정수가 주어진다 / 이 수들이 A안에 존재하는 지 알아내면 된다.
lst_M = list(map(int, sys.stdin.readline().split()))

A.sort()
# 결과를 저장할 배열 생성
result = [0] * M

for i in range(M):
    result[i] = func(0, len(A), lst_M[i])

for elem in result:
    print(elem)