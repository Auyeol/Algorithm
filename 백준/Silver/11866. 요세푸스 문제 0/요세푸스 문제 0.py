# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉음
# 양의 정수 K가 주어진다
from collections import deque
N, K = map(int, input().split())
deQ = deque([i+1 for i in range(N)])
result = []
while deQ:
    for _ in range(K-1):
        deQ.append(deQ.popleft())
    result.append(deQ.popleft())

print('<', end='')
for i in range(N-1):
    print(f'{result[i]},', end=' ')
print(result[-1], end='')
print('>')