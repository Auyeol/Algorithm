from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = list(permutations(arr, M))

for i in result:
    print(*i)