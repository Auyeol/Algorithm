N = int(input())
lst = []
result = [1] * N
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

for i in range(N):
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            result[i] += 1

print(*result)
