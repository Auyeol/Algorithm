from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = [(i+1) for i in range(N)]
result = list(combinations_with_replacement(arr, M))

for i in result:
    print(*i)