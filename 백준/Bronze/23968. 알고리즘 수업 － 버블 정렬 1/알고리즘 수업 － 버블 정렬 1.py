import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
result = []

for i in range(N-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            cnt += 1
            if cnt == K:
                result.append(A[j+1])
                result.append(A[j])
            A[j], A[j+1] = A[j+1], A[j]


if result:
    print(*result)
else:
    print(-1)
