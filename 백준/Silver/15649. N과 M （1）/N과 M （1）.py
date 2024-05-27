from itertools import permutations

N, M = map(int, input().split())
numbers = [(i+1) for i in range(N)]
result = list(permutations(numbers, M))

for i in result:
    print(*i)